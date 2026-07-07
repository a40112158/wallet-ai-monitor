from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ADDR_RE = re.compile(r"0x[a-fA-F0-9]{40}")


@dataclass(frozen=True)
class Wallet:
    address: str
    group: str
    weight: float


def read_addresses(path: Path) -> list[str]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="ignore")
    return [m.group(0).lower() for m in ADDR_RE.finditer(text)]


def load_wallets(data_dir: Path, smart_weight: float = 1.0, money_weight: float = 1.35) -> list[Wallet]:
    sources = [
        ("smart_money", data_dir / "smart_money_all_addresses.txt", smart_weight),
        ("money_printer", data_dir / "money_printer_all_addresses.txt", money_weight),
    ]
    merged: dict[str, Wallet] = {}
    for group, path, weight in sources:
        for addr in read_addresses(path):
            # 重复地址优先使用权重更高的分组
            prev = merged.get(addr)
            if prev is None or weight > prev.weight:
                merged[addr] = Wallet(address=addr, group=group, weight=weight)
    return list(merged.values())


def shard_wallets(wallets: list[Wallet], max_per_run: int, offset: int) -> list[Wallet]:
    if max_per_run <= 0 or max_per_run >= len(wallets):
        return wallets
    start = offset % len(wallets)
    end = start + max_per_run
    if end <= len(wallets):
        return wallets[start:end]
    return wallets[start:] + wallets[: end - len(wallets)]
