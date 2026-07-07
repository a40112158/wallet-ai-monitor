from wallet_ai_monitor.report import telegram_text


def test_telegram_text_with_signals_does_not_crash():
    signals = [{
        "coin": "BTC",
        "direction": "OPEN_LONG",
        "side": "LONG",
        "wallet_count": 3,
        "total_delta_notional": 250000,
        "max_wallet_delta_notional": 120000,
        "mark_px": 100000,
        "swing_score": 82,
        "swing": {"score": 82, "horizon_days": "3-14"},
        "ai_confidence": 75,
        "ai": {"action": "OPEN_LONG", "reason": "multi-window accumulation"},
    }]
    text = telegram_text(signals, {"summary": "ok"})
    assert "Wallet Swing Contract Monitor" in text
    assert "BTC" in text
    assert "OPEN_LONG" in text


def test_telegram_text_without_signals_with_exits():
    text = telegram_text([], {"summary": "none"}, exit_events=[{
        "coin": "ETH",
        "direction": "EXIT_LONG",
        "total_delta_notional": 100000,
    }])
    assert "无达标开仓信号" in text
    assert "ETH" in text
