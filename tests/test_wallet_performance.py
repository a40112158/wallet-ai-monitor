from wallet_ai_monitor.storage import Store
from wallet_ai_monitor.signals import aggregate_signals, build_position_deltas
from wallet_ai_monitor.hyperliquid import Position


def _pos(wallet="0xaaa", group="smart_money", coin="BTC", side="LONG", size=1.0, mark=100.0):
    signed_size = size if side == "LONG" else -size
    return Position(
        wallet=wallet,
        group=group,
        weight=1.0,
        coin=coin,
        side=side,
        size=signed_size,
        abs_size=abs(size),
        entry_px=mark,
        mark_px=mark,
        position_value=abs(size) * mark,
        unrealized_pnl=None,
        roe=None,
        leverage=None,
        raw={},
    )


def test_wallet_perf_events_update_score(tmp_path):
    store = Store(tmp_path / "s.sqlite3")
    deltas = [{
        "event": "INCREASE_POSITION",
        "wallet": "0xaaa",
        "group": "smart_money",
        "coin": "BTC",
        "side": "LONG",
        "mark_px": 100.0,
        "entry_px": 100.0,
        "delta_notional": 100000.0,
        "weight": 1.0,
        "wallet_score": 1.0,
        "effective_weight": 1.0,
    }]
    assert store.record_wallet_perf_events(1000, deltas, horizons_hours=[24, 72, 168], min_delta_notional=50000) == 3
    assert store.update_wallet_perf_outcomes(1000 + 24 * 3600, {"BTC": 110.0}) == 1
    assert store.refresh_wallet_scores(1000 + 24 * 3600, min_sample_size=1) == 1
    perf = store.wallet_performance_map()["0xaaa"]
    assert perf["trades"] >= 1
    assert perf["wins"] >= 1
    assert perf["score"] > 1.0
    assert perf["quality_grade"] in {"S", "A", "B", "NEW"}


def test_signal_includes_wallet_quality(tmp_path):
    store = Store(tmp_path / "s.sqlite3")
    # Seed a proven wallet score.
    store.conn.execute(
        "INSERT OR REPLACE INTO wallet_scores(wallet,wallet_group,trades,wins,losses,avg_pnl_pct,score,quality_grade,win_rate_72h,avg_pnl_72h,trades_72h,win_rate_168h,avg_pnl_168h,trades_168h,last_updated_ts) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        ("0xaaa", "smart_money", 10, 7, 3, 4.0, 1.45, "A", 0.7, 5.0, 10, 0.6, 4.0, 10, 1000),
    )
    store.conn.commit()
    prev = {("0xaaa", "BTC"): {"size": 0.5, "side": "LONG", "mark_px": 100.0, "entry_px": 100.0, "wallet_group": "smart_money", "position_value": 50000}}
    cur = [_pos(size=1000.0, mark=100.0)]
    deltas = build_position_deltas(
        prev,
        cur,
        scanned_wallets={"0xaaa"},
        baseline_wallets={"0xaaa"},
        wallet_scores=store.wallet_score_map(),
        wallet_performance=store.wallet_performance_map(),
        wallet_perf_weight_in_signal=0.25,
    )
    signals = aggregate_signals(deltas, min_delta_notional_usd=50000, min_single_whale_delta_usd=50000, min_wallet_count=1)
    assert signals
    s = signals[0]
    assert s["wallet_quality"]["high_quality_wallet_count"] == 1
    assert s["wallet_quality_score"] >= 50
    assert s["weighted_win_rate_72h"] == 0.7
