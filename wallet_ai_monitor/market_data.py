"""市场数据 + 历史 K 线 (candleSnapshot)。"""
from __future__ import annotations

from typing import Any

import requests

from .config import Config
from .logging_utils import get_logger

log = get_logger()


def fetch_market_ctx(cfg: Config) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    try:
        r = requests.post(cfg.hl_api_url, json={"type": "metaAndAssetCtxs"},
                          timeout=cfg.hl_timeout)
        r.raise_for_status()
        meta, ctxs = r.json()
        universe = meta.get("universe", [])
        for i, ctx in enumerate(ctxs):
            if i >= len(universe):
                break
            coin = universe[i].get("name")
            if not coin:
                continue
            mark = float(ctx.get("markPx", 0) or 0)
            prev = float(ctx.get("prevDayPx", 0) or 0)
            out[coin] = {
                "mark": mark,
                "oi": float(ctx.get("openInterest", 0) or 0),
                "funding": float(ctx.get("funding", 0) or 0),
                "prev_day_px": prev,
                "change_24h_pct": ((mark - prev) / prev * 100) if prev else 0.0,
            }
    except Exception as e:  # noqa: BLE001
        log.warning("市场数据获取失败: %s", e)
    return out


def fetch_candles(coin: str, interval: str, start_ms: int, end_ms: int,
                  cfg: Config) -> list[dict]:
    try:
        r = requests.post(cfg.hl_api_url, json={
            "type": "candleSnapshot",
            "req": {"coin": coin, "interval": interval,
                    "startTime": start_ms, "endTime": end_ms},
        }, timeout=cfg.hl_timeout)
        r.raise_for_status()
        data = r.json()
        return data if isinstance(data, list) else []
    except Exception as e:  # noqa: BLE001
        log.debug("candle %s 获取失败: %s", coin, e)
        return []
