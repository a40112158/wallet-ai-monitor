"""虚拟账户：模拟开仓与盯市。"""
from __future__ import annotations

import time

from .config import Config
from .signal_lifecycle import should_suppress_open


def _ensure(acc: dict, cfg: Config) -> None:
    if not acc:
        acc.update({
            "capital": cfg.virtual_capital_usd,
            "initial_capital": cfg.virtual_capital_usd,
            "trades": [],
            "seq": 0,
        })
    acc.setdefault("trades", [])
    acc.setdefault("seq", 0)
    acc.setdefault("capital", cfg.virtual_capital_usd)
    acc.setdefault("initial_capital", cfg.virtual_capital_usd)


def _open_margin_used(acc: dict) -> float:
    return sum(t["margin"] for t in acc["trades"] if t["status"] == "OPEN")


def _has_open(acc: dict, coin: str, side: str) -> bool:
    return any(t["status"] == "OPEN" and t["coin"] == coin and t["side"] == side
               for t in acc["trades"])


def try_open_trades(signals: list[dict], market: dict, state: dict,
                    cfg: Config) -> list[dict]:
    acc = state["virtual_account"]
    _ensure(acc, cfg)
    now = time.time()
    opened: list[dict] = []
    cap = acc["capital"]
    max_total_margin = cap * cfg.ai_max_total_margin_pct / 100

    for s in signals:
        if s.get("ai_action") != "OPEN":
            continue
        if (s.get("final_score") or 0) < cfg.ai_min_final_score_for_open:
            continue
        if should_suppress_open(s):
            continue
        side = "LONG" if s["direction"] == "OPEN_LONG" else "SHORT"
        if _has_open(acc, s["coin"], side):
            continue
        mark = market.get(s["coin"], {}).get("mark", 0)
        if mark <= 0:
            continue

        margin = cap * min(cfg.ai_max_margin_pct, s.get("margin_pct", 5)) / 100
        if _open_margin_used(acc) + margin > max_total_margin:
            continue
        lev = max(1, min(int(cfg.ai_max_leverage), int(s.get("suggested_leverage", 3))))
        notional = margin * lev

        acc["seq"] += 1
        trade = {
            "id": acc["seq"],
            "coin": s["coin"],
            "side": side,
            "leverage": lev,
            "margin": round(margin, 2),
            "notional": round(notional, 2),
            "entry_px": mark,
            "current_px": mark,
            "opened_at": now,
            "status": "OPEN",
            "pnl_pct": 0.0,
            "roe_pct": 0.0,
            "take_profit_pct": s.get("take_profit_pct", 30),
            "stop_loss_pct": s.get("stop_loss_pct", 15),
            "max_hold_hours": s.get("max_hold_hours", 120),
            "final_score": s.get("final_score"),
            "swing_score": s.get("swing_score"),
            "ai_confidence": s.get("ai_confidence"),
            "open_reason": s.get("reason", ""),
            "pre_close_warnings": [],
        }
        acc["trades"].append(trade)
        opened.append(trade)
    return opened


def mark_to_market(acc: dict, market: dict) -> None:
    if not acc:
        return
    for t in acc.get("trades", []):
        if t["status"] != "OPEN":
            continue
        mk = market.get(t["coin"], {}).get("mark", 0)
        if mk <= 0 or t["entry_px"] <= 0:
            continue
        t["current_px"] = mk
        move = (mk - t["entry_px"]) / t["entry_px"]
        if t["side"] == "SHORT":
            move = -move
        t["pnl_pct"] = round(move * 100, 2)
        t["roe_pct"] = round(move * 100 * t["leverage"], 2)
