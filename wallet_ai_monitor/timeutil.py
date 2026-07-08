"""统一北京时间 (CST, UTC+8) 工具。"""
from __future__ import annotations

from datetime import datetime, timezone, timedelta

BEIJING = timezone(timedelta(hours=8))


def now_bj() -> datetime:
    return datetime.now(BEIJING)


def fmt_bj(ts: float | None = None) -> str:
    dt = now_bj() if ts is None else datetime.fromtimestamp(ts, BEIJING)
    return dt.strftime("%Y-%m-%d %H:%M:%S") + " CST"


def date_bj() -> str:
    return now_bj().strftime("%Y-%m-%d")
