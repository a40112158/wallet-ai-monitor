"""Hyperliquid 持仓扫描 (clearinghouseState)。"""
from __future__ import annotations

import time
from typing import Any

import requests

from .config import Config
from .logging_utils import get_logger

log = get_logger()


def _fetch_one(addr: str, cfg: Config) -> dict:
    r = requests.post(cfg.hl_api_url,
                      json={"type": "clearinghouseState", "user": addr},
                      timeout=cfg.hl_timeout)
    r.raise_for_status()
    data = r.json()
    positions: dict[str, dict] = {}
    for ap in data.get("assetPositions", []):
        p = ap.get("position", {})
        coin = p.get("coin")
        szi = float(p.get("szi", 0) or 0)
        if not coin or szi == 0:
            continue
        entry = float(p.get("entryPx", 0) or 0)
        notional = abs(float(p.get("positionValue", 0) or 0))
        if notional == 0 and entry:
            notional = abs(szi * entry)
        positions[coin] = {
            "szi": szi,
            "entry_px": entry,
            "notional": notional,
            "side": "LONG" if szi > 0 else "SHORT",
        }
    return positions


def scan_wallets(addrs: list[str], cfg: Config) -> tuple[dict[str, dict], dict[str, Any]]:
    """扫描钱包并返回持仓 + 扫描统计。

    重点：失败的钱包必须和“成功读取但空仓”的钱包区分开。
    否则 API 临时失败时会把旧持仓误覆盖为空仓，下一轮恢复后产生假信号。
    """
    out: dict[str, dict] = {}
    ok_wallets: list[str] = []
    failed_wallets: list[str] = []
    total = len(addrs)

    for idx, addr in enumerate(addrs, start=1):
        try:
            out[addr] = _fetch_one(addr, cfg)
            ok_wallets.append(addr)
        except Exception as e:  # noqa: BLE001
            log.debug("扫描 %s 失败: %s", addr, e)
            failed_wallets.append(addr)
        if idx % 100 == 0 or idx == total:
            log.info("扫描进度 %d/%d，成功 %d，失败 %d",
                     idx, total, len(ok_wallets), len(failed_wallets))
        time.sleep(cfg.hl_request_delay)

    stats: dict[str, Any] = {
        "total": total,
        "success": len(ok_wallets),
        "failed": len(failed_wallets),
        "success_rate": round(len(ok_wallets) / total, 4) if total else 0.0,
        "ok_wallets": ok_wallets,
        "failed_wallets_sample": failed_wallets[:20],
    }
    log.info("扫描完成 %d/%d 成功，失败 %d，成功率 %.2f%%",
             stats["success"], total, stats["failed"], stats["success_rate"] * 100)
    return out, stats
