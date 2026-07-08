"""AI 对信号打分与开仓参数建议；不可用时回退到 swing 规则。"""
from __future__ import annotations

from .ai_client import AIClient
from .config import Config

_SYSTEM = (
    "你是加密永续合约中长期波段风控分析师。基于给定的巨鲸资金流信号与市场数据，"
    "评估该方向在数天到两周维度的胜率与风险。只输出严格 JSON，字段："
    "ai_score(0-100 整数), confidence(0-1), action(OPEN/WATCH/SKIP), "
    "reason(中文,一句话), score_reason(中文,打分依据), risks(中文字符串数组), "
    "invalidation(中文,失效条件), leverage(整数), margin_pct(数字,占本金百分比), "
    "take_profit_pct(数字,ROE止盈), stop_loss_pct(数字,ROE止损), "
    "max_hold_hours(整数)。风格保守，重视资金流持续性与是否追高。"
)


def _build_user(s: dict, market: dict, cfg: Config) -> dict:
    m = market.get(s["coin"], {})
    return {
        "coin": s["coin"],
        "direction": s["direction"],
        "swing_score": s.get("swing_score"),
        "swing_bucket": s.get("swing_bucket"),
        "flow_windows_usd": s.get("flow", {}),
        "delta_notional_usd": s["delta_notional"],
        "conflict_notional_usd": s.get("conflict_notional", 0),
        "wallet_count": s["wallet_count"],
        "avg_wallet_quality": s.get("avg_quality"),
        "change_24h_pct": round(m.get("change_24h_pct", 0), 2),
        "funding": m.get("funding", 0),
        "caps": {
            "max_leverage": cfg.ai_max_leverage,
            "max_margin_pct": cfg.ai_max_margin_pct,
        },
    }


def _fallback(s: dict, cfg: Config) -> None:
    swing = s.get("swing_score", 0)
    bucket = s.get("swing_bucket", "WEAK")
    action = "OPEN" if bucket in ("STRONG", "GOOD") else \
             "WATCH" if bucket == "WATCH" else "SKIP"
    s.update({
        "ai_score": round(swing, 2),
        "ai_confidence": round(min(1.0, swing / 100), 2),
        "ai_action": action,
        "final_score": round(swing, 2),
        "reason": "AI 不可用，使用规则回退评分",
        "ai_score_reason": f"swing={swing} bucket={bucket}",
        "risks": ["AI 未参与，仅规则判断"],
        "invalidation": "资金流反转或跌破关键位",
        "suggested_leverage": min(3, int(cfg.ai_max_leverage)),
        "margin_pct": min(5, cfg.ai_max_margin_pct),
        "take_profit_pct": 30,
        "stop_loss_pct": 15,
        "max_hold_hours": s.get("swing_horizon_days", 5) * 24,
    })


def _apply(s: dict, res: dict, cfg: Config) -> None:
    ai_score = float(res.get("ai_score", s.get("swing_score", 0)))
    ai_score = max(0.0, min(100.0, ai_score))
    swing = s.get("swing_score", 0)
    final = round(0.5 * swing + 0.5 * ai_score, 2)

    lev = int(res.get("leverage", 3) or 3)
    margin = float(res.get("margin_pct", 5) or 5)
    action = str(res.get("action", "WATCH")).upper()
    if action not in ("OPEN", "WATCH", "SKIP"):
        action = "WATCH"

    s.update({
        "ai_score": round(ai_score, 2),
        "ai_confidence": round(float(res.get("confidence", 0.5) or 0.5), 2),
        "ai_action": action,
        "final_score": final,
        "reason": res.get("reason", ""),
        "ai_score_reason": res.get("score_reason", ""),
        "risks": res.get("risks", []),
        "invalidation": res.get("invalidation", ""),
        "suggested_leverage": max(1, min(int(cfg.ai_max_leverage), lev)),
        "margin_pct": max(1.0, min(cfg.ai_max_margin_pct, margin)),
        "take_profit_pct": float(res.get("take_profit_pct", 30) or 30),
        "stop_loss_pct": float(res.get("stop_loss_pct", 15) or 15),
        "max_hold_hours": int(res.get("max_hold_hours",
                                      s.get("swing_horizon_days", 5) * 24) or 120),
        "_from_cache": res.get("_from_cache", False),
    })


def score_signals(signals: list[dict], market: dict, ai: AIClient,
                  cfg: Config) -> None:
    for s in signals:
        res = None
        if cfg.ai_enabled and cfg.ai_scoring_enabled:
            res = ai.chat_json(_SYSTEM, _build_user(s, market, cfg))
        if res:
            _apply(s, res, cfg)
        else:
            ai.stats["fallback_used"] = True
            _fallback(s, cfg)
