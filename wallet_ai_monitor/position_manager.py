"""持仓管理：TP/SL/持仓时限触发平仓，接近阈值发准备平仓提示，AI 复核。"""
from __future__ import annotations

import time

from .ai_client import AIClient
from .config import Config

_CLOSE_SYSTEM = (
    "你是加密永续合约风控助手。给定一笔持仓的实时盈亏与触发原因，"
    "判断是否应立即平仓。只输出严格 JSON：action(CLOSE/HOLD), "
    "confidence(0-1), reason(中文一句话)。"
)


def _ai_close_opinion(t: dict, reason: str, ai: AIClient, cfg: Config) -> dict:
    if not (cfg.ai_enabled and cfg.ai_scoring_enabled):
        return {"action": "CLOSE", "confidence": 1.0, "reason": f"规则触发:{reason}"}
    res = ai.chat_json(_CLOSE_SYSTEM, {
        "coin": t["coin"], "side": t["side"], "leverage": t["leverage"],
        "roe_pct": t["roe_pct"], "pnl_pct": t["pnl_pct"],
        "trigger": reason,
        "take_profit_pct": t["take_profit_pct"],
        "stop_loss_pct": t["stop_loss_pct"],
    })
    if not res:
        return {"action": "CLOSE", "confidence": 1.0, "reason": f"规则触发:{reason}"}
    return res


def _close(acc: dict, t: dict, reason: str, ai_op: dict, now: float) -> None:
    t["status"] = "CLOSED"
    t["close_reason"] = reason
    t["closed_at"] = now
    t["close_ai_confidence"] = ai_op.get("confidence")
    t["close_ai_reason"] = ai_op.get("reason", "")
    pnl_usd = t["margin"] * t["roe_pct"] / 100
    t["realized_pnl_usd"] = round(pnl_usd, 2)
    acc["capital"] = round(acc.get("capital", 0) + pnl_usd, 2)


def manage_positions(acc: dict, market: dict, signals: list[dict],
                     ai: AIClient, cfg: Config) -> tuple[list[dict], list[dict]]:
    if not acc:
        return [], []
    now = time.time()
    closed_now: list[dict] = []
    warnings: list[dict] = []

    for t in acc.get("trades", []):
        if t["status"] != "OPEN":
            continue
        roe = t.get("roe_pct", 0)
        tp = t["take_profit_pct"]
        sl = t["stop_loss_pct"]
        hold_h = (now - t["opened_at"]) / 3600

        reason = None
        if roe >= tp:
            reason = "TAKE_PROFIT"
        elif roe <= -sl:
            reason = "STOP_LOSS"
        elif hold_h >= t["max_hold_hours"]:
            reason = "MAX_HOLD"

        if reason:
            ai_op = _ai_close_opinion(t, reason, ai, cfg)
            if reason in ("STOP_LOSS", "MAX_HOLD") or \
               str(ai_op.get("action", "CLOSE")).upper() == "CLOSE":
                _close(acc, t, reason, ai_op, now)
                closed_now.append(t)
            else:
                t["pre_close_warnings"] = [{
                    "type": f"AI_HOLD_ON_{reason}",
                    "reason": ai_op.get("reason", "")}]
                warnings.append({"trade": t, "warnings": t["pre_close_warnings"]})
            continue

        warns = []
        if roe >= tp * 0.8:
            warns.append({"type": "NEAR_TP",
                          "reason": f"ROE {roe}% 接近止盈 {tp}%"})
        if roe <= -sl * 0.8:
            warns.append({"type": "NEAR_SL",
                          "reason": f"ROE {roe}% 接近止损 -{sl}%"})
        if hold_h >= t["max_hold_hours"] * 0.8:
            warns.append({"type": "NEAR_MAX_HOLD",
                          "reason": f"已持仓 {hold_h:.1f}h / 上限 {t['max_hold_hours']}h"})
        t["pre_close_warnings"] = warns
        if warns:
            warnings.append({"trade": t, "warnings": warns})

    return closed_now, warnings
