"""白名单参数优化：基于近期虚拟交易表现微调，永不突破硬风控。"""
from __future__ import annotations

import json
import os

from .config import (Config, HARD_MAX_LEVERAGE,
                     HARD_MAX_MARGIN_PCT_PER_TRADE, HARD_MAX_TOTAL_MARGIN_PCT)
from .timeutil import fmt_bj

WHITELIST_BOUNDS = {
    "min_delta_notional_usd": (50000, 5000000),
    "min_single_whale_delta_usd": (20000, 2000000),
    "min_wallet_count": (1, 10),
    "top_signals_for_ai": (3, 20),
    "signal_cooldown_minutes": (60, 1440),
    "ai_min_final_score_for_open": (50, 90),
    "ai_max_leverage": (1, HARD_MAX_LEVERAGE),
    "ai_max_margin_pct": (1, HARD_MAX_MARGIN_PCT_PER_TRADE),
    "ai_max_total_margin_pct": (5, HARD_MAX_TOTAL_MARGIN_PCT),
}

_ENV_MAP = {
    "min_delta_notional_usd": "MIN_DELTA_NOTIONAL_USD",
    "min_single_whale_delta_usd": "MIN_SINGLE_WHALE_DELTA_USD",
    "min_wallet_count": "MIN_WALLET_COUNT",
    "top_signals_for_ai": "TOP_SIGNALS_FOR_AI",
    "signal_cooldown_minutes": "SIGNAL_COOLDOWN_MINUTES",
    "ai_min_final_score_for_open": "AI_MIN_FINAL_SCORE_FOR_OPEN",
    "ai_max_leverage": "AI_MAX_LEVERAGE",
    "ai_max_margin_pct": "AI_MAX_MARGIN_PCT_PER_TRADE",
    "ai_max_total_margin_pct": "AI_MAX_TOTAL_MARGIN_PCT",
}


def run_optimizer(state: dict, cfg: Config) -> dict:
    acc = state.get("virtual_account", {})
    closed = [t for t in acc.get("trades", []) if t["status"] == "CLOSED"]
    recent = closed[-30:]

    suggestions: dict[str, float] = {}
    rationale = []
    if len(recent) >= 8:
        wins = sum(1 for t in recent if t.get("realized_pnl_usd", 0) > 0)
        win_rate = wins / len(recent)
        if win_rate < 0.4:
            suggestions["ai_min_final_score_for_open"] = min(
                90, cfg.ai_min_final_score_for_open + 5)
            suggestions["min_wallet_count"] = min(10, cfg.min_wallet_count + 1)
            rationale.append(f"近{len(recent)}笔胜率{win_rate:.0%}偏低，收紧开仓门槛")
        elif win_rate > 0.6:
            suggestions["ai_min_final_score_for_open"] = max(
                50, cfg.ai_min_final_score_for_open - 3)
            rationale.append(f"近{len(recent)}笔胜率{win_rate:.0%}良好，适度放宽")

    clamped = {}
    for k, v in suggestions.items():
        lo, hi = WHITELIST_BOUNDS[k]
        clamped[k] = max(lo, min(hi, v))

    result = {
        "generated_bj": fmt_bj(),
        "samples": len(recent),
        "suggestions": clamped,
        "rationale": rationale,
        "hard_limits": {"AI_MAX_LEVERAGE": HARD_MAX_LEVERAGE},
    }

    os.makedirs("reports", exist_ok=True)
    with open("reports/param_optimizer_latest.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    if clamped:
        os.makedirs("config", exist_ok=True)
        with open("config/ai_param_overrides.env", "w", encoding="utf-8") as f:
            for k, v in clamped.items():
                f.write(f"{_ENV_MAP[k]}={v}\n")
    return result


def load_overrides() -> dict:
    path = "config/ai_param_overrides.env"
    out: dict = {}
    if not os.path.exists(path):
        return out
    rev = {v: k for k, v in _ENV_MAP.items()}
    with open(path, encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                if k in rev:
                    try:
                        out[rev[k]] = float(v)
                    except ValueError:
                        pass
    return out
