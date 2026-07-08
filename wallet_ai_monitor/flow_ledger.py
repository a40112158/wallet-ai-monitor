"""资金流时间序列账本：真实 2h/6h/24h/72h/168h 窗口聚合。"""
from __future__ import annotations

import time

WINDOWS_SEC = {"2h": 7200, "6h": 21600, "24h": 86400,
               "72h": 259200, "168h": 604800}
_MAX_AGE = WINDOWS_SEC["168h"]


def record(raw_signals: list[dict], ledger: dict, now: float | None = None) -> None:
    now = now or time.time()
    for s in raw_signals:
        key = f"{s['coin']}:{s['direction']}"
        ledger.setdefault(key, []).append([round(now, 0),
                                           round(s["delta_notional"], 2)])
    prune(ledger, now)


def prune(ledger: dict, now: float) -> None:
    cutoff = now - _MAX_AGE
    for key in list(ledger.keys()):
        ledger[key] = [e for e in ledger[key] if e[0] >= cutoff]
        if not ledger[key]:
            del ledger[key]


def windows_for(coin: str, direction: str, ledger: dict,
                now: float | None = None) -> dict[str, float]:
    now = now or time.time()
    arr = ledger.get(f"{coin}:{direction}", [])
    return {w: round(sum(n for ts, n in arr if now - ts <= sec), 2)
            for w, sec in WINDOWS_SEC.items()}
