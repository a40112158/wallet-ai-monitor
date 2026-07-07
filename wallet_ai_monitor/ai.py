from __future__ import annotations

import json
import logging
import time
from typing import Any

try:
    from openai import OpenAI
except ModuleNotFoundError:  # allow local tests before pip install
    OpenAI = None  # type: ignore

from .budget import usage_from_openai_response

log = logging.getLogger(__name__)

ALLOWED_ACTIONS = {"OPEN_LONG", "OPEN_SHORT", "WATCH", "AVOID"}


class PoeAI:
    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str,
        max_tokens: int = 900,
        temperature: float = 0.15,
        timeout_seconds: int = 60,
    ):
        self.enabled = bool(api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout_seconds,
            max_retries=1,
        ) if api_key and OpenAI is not None else None

    def analyze_signals(self, signals: list[dict[str, Any]]) -> dict[str, Any]:
        if not self.enabled or not self.client or not signals:
            return {"ok": False, "reason": "AI disabled or no signals", "signals": []}
        payload = _compact_for_ai(signals)
        system = (
            "你是加密合约中长期交易信号分析器。目标不是短线追单，而是通过聪明钱钱包行为筛选3-14天甚至更长周期的合约开单候选。"
            "你只做信号过滤、风险提示和模拟交易建议，不执行交易。必须输出严格 JSON，不要 Markdown。根字段：summary, signals。"
            "每个 signal 字段必须包含：coin, direction, confidence, action, reason, risks, invalidation, "
            "suggested_leverage, entry_zone, hold_period_days, take_profit_notes, stop_loss_notes。"
            "confidence 和 ai_score 必须是 0-100 数字；action 只能是 OPEN_LONG/OPEN_SHORT/WATCH/AVOID。ai_score 是你对该信号作为3-14天合约机会的独立评分，不等同于规则 swing_score。"
            "中长期原则：优先选择多窗口持续建仓、多个钱包同方向共振、money_printer 参与、历史胜率/盈亏比更好的高质量钱包参与、价格还没极端拉升/砸盘、funding 不拥挤、多空冲突低的币。"
            "如果只是单轮小额开仓、价格已经过度延伸、funding 极端拥挤、反向钱包强冲突，ai_score 应明显降低并且应该 WATCH 或 AVOID。"
            "需要给出入场区间，而不是让用户追市价；失效条件必须具体。"
        )
        user = "请分析以下 Hyperliquid 钱包中长期合约候选信号，筛选真正值得开多/开空或继续观察的币：\n" + json.dumps(payload, ensure_ascii=False)
        for attempt in range(2):
            try:
                resp = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                )
                content = resp.choices[0].message.content or "{}"
                usage = usage_from_openai_response(resp)
                parsed = _parse_json_response(content)
                ok, reason = _validate_ai_result(parsed)
                if ok:
                    parsed["ok"] = True
                    parsed["model"] = self.model
                    parsed["usage"] = usage
                    return parsed
                if attempt == 0:
                    user += f"\n\n上一次输出不合格：{reason}。请只返回合格 JSON。"
                    continue
                parsed.setdefault("ok", False)
                parsed.setdefault("reason", reason)
                return parsed
            except Exception as exc:  # noqa: BLE001
                if attempt == 0:
                    log.warning("AI signal analysis failed; retrying: %s", exc)
                    time.sleep(1.0)
                    continue
                log.exception("AI signal analysis failed after retry")
                return {"ok": False, "reason": str(exc), "signals": []}
        return {"ok": False, "reason": "AI validation failed", "signals": []}


    def manage_virtual_trades(self, open_trades: list[dict[str, Any]], market_context: dict[str, Any]) -> dict[str, Any]:
        """Ask AI whether existing virtual trades should stay open or be closed.

        This is for paper trading only. Hard stop-loss/take-profit/max-hold rules still
        remain outside the model as safety rails.
        """
        if not self.enabled or not self.client or not open_trades:
            return {"ok": False, "reason": "AI disabled or no open virtual trades", "decisions": []}

        payload = {
            "open_trades": open_trades[:20],
            "market_context": market_context,
        }
        system = (
            "你是加密合约中长期虚拟账户的风控/平仓决策器。你只管理纸面模拟账户，不执行真实交易。"
            "目标是在3-14天周期内决定现有虚拟仓位 HOLD 还是 CLOSE。必须输出严格 JSON，不要 Markdown。"
            "根字段：summary, decisions。每个 decision 必须包含：id, coin, action, confidence, reason。"
            "action 只能是 HOLD 或 CLOSE；confidence 必须是0-100数字。"
            "当出现反向钱包强共振、ACTIVE_SIGNAL_DECAY、价格到达失效区、资金流明显反向、AI原始逻辑失效、"
            "或者风险收益已经明显变差时，才 CLOSE。普通浮亏不一定平，普通浮盈也不一定平。"
            "禁止建议加仓真实交易。"
        )
        user = "请判断以下虚拟仓位是否继续持有或平仓：\n" + json.dumps(payload, ensure_ascii=False)
        for attempt in range(2):
            try:
                resp = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                )
                content = resp.choices[0].message.content or "{}"
                usage = usage_from_openai_response(resp)
                parsed = _parse_json_response(content)
                ok, reason = _validate_trade_decisions(parsed)
                if ok:
                    parsed["ok"] = True
                    parsed["model"] = self.model
                    parsed["usage"] = usage
                    return parsed
                if attempt == 0:
                    user += f"\n\n上一次输出不合格：{reason}。请只返回合格 JSON。"
                    continue
                parsed.setdefault("ok", False)
                parsed.setdefault("reason", reason)
                return parsed
            except Exception as exc:  # noqa: BLE001
                if attempt == 0:
                    log.warning("AI virtual trade management failed; retrying: %s", exc)
                    time.sleep(1.0)
                    continue
                log.exception("AI virtual trade management failed after retry")
                return {"ok": False, "reason": str(exc), "decisions": []}
        return {"ok": False, "reason": "AI trade decision validation failed", "decisions": []}



