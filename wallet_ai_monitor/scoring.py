"""中长期 swing 评分。"""
from __future__ import annotations

from .config import Config


def _bucket(score: float) -> str:
    if score >= 80:
        return "STRONG"
    if score >= 65:
        return "GOOD"
    if score >= 50:
        return "WATCH"
    return "WEAK"


def _horizon_days(score: float) -> int:
    if score >= 80:
        return 14
    if score >= 70:
        return 10
    if score >= 60:
        return 7
    return 3


def compute_swing_score(signal: dict, market: dict, lifecycle: dict,
                        flow_windows: dict, cfg: Config) -> dict:
    coin = signal["coin"]
    parts: dict[str, float] = {}
    base = max(cfg.min_delta_notional_usd, 1)

    dn = signal["delta_notional"]
    parts["flow_size"] = min(26.0, dn / base * 10.0)
    parts["resonance"] = min(18.0, signal["wallet_count"] * 3.5)

    conc = signal["max_single_notional"] / dn if dn else 0
    parts["concentration"] = 8.0 * (1 - conc)

    conflict = signal.get("conflict_notional", 0)
    parts["conflict_penalty"] = -min(15.0, conflict / max(dn, 1) * 15.0)
    parts["wallet_quality"] = signal.get("avg_quality", 0.5) * 14.0

    round_n = (lifecycle or {}).get("round", 1)
    parts["persistence"] = min(12.0, (round_n - 1) * 4.0)

    f2 = flow_windows.get("2h", 0)
    f168 = flow_windows.get("168h", 0)
    parts["sustained_flow"] = min(14.0, f168 / base * 3.0)
    if f168 > 0:
        spike_ratio = f2 / f168
        parts["spike_penalty"] = -min(8.0, max(0.0, spike_ratio - 0.7) * 20.0)
    else:
        parts["spike_penalty"] = 0.0

    ch = market.get(coin, {}).get("change_24h_pct", 0)
    overext = ch if "LONG" in signal["direction"] else -ch
    parts["overextension_penalty"] = -min(12.0, max(0.0, overext - 8) * 1.2)

    raw = sum(parts.values())
    score = max(0.0, min(100.0, raw))

    return {
        "swing_score": round(score, 2),
        "swing_bucket": _bucket(score),
        "swing_horizon_days": _horizon_days(score),
        "score_parts": {k: round(v, 2) for k, v in parts.items()},
        "flow": flow_windows,
    }
