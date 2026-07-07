from wallet_ai_monitor.storage import Store
from wallet_ai_monitor.report import render_markdown, telegram_text


def _signal(amount=1000):
    return {
        "coin": "BTC",
        "side": "LONG",
        "direction": "OPEN_LONG",
        "wallet_count": 2,
        "total_delta_notional": amount,
        "total_position_value": amount,
        "max_wallet_delta_notional": amount,
        "weighted_score": 1,
        "mark_px": 100.0,
        "avg_entry_px": 100.0,
        "ai_confidence": 80,
        "wallets": [],
    }


def test_signal_state_counts_suppressed_rounds(tmp_path):
    store = Store(tmp_path / "state.sqlite3")
    s1 = _signal(1000)
    state1 = store.update_signal_state(100, [s1], [s1], [], cooldown_seconds=3600)
    assert s1["signal_status"] == "NEW_SIGNAL"
    assert s1["signal_seen_runs"] == 1

    s2 = _signal(1100)
    lifecycle = [{
        "event": "COOLDOWN_MERGED",
        "coin": "BTC",
        "side": "LONG",
        "previous_signal_id": 1,
        "amount": 1100,
    }]
    store.update_signal_state(200, [s2], [], lifecycle, cooldown_seconds=3600)
    assert s2["signal_status"] == "COOLDOWN_REPEAT"
    assert s2["signal_seen_runs"] == 2
    assert lifecycle[0]["seen_runs"] == 2
    assert lifecycle[0]["cooldown_remaining_minutes"] > 0


def test_report_and_tg_show_signal_state():
    sig = _signal(1000)
    sig["signal_state"] = {
        "status": "RE_ALERT",
        "seen_runs": 4,
        "age_minutes": 90,
        "cooldown_remaining_minutes": 360,
        "amount_change_ratio": 2.4,
    }
    sig["swing_score"] = 88
    sig["swing"] = {"score": 88, "horizon_days": "3-14"}
    sig["swing_bucket"] = "STRONG_CANDIDATE"
    sig["ai"] = {"action": "OPEN_LONG"}
    sig["ai_score"] = 86
    sig["final_score"] = 87
    text = render_markdown(100, [sig], [], {"summary": "ok"})
    assert "信号状态" in text
    assert "第4轮" in text
    tg = telegram_text([sig], {"summary": "ok"})
    assert "第4轮" in tg