def _compact_for_ai(signals: list[dict[str, Any]]) -> list[dict[str, Any]]:
    compact = []
    for s in signals:
        compact.append({
            "coin": s.get("coin"),
            "direction": s.get("direction"),
            "wallet_count": s.get("wallet_count"),
            "groups": s.get("groups"),
            "events": s.get("events"),
            "total_delta_notional": s.get("total_delta_notional"),
            "max_wallet_delta_notional": s.get("max_wallet_delta_notional"),
            "total_position_value": s.get("total_position_value"),
            "weighted_score": s.get("weighted_score"),
            "net_bias_score": s.get("net_bias_score"),
            "conflict_level": s.get("conflict_level"),
            "conflict_ratio": s.get("conflict_ratio"),
            "opposite_delta_notional": s.get("opposite_delta_notional"),
            "risk_tags": s.get("risk_tags"),
            "swing_score": s.get("swing_score"),
            "swing_bucket": s.get("swing_bucket"),
            "swing_horizon_days": s.get("swing_horizon_days"),
            "swing": s.get("swing"),
            "wallet_quality": s.get("wallet_quality"),
            "avg_entry_px": s.get("avg_entry_px"),
            "mark_px": s.get("mark_px"),
            "market": s.get("market"),
            "top_wallets": [
                {
                    "wallet": _mask(w.get("wallet") or ""),
                    "group": w.get("group"),
                    "event": w.get("event"),
                    "delta_notional": round(float(w.get("delta_notional") or 0), 2),
                    "wallet_score": round(float(w.get("wallet_score") or 1), 3),
                    "quality_grade": w.get("quality_grade"),
                    "perf_trades": w.get("perf_trades"),
                    "win_rate_72h": w.get("win_rate_72h"),
                    "avg_pnl_72h": w.get("avg_pnl_72h"),
                    "win_rate_168h": w.get("win_rate_168h"),
                    "avg_pnl_168h": w.get("avg_pnl_168h"),
                    "entry_px": w.get("entry_px"),
                    "leverage": w.get("leverage"),
                    "roe": w.get("roe"),
                }
                for w in s.get("wallets", [])[:5]
            ],
        })
    return compact


def _mask(addr: str) -> str:
    if len(addr) < 16:
        return addr
    return addr[:10] + "..." + addr[-6:]


def _parse_json_response(content: str) -> dict[str, Any]:
    s = content.strip()
    if s.startswith("```"):
        s = s.strip("`")
        if s.lower().startswith("json"):
            s = s[4:].strip()
    first = s.find("{")
    last = s.rfind("}")
    if first != -1 and last != -1 and last > first:
        s = s[first:last + 1]
    try:
        data = json.loads(s)
        if isinstance(data, dict):
            return data
    except json.JSONDecodeError:
        pass
    return {"ok": False, "reason": "AI returned non-json", "raw": content, "signals": []}


def _bounded_float(value: Any, default: float, low: float, high: float) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        number = default
    return max(low, min(high, number))


