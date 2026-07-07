from __future__ import annotations

import logging
import aiohttp

log = logging.getLogger(__name__)


async def send_telegram(bot_token: str, chat_id: str, text: str) -> bool:
    if not bot_token or not chat_id:
        return False
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text[:3900], "parse_mode": "HTML", "disable_web_page_preview": True}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, timeout=15) as resp:
                if resp.status >= 300:
                    log.warning("telegram send failed status=%s text=%s", resp.status, await resp.text())
                    return False
                return True
    except Exception as exc:  # noqa: BLE001
        log.warning("telegram send error: %s", exc)
        return False
