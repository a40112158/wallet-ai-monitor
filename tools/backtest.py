from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser(description="Summarize wallet-monitor signal performance from SQLite state")
    p.add_argument("--db", default=".state/wallet_monitor.sqlite3")
    args = p.parse_args()
    db = Path(args.db)
    if not db.exists():
        print(f"DB not found: {db}")
        return 2
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        WITH latest AS (
          SELECT signal_id, pnl_pct, conservative_pnl_pct, mfe_pct, mae_pct,
                 ROW_NUMBER() OVER (PARTITION BY signal_id ORDER BY ts DESC) rn
          FROM signal_pnl
        )
        SELECT s.coin, s.side, COUNT(*) signals,
               AVG(l.pnl_pct) avg_pnl_pct,
               AVG(l.conservative_pnl_pct) avg_conservative_pnl_pct,
               AVG(CASE WHEN l.pnl_pct > 0 THEN 1.0 ELSE 0.0 END) win_rate,
               AVG(l.mfe_pct) avg_mfe_pct,
               AVG(l.mae_pct) avg_mae_pct
        FROM signals s
        JOIN latest l ON l.signal_id=s.id AND l.rn=1
        GROUP BY s.coin, s.side
        HAVING COUNT(*) >= 2
        ORDER BY avg_conservative_pnl_pct DESC
        LIMIT 50
        """
    ).fetchall()
    print("coin side signals avg_pnl% avg_cons% win_rate avg_mfe% avg_mae%")
    for r in rows:
        print(
            f"{r['coin']} {r['side']} {r['signals']} "
            f"{(r['avg_pnl_pct'] or 0):.2f} {(r['avg_conservative_pnl_pct'] or 0):.2f} "
            f"{(r['win_rate'] or 0):.2%} {(r['avg_mfe_pct'] or 0):.2f} {(r['avg_mae_pct'] or 0):.2f}"
        )
    v = conn.execute(
        """
        SELECT COUNT(*) total,
               SUM(CASE WHEN status='OPEN' THEN 1 ELSE 0 END) open_count,
               SUM(CASE WHEN status='CLOSED' AND pnl_pct>0 THEN 1 ELSE 0 END) wins,
               SUM(CASE WHEN status='CLOSED' AND pnl_pct<=0 THEN 1 ELSE 0 END) losses,
               AVG(CASE WHEN status='CLOSED' THEN pnl_pct END) avg_closed_pnl_pct,
               SUM(CASE WHEN status='CLOSED' THEN pnl_usd ELSE 0 END) realized_pnl_usd
        FROM virtual_trades
        """
    ).fetchone()
    if v:
        print("\nVirtual account:")
        print(dict(v))
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
