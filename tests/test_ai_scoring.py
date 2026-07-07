from wallet_ai_monitor.ai import _validate_ai_result, merge_ai
from wallet_ai_monitor.config import Settings
import wallet_ai_monitor.main as main


def test_ai_score_is_validated_and_merged():
    data = {
        "summary": "ok",
        "signals": [{
            "coin": "BTC",
            "direction": "OPEN_LONG",
            "action": "OPEN_LONG",
            "confidence": 80,
            "ai_score": 92,
            "ai_score_reason": "strong multi-window accumulation",
            "score_factors": {"wallet_resonance": 90},
        }],
    }
    ok, reason = _validate_ai_result(data)
    assert ok, reason

    signals = [{"coin": "BTC", "side": "LONG"}]
    merge_ai(signals, data)
    assert signals[0]["ai_score"] == 92
    assert signals[0]["score_factors"]["wallet_resonance"] == 90


class DummySettings:
    ai_scoring_enabled = True
    ai_score_weight = 0.6
    ai_rule_score_weight = 0.25
    ai_confidence_score_weight = 0.15


def test_ai_composite_score_is_ai_led():
    signals = [{
        "swing_score": 60,
        "ai_confidence": 80,
        "ai_score": 95,
    }]
    main._apply_ai_composite_scores(signals, DummySettings())
    assert signals[0]["score_source"] == "ai_led"
    # 95*0.6 + 60*0.25 + 80*0.15 = 84
    assert signals[0]["final_score"] == 84
