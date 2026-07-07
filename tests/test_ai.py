from wallet_ai_monitor.ai import _validate_ai_result, merge_ai


def test_watch_result_is_merged_by_direction():
    signals = [{"coin": "BTC", "side": "LONG"}]
    result = {
        "signals": [{
            "coin": "btc",
            "direction": "OPEN_LONG",
            "action": "WATCH",
            "confidence": 80,
        }]
    }
    assert _validate_ai_result(result) == (True, "ok")
    merge_ai(signals, result)
    assert signals[0]["ai"]["action"] == "WATCH"
    assert signals[0]["ai_confidence"] == 80


def test_watch_without_direction_is_rejected():
    result = {"signals": [{"coin": "BTC", "action": "WATCH", "confidence": 80}]}
    ok, reason = _validate_ai_result(result)
    assert ok is False
    assert "direction" in reason


def test_ai_direction_long_short_aliases_are_normalized():
    result = {
        "signals": [
            {"coin": "ETH", "direction": "LONG", "action": "WATCH", "confidence": 72},
            {"coin": "SOL", "direction": "SHORT", "action": "AVOID", "confidence": 55},
        ]
    }
    assert _validate_ai_result(result) == (True, "ok")
    assert result["signals"][0]["direction"] == "OPEN_LONG"
    assert result["signals"][1]["direction"] == "OPEN_SHORT"
