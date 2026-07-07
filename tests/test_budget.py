from wallet_ai_monitor.budget import decide_budget, estimate_points


def test_budget_expands_when_under_spending():
    d = decide_budget(
        enabled=True,
        daily_target_points=1000,
        estimated_points_today=100,
        base_min_delta=100000,
        base_top_n=8,
        base_max_output_tokens=900,
        min_threshold_multiplier=0.45,
        max_threshold_multiplier=2.5,
        min_top_n=3,
        max_top_n=14,
    )
    assert d.threshold_multiplier < 1
    assert d.top_n > 8
    assert d.max_output_tokens > 900


def test_budget_protects_when_over_spending():
    d = decide_budget(
        enabled=True,
        daily_target_points=1000,
        estimated_points_today=2000,
        base_min_delta=100000,
        base_top_n=8,
        base_max_output_tokens=900,
        min_threshold_multiplier=0.45,
        max_threshold_multiplier=2.5,
        min_top_n=3,
        max_top_n=14,
    )
    assert d.threshold_multiplier > 1
    assert d.top_n < 8
    assert d.max_output_tokens < 900


def test_estimate_points_is_configurable():
    points = estimate_points(
        prompt_tokens=1000,
        completion_tokens=500,
        input_cost_per_million_usd=1.0,
        output_cost_per_million_usd=2.0,
        points_per_usd=1000,
    )
    assert points == 2
