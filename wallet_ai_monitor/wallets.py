"""钱包清单加载与分片轮换选择。"""
from __future__ import annotations

import math
import os
import time

from .logging_utils import get_logger

log = get_logger()


def _norm(addr: str) -> str:
    return addr.strip().lower()


def load_wallets(wallet_dir: str) -> dict[str, list[str]]:
    meta: dict[str, list[str]] = {}
    if not os.path.isdir(wallet_dir):
        log.warning("钱包目录不存在: %s", wallet_dir)
        return meta
    for fn in sorted(os.listdir(wallet_dir)):
        if not fn.endswith((".txt", ".csv")):
            continue
        group = os.path.splitext(fn)[0]
        path = os.path.join(wallet_dir, fn)
        try:
            with open(path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    addr = _norm(line.split(",")[0])
                    if not addr.startswith("0x") or len(addr) < 10:
                        continue
                    meta.setdefault(addr, [])
                    if group not in meta[addr]:
                        meta[addr].append(group)
        except Exception as e:  # noqa: BLE001
            log.warning("读取 %s 失败: %s", path, e)
    log.info("加载钱包 %d 个", len(meta))
    return meta


def select_wallets(meta: dict[str, list[str]], max_per_run: int,
                   rotate: bool) -> list[str]:
    addrs = sorted(meta.keys())
    if len(addrs) <= max_per_run:
        return addrs
    if not rotate:
        return addrs[:max_per_run]
    shards = math.ceil(len(addrs) / max_per_run)
    idx = int(time.time() // 3600) % shards
    start = idx * max_per_run
    return addrs[start:start + max_per_run]
