"""Telegram 推送（头部带北京时间）。"""
from __future__ import annotations

import requests

from .config import Config
from .logging_utils import get_logger
from .timeutil import fmt_bj

log = get_logger()


def _fmt_usd(v):
    try:
        return f"${v:,.0f}"
    except (TypeError, ValueError):
        return "-"


def send_report(ctx: dict, cfg: Config) -> None:
    if not cfg.telegram_enabled or not cfg.telegram_bot_token \
            or not cfg.telegram_chat_id:
        return
    signals = [s for s in ctx["signals"]
               if (s.get("final_score") or 0) >= cfg.ai_min_final_score_for_open]
    if not signals and not ctx.get("close_warnings") and not ctx.get("closed_now"):
        return

    lines = [f"🐋 <b>巨鲸中长期信号</b>  {fmt_bj()}"]
    for s in sorted(signals, key=lambda x: x["final_score"], reverse=True)[:8]:
        lines.append(
            f"\n<b>{s['coin']} {s['direction']}</b>\n"
            f"swing={s.get('swing_score')} AI={s.get('ai_score')} "
            f"综合={s.get('final_score')} conf={s.get('ai_confidence')}\n"
            f"{s.get('state')}/第{s.get('round')}轮/冷却{s.get('cooldown_remaining_min')}分/"
            f"{s.get('amount_change_x')}x\n"
            f"wallets={s.get('wallet_count')} {_fmt_usd(s.get('delta_notional'))} "
            f"AI={s.get('ai_action')}")

    for t in ctx.get("closed_now", []):
        lines.append(f"\n✅ 平仓 {t['coin']} {t['side']} {t['close_reason']} "
                     f"pnl={t.get('pnl_pct')}%")

    for w in ctx.get("close_warnings", []):
        t = w["trade"]
        types = ",".join(x["type"] for x in w["warnings"])
        lines.append(f"\n⚠️ 准备平仓 {t['coin']} {t['side']} {types} "
                     f"pnl={t.get('pnl_pct')}%")

    text = "\n".join(lines)
    try:
        requests.post(
            f"https://api.telegram.org/bot{cfg.telegram_bot_token}/sendMessage",
            json={"chat_id": cfg.telegram_chat_id, "text": text,
                  "parse_mode": "HTML", "disable_web_page_preview": True},
            timeout=15)
    except Exception as e:  # noqa: BLE001
        log.warning("Telegram 推送失败: %s", e)
