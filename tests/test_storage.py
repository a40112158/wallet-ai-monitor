from dataclasses import replace

import pytest

from wallet_ai_monitor.hyperliquid import Position
from wallet_ai_monitor.storage import Store


def test_meta_and_ai_cache(tmp_path):
    s = Store(tmp_path / "x.sqlite3")
    s.set_meta("next_scan_offset", 600)
    assert s.get_meta("next_scan_offset") == "600"
    s.save_ai_cache("abc", "model", {"ok": True, "signals": []})
    assert s.get_ai_cache("abc", 3600)["ok"] is True
    s.close()


def test_batch_pnl_returns_cumulative_extrema_and_expires(tmp_path):
    s = Store(tmp_path / "pnl.sqlite3")
    signal = {
        "coin": "BTC",
        "side": "LONG",
        "direction": "OPEN_LONG",
        "wallet_count": 1,
        "total_delta_notional": 1000,
        "total_position_value": 1000,
        "weighted_score": 1,
        "wallets": [],
    }
    signal_id = s.insert_signal(100, signal)
    base = {
        "signal_id": signal_id,
        "current_px": 101,
        "pnl_pct": 1.0,
        "leveraged_roe_pct": 1.0,
        "pnl_usd": 10.0,
    }
    first = s.save_signal_pnls(101, [base])[0]
    assert first["mfe_pct"] == 1.0
    assert first["mae_pct"] == 1.0

    second = s.save_signal_pnls(102, [{**base, "current_px": 98, "pnl_pct": -2.0}])[0]
    assert second["mfe_pct"] == 1.0
    assert second["mae_pct"] == -2.0
    assert s.expire_signals_before(101) == 1
    assert s.recent_open_signals(0) == []
    s.close()


def test_latest_position_replacement_is_atomic(tmp_path):
    s = Store(tmp_path / "atomic.sqlite3")
    wallet = "0x" + "3" * 40
    position = Position(
        wallet=wallet,
        group="smart_money",
        weight=1.0,
        coin="BTC",
        side="LONG",
        size=1.0,
        abs_size=1.0,
        entry_px=100.0,
        mark_px=100.0,
        position_value=100.0,
        unrealized_pnl=0.0,
        roe=0.0,
        leverage=1.0,
        raw={},
    )
    s.replace_latest_for_scanned_wallets(1, [position], [wallet])
    circular = {}
    circular["self"] = circular
    with pytest.raises(ValueError):
        s.replace_latest_for_scanned_wallets(2, [replace(position, size=2.0, raw=circular)], [wallet])
    assert float(s.latest_map()[(wallet, "BTC")]["size"]) == 1.0
    s.close()


def test_ai_usage_and_state_backup(tmp_path):
    s = Store(tmp_path / "usage.sqlite3")
    s.record_ai_usage(
        ts=100, model="m", purpose="signal", usage={"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
        estimated_points=3, cached=False, ok=True,
    )
    assert s.estimated_ai_points_since(0) == 3
    assert s.run_health_summary(0)["ai_estimated_points"] == 3
    assert s.integrity_ok() is True
    backup = s.backup_database(101)
    assert backup and backup.exists()
    s.close()


def test_virtual_account_total_capital_mode(tmp_path):
    s = Store(tmp_path / "virtual.sqlite3")
    signal = {
        "coin": "BTC",
        "side": "LONG",
        "direction": "OPEN_LONG",
        "wallet_count": 1,
        "total_delta_notional": 1000,
        "total_position_value": 1000,
        "weighted_score": 1,
        "mark_px": 100.0,
        "avg_entry_px": 100.0,
        "ai_confidence": 80,
        "wallets": [],
    }
    sid = s.insert_signal(100, signal)
    assert s.open_virtual_trade(sid, 100, signal, 1666.67)
    assert round(s.virtual_open_notional(), 2) == 1666.67
    rows = s.update_virtual_trades(200, {"BTC": 110.0}, take_profit_pct=50, stop_loss_pct=50, max_hold_seconds=999999)
    assert rows[0]["notional_usd"] == 1666.67
    summary = s.virtual_summary(10000)
    assert round(summary["account_capital_usd"], 2) == 10000
    assert round(summary["open_notional_usd"], 2) == 1666.67
    assert round(summary["unrealized_pnl_usd"], 2) == 166.67
    assert round(summary["equity_usd"], 2) == 10166.67
    assert round(summary["available_notional_usd"], 2) == 8333.33
    s.close()


def test_wallet_scores_rows_for_export(tmp_path):
    s = Store(tmp_path / "wallet_scores_export.sqlite3")
    s.conn.execute(
        "INSERT OR REPLACE INTO wallet_scores(wallet,wallet_group,trades,wins,losses,avg_pnl_pct,score,quality_grade,win_rate_72h,avg_pnl_72h,trades_72h,win_rate_168h,avg_pnl_168h,trades_168h,last_updated_ts) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        ("0xaaa", "smart_money", 10, 7, 3, 4.0, 1.45, "A", 0.7, 5.0, 10, 0.6, 4.0, 10, 1000),
    )
    s.conn.commit()
    rows = s.wallet_scores_rows(limit=10)
    assert rows
    assert rows[0]["wallet"] == "0xaaa"
    assert rows[0]["quality_grade"] == "A"
    s.close()
