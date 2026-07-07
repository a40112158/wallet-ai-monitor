from wallet_ai_monitor.storage import Store


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


def test_virtual_trade_leverage_is_capped_at_10x(tmp_path):
    store = Store(tmp_path / "v.sqlite3")
    sig = _signal()
    sid = store.insert_signal(100, sig)
    tid = store.open_virtual_trade(
        sid,
        100,
        sig,
        1000.0,
        leverage=15,
        margin_usd=100.0,
        ai_open_reason="test",
    )
    assert tid
    row = store.virtual_open_rows()[0]
    assert row["leverage"] == 10
    assert row["margin_usd"] == 100.0

    rows = store.update_virtual_trades(
        200,
        {"BTC": 105.0},
        take_profit_pct=50,
        stop_loss_pct=50,
        max_hold_seconds=999999,
    )
    assert round(rows[0]["pnl_pct"], 2) == 5.0
    assert round(rows[0]["leveraged_roe_pct"], 2) == 50.0


def test_ai_close_decision_closes_virtual_trade(tmp_path):
    store = Store(tmp_path / "v.sqlite3")
    sig = _signal()
    sid = store.insert_signal(100, sig)
    tid = store.open_virtual_trade(sid, 100, sig, 1000.0, leverage=3, margin_usd=333.33)
    rows = store.update_virtual_trades(
        200,
        {"BTC": 101.0},
        take_profit_pct=50,
        stop_loss_pct=50,
        max_hold_seconds=999999,
        ai_exit_decisions={tid: {"action": "CLOSE", "confidence": 80, "reason": "wallet flow reversed"}},
        ai_close_min_confidence=65,
    )
    assert rows[0]["status"] == "CLOSED"
    assert rows[0]["reason"] == "AI_CLOSE"
    assert rows[0]["ai_exit_confidence"] == 80
