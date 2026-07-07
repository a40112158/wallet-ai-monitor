from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PnlResult:
    side: str
    entry_px: float
    current_px: float
    notional_usd: float | None
    leverage: float
    pnl_pct: float
    leveraged_roe_pct: float
    pnl_usd: float | None


def calc_pnl(side: str, entry_px: float, current_px: float, leverage: float = 1.0, notional_usd: float | None = None) -> PnlResult:
    if entry_px <= 0:
        raise ValueError("entry_px must be positive")
    side_u = side.upper()
    if side_u in {"LONG", "OPEN_LONG", "BUY"}:
        raw = (current_px - entry_px) / entry_px
        side_norm = "LONG"
    elif side_u in {"SHORT", "OPEN_SHORT", "SELL"}:
        raw = (entry_px - current_px) / entry_px
        side_norm = "SHORT"
    else:
        raise ValueError("side must be LONG/SHORT")
    lev = max(float(leverage or 1), 1.0)
    pnl_usd = None if notional_usd is None else float(notional_usd) * raw
    return PnlResult(
        side=side_norm,
        entry_px=float(entry_px),
        current_px=float(current_px),
        notional_usd=None if notional_usd is None else float(notional_usd),
        leverage=lev,
        pnl_pct=raw * 100.0,
        leveraged_roe_pct=raw * lev * 100.0,
        pnl_usd=pnl_usd,
    )
