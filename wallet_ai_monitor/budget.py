from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class BudgetDecision:
    daily_target_points: int
    estimated_points_today: int
    remaining_today_points: int
    usage_ratio: float
    threshold_multiplier: float
    top_n: int
    max_output_tokens: int
    mode: str


def estimate_points(
    *,
    prompt_tokens: int | None,
    completion_tokens: int | None,
    input_cost_per_million_usd: float,
    output_cost_per_million_usd: float,
    points_per_usd: float,
) -> int:
    """Estimate Poe points from token usage.

    Poe may not expose exact cost_points in the OpenAI-compatible response, so this
    estimator is intentionally configurable. Defaults are conservative and can be
    tuned in GitHub Variables without code changes.
    """
    prompt = max(0, int(prompt_tokens or 0))
    completion = max(0, int(completion_tokens or 0))
    usd = (prompt / 1_000_000.0) * input_cost_per_million_usd + (completion / 1_000_000.0) * output_cost_per_million_usd
    return max(0, int(math.ceil(usd * points_per_usd)))


def decide_budget(
    *,
    enabled: bool,
    daily_target_points: int,
    estimated_points_today: int,
    base_min_delta: float,
    base_top_n: int,
    base_max_output_tokens: int,
    min_threshold_multiplier: float,
    max_threshold_multiplier: float,
    min_top_n: int,
    max_top_n: int,
) -> BudgetDecision:
    if not enabled or daily_target_points <= 0:
        return BudgetDecision(
            daily_target_points=max(0, int(daily_target_points)),
            estimated_points_today=max(0, int(estimated_points_today)),
            remaining_today_points=max(0, int(daily_target_points) - int(estimated_points_today)),
            usage_ratio=0.0,
            threshold_multiplier=1.0,
            top_n=max(1, int(base_top_n)),
            max_output_tokens=max(128, int(base_max_output_tokens)),
            mode="fixed",
        )

    ratio = max(0.0, estimated_points_today / max(float(daily_target_points), 1.0))
    # Spend too little -> lower threshold, analyze more, allow longer output.
    # Spend too much -> raise threshold, fewer candidates, shorter output.
    if ratio < 0.35:
        mult = 0.55
        top_n = base_top_n + 4
        token_mult = 1.25
        mode = "under_spending_expand"
    elif ratio < 0.70:
        mult = 0.75
        top_n = base_top_n + 2
        token_mult = 1.10
        mode = "under_spending"
    elif ratio <= 1.10:
        mult = 1.0
        top_n = base_top_n
        token_mult = 1.0
        mode = "on_track"
    elif ratio <= 1.50:
        mult = 1.35
        top_n = max(1, base_top_n - 2)
        token_mult = 0.85
        mode = "over_spending"
    else:
        mult = 1.85
        top_n = max(1, base_top_n - 4)
        token_mult = 0.70
        mode = "protect_budget"

    mult = max(float(min_threshold_multiplier), min(float(max_threshold_multiplier), mult))
    top_n = max(int(min_top_n), min(int(max_top_n), int(top_n)))
    max_tokens = max(128, int(round(base_max_output_tokens * token_mult)))
    return BudgetDecision(
        daily_target_points=int(daily_target_points),
        estimated_points_today=int(estimated_points_today),
        remaining_today_points=max(0, int(daily_target_points) - int(estimated_points_today)),
        usage_ratio=round(ratio, 4),
        threshold_multiplier=round(mult, 4),
        top_n=top_n,
        max_output_tokens=max_tokens,
        mode=mode,
    )


def usage_from_openai_response(resp: Any) -> dict[str, int]:
    usage = getattr(resp, "usage", None)
    if usage is None:
        return {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    def get(name: str) -> int:
        try:
            if isinstance(usage, dict):
                return int(usage.get(name) or 0)
            return int(getattr(usage, name, 0) or 0)
        except (TypeError, ValueError):
            return 0
    return {
        "prompt_tokens": get("prompt_tokens"),
        "completion_tokens": get("completion_tokens"),
        "total_tokens": get("total_tokens"),
    }