def _validate_ai_result(data: dict[str, Any]) -> tuple[bool, str]:
    if not isinstance(data, dict):
        return False, "root is not object"
    signals = data.get("signals")
    if not isinstance(signals, list):
        return False, "signals is not list"
    for idx, item in enumerate(signals):
        if not isinstance(item, dict):
            return False, f"signals[{idx}] is not object"
        action = str(item.get("action", "")).upper()
        if action not in ALLOWED_ACTIONS:
            return False, f"signals[{idx}].action invalid: {action}"
        try:
            conf = float(item.get("confidence"))
        except (TypeError, ValueError):
            return False, f"signals[{idx}].confidence invalid"
        if not 0 <= conf <= 100:
            return False, f"signals[{idx}].confidence out of range"
        if not item.get("coin"):
            return False, f"signals[{idx}].coin missing"
        direction = str(item.get("direction", "")).upper()
        if direction in {"LONG", "BUY"}:
            direction = "OPEN_LONG"
        elif direction in {"SHORT", "SELL"}:
            direction = "OPEN_SHORT"
        if direction not in {"OPEN_LONG", "OPEN_SHORT"}:
            if action in {"OPEN_LONG", "OPEN_SHORT"}:
                direction = action
            else:
                return False, f"signals[{idx}].direction invalid: {direction}"
        item["direction"] = direction
        item["action"] = action
        item["confidence"] = conf
        item["ai_score"] = _bounded_float(item.get("ai_score"), conf, 0.0, 100.0)
        item.setdefault("ai_score_reason", item.get("reason", ""))
        factors = item.get("score_factors")
        item["score_factors"] = factors if isinstance(factors, dict) else {}
        item["suggested_leverage"] = _bounded_float(item.get("suggested_leverage"), 1.0, 1.0, 10.0)
        item["margin_pct"] = _bounded_float(item.get("margin_pct"), 0.0, 0.0, 15.0)
        item["take_profit_pct"] = _bounded_float(item.get("take_profit_pct"), 0.0, 0.0, 50.0)
        item["stop_loss_pct"] = _bounded_float(item.get("stop_loss_pct"), 0.0, 0.0, 30.0)
        item["max_hold_hours"] = _bounded_float(item.get("max_hold_hours"), 0.0, 0.0, 720.0)
        item.setdefault("entry_zone", "")
        item.setdefault("hold_period_days", "")
        item.setdefault("position_reason", item.get("reason", ""))
    return True, "ok"



def _validate_trade_decisions(data: dict[str, Any]) -> tuple[bool, str]:
    if not isinstance(data, dict):
        return False, "root is not object"
    decisions = data.get("decisions")
    if not isinstance(decisions, list):
        return False, "decisions is not list"
    for idx, item in enumerate(decisions):
        if not isinstance(item, dict):
            return False, f"decisions[{idx}] is not object"
        try:
            item["id"] = int(item.get("id"))
        except (TypeError, ValueError):
            return False, f"decisions[{idx}].id invalid"
        action = str(item.get("action", "")).upper()
        if action not in {"HOLD", "CLOSE"}:
            return False, f"decisions[{idx}].action invalid: {action}"
        try:
            conf = float(item.get("confidence"))
        except (TypeError, ValueError):
            return False, f"decisions[{idx}].confidence invalid"
        if not 0 <= conf <= 100:
            return False, f"decisions[{idx}].confidence out of range"
        item["action"] = action
        item["confidence"] = conf
        item.setdefault("reason", "")
        item.setdefault("coin", "")
    return True, "ok"

def merge_ai(signals: list[dict[str, Any]], ai_result: dict[str, Any]) -> None:
    ai_by_coin_dir: dict[tuple[str, str], dict[str, Any]] = {}
    for item in ai_result.get("signals", []) or []:
        if not isinstance(item, dict):
            continue
        coin = str(item.get("coin", "")).upper()
        direction = str(item.get("direction") or "")
        action = str(item.get("action") or "")
        side_hint = direction if direction else action
        side = "LONG" if "LONG" in side_hint.upper() else "SHORT" if "SHORT" in side_hint.upper() else None
        if coin and side:
            ai_by_coin_dir[(coin, side)] = item
    for s in signals:
        item = ai_by_coin_dir.get((str(s["coin"]).upper(), s["side"]))
        if item:
            s["ai"] = item
            try:
                s["ai_confidence"] = float(item.get("confidence"))
            except (TypeError, ValueError):
                s["ai_confidence"] = None
            try:
                s["ai_score"] = float(item.get("ai_score"))
            except (TypeError, ValueError):
                s["ai_score"] = None
            s["ai_score_reason"] = item.get("ai_score_reason") or item.get("reason")
            s["score_factors"] = item.get("score_factors") if isinstance(item.get("score_factors"), dict) else {}
        else:
            s.setdefault("ai", {})
            s.setdefault("ai_confidence", None)
            s.setdefault("ai_score", None)
            s.setdefault("ai_score_reason", None)
            s.setdefault("score_factors", {})
