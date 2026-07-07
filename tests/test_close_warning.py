from wallet_ai_monitor.storage import Store
from wallet_ai_monitor.report import render_markdown, telegram_text


def _signal():
    return {
        "coin": "BTC",
        "side": "LONG",
        "direction": "OPEN_LONG",
        "wallet_count": 2,
        "total_delta_notional": 500000,
        "total_position_value": 500000,
        "weighted_score": 1,
        "mark_px": 100.0,
        "avg_entry_px": 100.0,
        "ai_confidence": 85,
        "wallets": [],
    }


def test_close_warning_near_take_profit(tmp_path):
    store = Store(tmp_path / "v.sqlite3")
    sig = _signal()
    sid = store.insert_signal(100, sig)
    tid = store.open_virtual_trade(sid, 100, sig, 1000.0, leverage=3, margin_usd=333.33)
    assert tid
    rows = store.update_virtual_trades(
        200,
        {"BTC": 106.0},
        take_profit_pct=8,
        stop_loss_pct=3,
        max_hold_seconds=999999,
        close_warning_enabled=True,
        close_warning_tp_ratio=0.75,
    )
    assert rows[0]["status"] == "OPEN"
    assert rows[0]["close_warning"] is True
    assert rows[0]["close_warning_reason"] == "NEAR_TAKE_PROFIT"


def test_close_warning_ai_pre_close(tmp_path):
    store = Store(tmp_path / "v.sqlite3")
    sig = _signal()
    sid = store.insert_signal(100, sig)
    tid = store.open_virtual_trade(sid, 100, sig, 1000.0, leverage=2, margin_usd=500)
    rows = store.update_virtual_trades(
        200,
        {"BTC": 101.0},
        take_profit_pct=8,
        stop_loss_pct=3,
        max_hold_seconds=999999,
        ai_exit_decisions={tid: {"action": "CLOSE", "confidence": 55, "reason": "flow weakening"}},
        ai_close_min_confidence=65,
        ai_pre_close_min_confidence=50,
    )
    assert rows[0]["status"] == "OPEN"
    assert rows[0]["close_warning"] is True
    assert rows[0]["close_warning_reason"] == "AI_PRE_CLOSE"


def test_report_and_tg_include_close_warning():
    rows = [{
        "id": 1,
        "coin": "BTC",
        "side": "LONG",
        "leverage": 3,
        "margin_usd": 300,
        "notional_usd": 900,
        "entry_px": 100,
        "current_px": 106,
        "pnl_pct": 6,
        "leveraged_roe_pct": 18,
        "pnl_usd": 54,
        "status": "OPEN",
        "reason": None,
        "ai_exit_confidence": 55,
        "ai_exit_reason": "flow weakening",
        "mfe_pct": 6,
        "mae_pct": 0,
        "close_warning": True,
        "close_warning_reason": "AI_PRE_CLOSE",
    }]
    text = render_markdown(100, [], [], {"reason": "test"}, virtual_rows=rows, virtual_summary={"account_capital_usd": 10000})
    assert "准备平仓提示" in text
    tg = telegram_text([], {"reason": "test"}, virtual_rows=rows)
    assert "准备平仓提示" in tg
