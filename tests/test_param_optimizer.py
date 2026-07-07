from tools.ai_param_optimizer import validate_overrides, fallback_suggestions


def test_param_optimizer_rejects_secrets_and_out_of_bounds():
    result = validate_overrides({
        "POE_API_KEY": "bad",
        "MIN_DELTA_NOTIONAL_USD": 999999999,
        "SWING_MIN_SCORE_FOR_AI": 63,
    })
    assert result.overrides["SWING_MIN_SCORE_FOR_AI"] == "63"
    assert "POE_API_KEY" in result.rejected
    assert "MIN_DELTA_NOTIONAL_USD" in result.rejected


def test_param_optimizer_cross_constraints():
    result = validate_overrides({
        "SWING_MIN_SCORE_FOR_AI": 70,
        "SWING_WATCH_SCORE": 60,
        "SWING_STRONG_SCORE": 80,
    })
    assert "SWING_MIN_SCORE_FOR_AI" in result.overrides
    assert "SWING_WATCH_SCORE" in result.rejected


def test_fallback_suggestions_make_filters_stricter_when_signal_count_high():
    metrics = {
        "current_params": {
            "MIN_DELTA_NOTIONAL_USD": "100000",
            "SWING_MIN_SCORE_FOR_AI": "60",
            "SIGNAL_COOLDOWN_MINUTES": "360",
            "VIRTUAL_MIN_AI_CONFIDENCE": "70",
            "SWING_STRONG_SCORE": "80",
            "VIRTUAL_STOP_LOSS_PCT": "3",
            "MARKET_MAX_CANDLE_COINS": "12",
            "HL_CONCURRENCY": "16",
        },
        "state": {"health_24h": {"signals_count": 99, "avg_duration_sec": 0}, "virtual_summary": {}},
    }
    suggestions = fallback_suggestions(metrics)
    assert suggestions["MIN_DELTA_NOTIONAL_USD"] > 100000
    assert suggestions["SWING_MIN_SCORE_FOR_AI"] > 60


def test_write_override_file_preserves_existing_when_no_valid_overrides(monkeypatch, tmp_path):
    import tools.ai_param_optimizer as opt

    override_path = tmp_path / "ai_param_overrides.env"
    override_path.write_text("MIN_DELTA_NOTIONAL_USD=120000\n", encoding="utf-8")
    monkeypatch.setattr(opt, "OVERRIDE_PATH", override_path)
    monkeypatch.setattr(opt, "ROOT", tmp_path)

    opt.write_override_file({}, {"current_params": {}}, {"ok": False, "reason": "no change"}, {})
    assert override_path.read_text(encoding="utf-8") == "MIN_DELTA_NOTIONAL_USD=120000\n"
    assert not (tmp_path / "reports" / "param_optimizer_report.md").exists()
    assert (tmp_path / "reports" / "param_optimizer_latest.json").exists()
