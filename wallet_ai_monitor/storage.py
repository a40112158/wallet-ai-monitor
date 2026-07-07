from __future__ import annotations

import json
import sqlite3
import time
from pathlib import Path
from typing import Any

from .hyperliquid import Position

SCHEMA = """
CREATE TABLE IF NOT EXISTS position_snapshots (
    ts INTEGER NOT NULL,
    wallet TEXT NOT NULL,
    wallet_group TEXT NOT NULL,
    coin TEXT NOT NULL,
    side TEXT NOT NULL,
    size REAL NOT NULL,
    abs_size REAL NOT NULL,
    entry_px REAL,
    mark_px REAL,
    position_value REAL NOT NULL,
    unrealized_pnl REAL,
    roe REAL,
    leverage REAL,
    raw_json TEXT,
    PRIMARY KEY (ts, wallet, coin)
);
CREATE INDEX IF NOT EXISTS idx_pos_wallet_coin_ts ON position_snapshots(wallet, coin, ts);
CREATE INDEX IF NOT EXISTS idx_pos_ts ON position_snapshots(ts);

CREATE TABLE IF NOT EXISTS latest_positions (
    wallet TEXT NOT NULL,
    wallet_group TEXT NOT NULL,
    coin TEXT NOT NULL,
    side TEXT NOT NULL,
    size REAL NOT NULL,
    abs_size REAL NOT NULL,
    entry_px REAL,
    mark_px REAL,
    position_value REAL NOT NULL,
    unrealized_pnl REAL,
    roe REAL,
    leverage REAL,
    updated_ts INTEGER NOT NULL,
    raw_json TEXT,
    PRIMARY KEY (wallet, coin)
);

CREATE TABLE IF NOT EXISTS run_log (
    ts INTEGER PRIMARY KEY,
    wallets_total INTEGER,
    wallets_scanned INTEGER,
    positions_count INTEGER,
    signals_count INTEGER,
    ai_enabled INTEGER,
    ai_ok INTEGER,
    duration_sec REAL,
    note TEXT
);

CREATE TABLE IF NOT EXISTS signals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts INTEGER NOT NULL,
    coin TEXT NOT NULL,
    side TEXT NOT NULL,
    direction TEXT,
    wallet_count INTEGER NOT NULL,
    total_delta_notional REAL NOT NULL,
    total_position_value REAL NOT NULL,
    weighted_score REAL NOT NULL,
    avg_entry_px REAL,
    mark_px REAL,
    ai_confidence REAL,
    ai_json TEXT,
    status TEXT DEFAULT 'OPEN',
    details_json TEXT
);
CREATE INDEX IF NOT EXISTS idx_signals_coin_side_ts ON signals(coin, side, ts);
CREATE INDEX IF NOT EXISTS idx_signals_status_ts ON signals(status, ts);

CREATE TABLE IF NOT EXISTS signal_state (
    coin TEXT NOT NULL,
    side TEXT NOT NULL,
    first_seen_ts INTEGER NOT NULL,
    last_seen_ts INTEGER NOT NULL,
    last_alert_ts INTEGER,
    seen_runs INTEGER DEFAULT 0,
    alert_runs INTEGER DEFAULT 0,
    suppressed_runs INTEGER DEFAULT 0,
    last_amount REAL DEFAULT 0,
    last_status TEXT,
    previous_signal_id INTEGER,
    PRIMARY KEY(coin, side)
);

CREATE TABLE IF NOT EXISTS signal_wallets (
    signal_id INTEGER NOT NULL,
    ts INTEGER NOT NULL,
    wallet TEXT NOT NULL,
    wallet_group TEXT,
    coin TEXT NOT NULL,
    side TEXT NOT NULL,
    event TEXT,
    delta_notional REAL,
    weight REAL,
    wallet_score REAL,
    PRIMARY KEY(signal_id, wallet, coin, side, event)
);
CREATE INDEX IF NOT EXISTS idx_signal_wallets_wallet ON signal_wallets(wallet, ts);

CREATE TABLE IF NOT EXISTS signal_pnl (
    signal_id INTEGER NOT NULL,
    ts INTEGER NOT NULL,
    mark_px REAL NOT NULL,
    pnl_pct REAL,
    leveraged_roe_pct REAL,
    pnl_usd REAL,
    conservative_pnl_pct REAL,
    conservative_pnl_usd REAL,
    mfe_pct REAL,
    mae_pct REAL,
    PRIMARY KEY(signal_id, ts)
);

CREATE TABLE IF NOT EXISTS wallet_scores (
    wallet TEXT PRIMARY KEY,
    wallet_group TEXT,
    trades INTEGER DEFAULT 0,
    wins INTEGER DEFAULT 0,
    losses INTEGER DEFAULT 0,
    avg_pnl_pct REAL DEFAULT 0,
    score REAL DEFAULT 1,
    last_updated_ts INTEGER
);


CREATE TABLE IF NOT EXISTS wallet_perf_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts_open INTEGER NOT NULL,
    wallet TEXT NOT NULL,
    wallet_group TEXT,
    coin TEXT NOT NULL,
    side TEXT NOT NULL,
    event TEXT,
    entry_px REAL NOT NULL,
    delta_notional REAL NOT NULL,
    weight REAL DEFAULT 1,
    horizon_hours INTEGER NOT NULL,
    due_ts INTEGER NOT NULL,
    evaluated_ts INTEGER,
    close_px REAL,
    pnl_pct REAL,
    win INTEGER,
    raw_json TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_wallet_perf_unique
ON wallet_perf_events(ts_open,wallet,coin,side,horizon_hours);
CREATE INDEX IF NOT EXISTS idx_wallet_perf_due ON wallet_perf_events(evaluated_ts,due_ts);
CREATE INDEX IF NOT EXISTS idx_wallet_perf_wallet ON wallet_perf_events(wallet,evaluated_ts);

CREATE TABLE IF NOT EXISTS ai_cache (
    cache_key TEXT PRIMARY KEY,
    created_ts INTEGER NOT NULL,
    model TEXT,
    response_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ai_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts INTEGER NOT NULL,
    model TEXT,
    purpose TEXT,
    prompt_tokens INTEGER DEFAULT 0,
    completion_tokens INTEGER DEFAULT 0,
    total_tokens INTEGER DEFAULT 0,
    estimated_points INTEGER DEFAULT 0,
    cached INTEGER DEFAULT 0,
    ok INTEGER DEFAULT 0
);
CREATE INDEX IF NOT EXISTS idx_ai_usage_ts ON ai_usage(ts);

CREATE TABLE IF NOT EXISTS meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS virtual_trades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    signal_id INTEGER,
    ts_open INTEGER NOT NULL,
    ts_close INTEGER,
    coin TEXT NOT NULL,
    side TEXT NOT NULL,
    entry_px REAL NOT NULL,
    close_px REAL,
    notional_usd REAL NOT NULL,
    status TEXT NOT NULL DEFAULT 'OPEN',
    reason TEXT,
    pnl_pct REAL,
    pnl_usd REAL,
    max_favorable_pct REAL DEFAULT 0,
    max_adverse_pct REAL DEFAULT 0,
    ai_confidence REAL,
    leverage REAL DEFAULT 1,
    margin_usd REAL,
    ai_open_reason TEXT,
    ai_exit_confidence REAL,
    ai_exit_reason TEXT
);
CREATE INDEX IF NOT EXISTS idx_virtual_open ON virtual_trades(status, coin, side);
"""



def _wallet_quality_grade(score: float, trades: int, min_sample_size: int) -> str:
    if trades < max(1, min_sample_size):
        return "NEW"
    if score >= 1.55:
        return "S"
    if score >= 1.25:
        return "A"
    if score >= 0.90:
        return "B"
    if score >= 0.70:
        return "C"
    return "D"


class Store:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)
        self._migrate()
        self.conn.commit()

    def _migrate(self) -> None:
        self._ensure_columns("signals", {
            "direction": "TEXT",
            "details_json": "TEXT",
        })
        self._ensure_columns("signal_pnl", {
            "conservative_pnl_pct": "REAL",
            "conservative_pnl_usd": "REAL",
            "mfe_pct": "REAL",
            "mae_pct": "REAL",
        })
        self._ensure_columns("virtual_trades", {
            "leverage": "REAL DEFAULT 1",
            "margin_usd": "REAL",
            "ai_open_reason": "TEXT",
            "ai_exit_confidence": "REAL",
            "ai_exit_reason": "TEXT",
        })
        self._ensure_columns("wallet_scores", {
            "trades_24h": "INTEGER DEFAULT 0",
            "wins_24h": "INTEGER DEFAULT 0",
            "win_rate_24h": "REAL",
            "avg_pnl_24h": "REAL",
            "trades_72h": "INTEGER DEFAULT 0",
            "wins_72h": "INTEGER DEFAULT 0",
            "win_rate_72h": "REAL",
            "avg_pnl_72h": "REAL",
            "trades_168h": "INTEGER DEFAULT 0",
            "wins_168h": "INTEGER DEFAULT 0",
            "win_rate_168h": "REAL",
            "avg_pnl_168h": "REAL",
            "profit_factor": "REAL",
            "quality_grade": "TEXT",
            "perf_json": "TEXT",
        })

    def _ensure_columns(self, table: str, columns: dict[str, str]) -> None:
        current = {r[1] for r in self.conn.execute(f"PRAGMA table_info({table})").fetchall()}
        for name, typ in columns.items():
            if name not in current:
                self.conn.execute(f"ALTER TABLE {table} ADD COLUMN {name} {typ}")

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "Store":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def get_meta(self, key: str, default: str | None = None) -> str | None:
        row = self.conn.execute("SELECT value FROM meta WHERE key=?", (key,)).fetchone()
        return str(row["value"]) if row else default

    def set_meta(self, key: str, value: str | int | float) -> None:
        self.conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES (?,?)", (key, str(value)))
        self.conn.commit()

    def latest_map(self) -> dict[tuple[str, str], sqlite3.Row]:
        rows = self.conn.execute("SELECT * FROM latest_positions").fetchall()
        return {(r["wallet"], r["coin"]): r for r in rows}

    def wallets_with_latest(self, wallets: list[str]) -> set[str]:
        if not wallets:
            return set()
        out: set[str] = set()
        chunk_size = 500
        for i in range(0, len(wallets), chunk_size):
            chunk = wallets[i:i + chunk_size]
            marks = ",".join("?" for _ in chunk)
            rows = self.conn.execute(f"SELECT DISTINCT wallet FROM latest_positions WHERE wallet IN ({marks})", chunk).fetchall()
            out.update(str(r["wallet"]) for r in rows)
        return out

    def save_positions(self, ts: int, positions: list[Position]) -> None:
        with self.conn:
            self._save_positions(self.conn.cursor(), ts, positions)

    @staticmethod
    def _save_positions(cur: sqlite3.Cursor, ts: int, positions: list[Position]) -> None:
        for p in positions:
            raw_json = json.dumps(p.raw, ensure_ascii=False, separators=(",", ":"))
            cur.execute(
                """
                INSERT OR REPLACE INTO position_snapshots
                (ts,wallet,wallet_group,coin,side,size,abs_size,entry_px,mark_px,position_value,unrealized_pnl,roe,leverage,raw_json)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (ts, p.wallet, p.group, p.coin, p.side, p.size, p.abs_size, p.entry_px, p.mark_px,
                 p.position_value, p.unrealized_pnl, p.roe, p.leverage, raw_json),
            )
            cur.execute(
                """
                INSERT OR REPLACE INTO latest_positions
                (wallet,wallet_group,coin,side,size,abs_size,entry_px,mark_px,position_value,unrealized_pnl,roe,leverage,updated_ts,raw_json)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (p.wallet, p.group, p.coin, p.side, p.size, p.abs_size, p.entry_px, p.mark_px,
                 p.position_value, p.unrealized_pnl, p.roe, p.leverage, ts, raw_json),
            )

    def replace_latest_for_scanned_wallets(self, ts: int, positions: list[Position], scanned_wallets: list[str]) -> None:
        # Deleting the old baseline and writing the new one must be atomic. Otherwise a
        # cancelled run can erase baselines and create misleading signals next time.
        with self.conn:
            cur = self.conn.cursor()
            cur.executemany("DELETE FROM latest_positions WHERE wallet=?", [(w,) for w in scanned_wallets])
            self._save_positions(cur, ts, positions)

    def wallet_score_map(self) -> dict[str, float]:
        rows = self.conn.execute("SELECT wallet, score FROM wallet_scores").fetchall()
        return {str(r["wallet"]): float(r["score"] or 1.0) for r in rows}

    def wallet_performance_map(self) -> dict[str, dict[str, Any]]:
        rows = self.conn.execute("SELECT * FROM wallet_scores").fetchall()
        out: dict[str, dict[str, Any]] = {}
        for r in rows:
            d = dict(r)
            perf = {}
            raw = d.get("perf_json")
            if raw:
                try:
                    perf = json.loads(raw)
                except json.JSONDecodeError:
                    perf = {}
            d["perf"] = perf
            out[str(d.get("wallet"))] = d
        return out


    def update_signal_state(
        self,
        ts: int,
        raw_signals: list[dict[str, Any]],
        kept_signals: list[dict[str, Any]],
        lifecycle_events: list[dict[str, Any]],
        *,
        cooldown_seconds: int,
    ) -> dict[tuple[str, str], dict[str, Any]]:
        """Track how long each coin/side signal has been appearing.

        This is intentionally separate from the main `signals` table because cooldown
        can suppress duplicate alerts. The state still counts those suppressed rounds,
        so the report can say "this is the 6th time we saw it" even if only the first
        alert was inserted as an active signal.
        """
        raw_signals = raw_signals or []
        kept_ids = {id(s) for s in kept_signals or []}
        lifecycle_by_key: dict[tuple[str, str], dict[str, Any]] = {}
        for e in lifecycle_events or []:
            key = (str(e.get("coin")), str(e.get("side")))
            lifecycle_by_key[key] = e

        out: dict[tuple[str, str], dict[str, Any]] = {}
        for s in raw_signals:
            key = (str(s.get("coin")), str(s.get("side")))
            if not key[0] or not key[1] or key[0] == "None" or key[1] == "None":
                continue
            amount = float(s.get("total_delta_notional") or 0.0)
            row = self.conn.execute(
                "SELECT * FROM signal_state WHERE coin=? AND side=?",
                key,
            ).fetchone()

            if row is None:
                # Backfill from historical signals so the first upgraded run does not
                # incorrectly label every existing coin/side as brand new.
                hist = self.conn.execute(
                    """
                    SELECT MIN(ts) AS first_ts, MAX(ts) AS last_ts, COUNT(*) AS c,
                           MAX(total_delta_notional) AS max_amount
                    FROM signals
                    WHERE coin=? AND side=?
                    """,
                    key,
                ).fetchone()
                hist_count = int(hist["c"] or 0) if hist else 0
                first_seen = int(hist["first_ts"] or ts) if hist and hist_count else ts
                last_seen_prev = int(hist["last_ts"] or 0) if hist and hist_count else 0
                last_alert_prev = last_seen_prev or None
                seen_prev = hist_count
                alert_prev = hist_count
                suppressed_prev = 0
                last_amount_prev = float(hist["max_amount"] or 0.0) if hist and hist_count else 0.0
                previous_signal_id = None
                previous_status = None
            else:
                first_seen = int(row["first_seen_ts"])
                last_seen_prev = int(row["last_seen_ts"] or 0)
                last_alert_prev = int(row["last_alert_ts"] or 0) if row["last_alert_ts"] is not None else None
                seen_prev = int(row["seen_runs"] or 0)
                alert_prev = int(row["alert_runs"] or 0)
                suppressed_prev = int(row["suppressed_runs"] or 0)
                last_amount_prev = float(row["last_amount"] or 0.0)
                previous_signal_id = int(row["previous_signal_id"]) if row["previous_signal_id"] is not None else None
                previous_status = row["last_status"]

            event = lifecycle_by_key.get(key)
            kept = id(s) in kept_ids
            if event and event.get("event") == "COOLDOWN_MERGED":
                status = "COOLDOWN_REPEAT"
            elif "cooldown_realert_large_add" in (s.get("risk_tags") or []):
                status = "RE_ALERT"
            elif seen_prev <= 0:
                status = "NEW_SIGNAL"
            elif kept:
                status = "ACTIVE_REPEAT"
            else:
                status = "SEEN"

            seen_runs = seen_prev + 1
            alert_runs = alert_prev + (0 if status == "COOLDOWN_REPEAT" else 1)
            suppressed_runs = suppressed_prev + (1 if status == "COOLDOWN_REPEAT" else 0)
            last_alert_ts = last_alert_prev if status == "COOLDOWN_REPEAT" else ts

            if last_amount_prev > 0:
                amount_change_ratio = amount / last_amount_prev
            else:
                amount_change_ratio = None

            age_minutes = max(0.0, (ts - first_seen) / 60.0)
            since_last_alert_minutes = None
            cooldown_remaining_minutes = None
            if last_alert_prev:
                since_last_alert_minutes = max(0.0, (ts - last_alert_prev) / 60.0)
                cooldown_remaining_minutes = max(0.0, (cooldown_seconds - (ts - last_alert_prev)) / 60.0)
            if status != "COOLDOWN_REPEAT":
                cooldown_remaining_minutes = max(0.0, cooldown_seconds / 60.0) if cooldown_seconds > 0 else 0.0

            state = {
                "status": status,
                "previous_status": previous_status,
                "first_seen_ts": first_seen,
                "last_seen_ts": ts,
                "last_alert_ts": last_alert_ts,
                "seen_runs": seen_runs,
                "alert_runs": alert_runs,
                "suppressed_runs": suppressed_runs,
                "age_minutes": round(age_minutes, 1),
                "since_last_alert_minutes": None if since_last_alert_minutes is None else round(since_last_alert_minutes, 1),
                "cooldown_remaining_minutes": None if cooldown_remaining_minutes is None else round(cooldown_remaining_minutes, 1),
                "amount_change_ratio": None if amount_change_ratio is None else round(amount_change_ratio, 4),
                "previous_amount": round(last_amount_prev, 2),
                "current_amount": round(amount, 2),
                "previous_signal_id": previous_signal_id or (int(event["previous_signal_id"]) if event and event.get("previous_signal_id") is not None else None),
            }
            s["signal_state"] = state
            s["signal_status"] = status
            s["signal_seen_runs"] = seen_runs
            s["signal_age_minutes"] = state["age_minutes"]
            s["cooldown_remaining_minutes"] = state["cooldown_remaining_minutes"]
            s["amount_change_ratio"] = state["amount_change_ratio"]
            out[key] = state

            self.conn.execute(
                """
                INSERT OR REPLACE INTO signal_state
                (coin,side,first_seen_ts,last_seen_ts,last_alert_ts,seen_runs,alert_runs,suppressed_runs,last_amount,last_status,previous_signal_id)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    key[0], key[1], first_seen, ts, last_alert_ts, seen_runs, alert_runs,
                    suppressed_runs, amount, status, state["previous_signal_id"],
                ),
            )

        for e in lifecycle_events or []:
            key = (str(e.get("coin")), str(e.get("side")))
            state = out.get(key)
            if state:
                e["signal_state"] = state
                e["seen_runs"] = state.get("seen_runs")
                e["signal_status"] = state.get("status")
                e["cooldown_remaining_minutes"] = state.get("cooldown_remaining_minutes")
                e["amount_change_ratio"] = state.get("amount_change_ratio")
        self.conn.commit()
        return out

    def insert_signal(self, ts: int, signal: dict[str, Any]) -> int:
        cur = self.conn.cursor()
        details_json = json.dumps(signal, ensure_ascii=False, default=str)
        cur.execute(
            """
            INSERT INTO signals
            (ts,coin,side,direction,wallet_count,total_delta_notional,total_position_value,weighted_score,avg_entry_px,mark_px,ai_confidence,ai_json,status,details_json)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                ts,
                signal["coin"],
                signal["side"],
                signal.get("direction"),
                signal["wallet_count"],
                signal["total_delta_notional"],
                signal["total_position_value"],
                signal["weighted_score"],
                signal.get("avg_entry_px"),
                signal.get("mark_px"),
                signal.get("ai_confidence"),
                json.dumps(signal.get("ai", {}), ensure_ascii=False),
                signal.get("status", "OPEN"),
                details_json,
            ),
        )
        signal_id = int(cur.lastrowid)
        for w in signal.get("wallets", []) or []:
            cur.execute(
                """
                INSERT OR REPLACE INTO signal_wallets
                (signal_id,ts,wallet,wallet_group,coin,side,event,delta_notional,weight,wallet_score)
                VALUES (?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    signal_id,
                    ts,
                    str(w.get("wallet")),
                    str(w.get("group")),
                    signal["coin"],
                    signal["side"],
                    str(w.get("event")),
                    float(w.get("delta_notional") or 0),
                    float(w.get("weight") or 1),
                    float(w.get("wallet_score") or 1),
                ),
            )
        self.conn.commit()
        return signal_id

    def recent_open_signals(self, since_ts: int) -> list[sqlite3.Row]:
        return self.conn.execute(
            "SELECT * FROM signals WHERE status='OPEN' AND ts>=? ORDER BY ts DESC", (since_ts,)
        ).fetchall()

    def latest_pnl_extrema(self, signal_id: int) -> tuple[float | None, float | None]:
        row = self.conn.execute(
            "SELECT MAX(mfe_pct) AS mfe, MIN(mae_pct) AS mae FROM signal_pnl WHERE signal_id=?", (signal_id,)
        ).fetchone()
        if not row:
            return None, None
        return row["mfe"], row["mae"]

    def save_signal_pnl(
        self,
        signal_id: int,
        ts: int,
        mark_px: float,
        pnl_pct: float,
        leveraged_roe_pct: float,
        pnl_usd: float | None,
        conservative_pnl_pct: float | None = None,
        conservative_pnl_usd: float | None = None,
    ) -> None:
        self.save_signal_pnls(ts, [{
            "signal_id": signal_id,
            "current_px": mark_px,
            "pnl_pct": pnl_pct,
            "leveraged_roe_pct": leveraged_roe_pct,
            "pnl_usd": pnl_usd,
            "conservative_pnl_pct": conservative_pnl_pct,
            "conservative_pnl_usd": conservative_pnl_usd,
        }])

    def save_signal_pnls(self, ts: int, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Persist a run's PnL rows in one transaction and return true cumulative extrema."""
        if not rows:
            return []
        extrema: dict[int, tuple[float | None, float | None]] = {}
        signal_ids = sorted({int(r["signal_id"]) for r in rows})
        for i in range(0, len(signal_ids), 500):
            chunk = signal_ids[i:i + 500]
            marks = ",".join("?" for _ in chunk)
            found = self.conn.execute(
                f"SELECT signal_id, MAX(mfe_pct) AS mfe, MIN(mae_pct) AS mae "
                f"FROM signal_pnl WHERE signal_id IN ({marks}) GROUP BY signal_id",
                chunk,
            ).fetchall()
            extrema.update({int(r["signal_id"]): (r["mfe"], r["mae"]) for r in found})

        persisted: list[dict[str, Any]] = []
        values = []
        for row in rows:
            signal_id = int(row["signal_id"])
            pnl_pct = float(row["pnl_pct"])
            prev_mfe, prev_mae = extrema.get(signal_id, (None, None))
            mfe = pnl_pct if prev_mfe is None else max(float(prev_mfe), pnl_pct)
            mae = pnl_pct if prev_mae is None else min(float(prev_mae), pnl_pct)
            enriched = {**row, "mfe_pct": mfe, "mae_pct": mae}
            persisted.append(enriched)
            values.append((
                signal_id,
                ts,
                float(row["current_px"]),
                pnl_pct,
                float(row["leveraged_roe_pct"]),
                row.get("pnl_usd"),
                row.get("conservative_pnl_pct"),
                row.get("conservative_pnl_usd"),
                mfe,
                mae,
            ))
        with self.conn:
            self.conn.executemany(
                """
                INSERT OR REPLACE INTO signal_pnl
                (signal_id,ts,mark_px,pnl_pct,leveraged_roe_pct,pnl_usd,conservative_pnl_pct,conservative_pnl_usd,mfe_pct,mae_pct)
                VALUES (?,?,?,?,?,?,?,?,?,?)
                """,
                values,
            )
        return persisted

    def expire_signals_before(self, before_ts: int) -> int:
        with self.conn:
            cur = self.conn.execute(
                "UPDATE signals SET status='EXPIRED' WHERE status='OPEN' AND ts<?",
                (before_ts,),
            )
        return int(cur.rowcount)

    def prune_history(self, before_ts: int) -> int:
        """Bound long-running state growth while preserving current baselines and open trades."""
        before_changes = self.conn.total_changes
        with self.conn:
            self.conn.execute(
                "DELETE FROM virtual_trades WHERE status='CLOSED' AND ts_close IS NOT NULL AND ts_close<?",
                (before_ts,),
            )
            self.conn.execute(
                "DELETE FROM signal_wallets WHERE signal_id IN (SELECT id FROM signals WHERE ts<?)",
                (before_ts,),
            )
            self.conn.execute(
                "DELETE FROM signal_pnl WHERE signal_id IN (SELECT id FROM signals WHERE ts<?)",
                (before_ts,),
            )
            self.conn.execute("DELETE FROM signals WHERE ts<?", (before_ts,))
            self.conn.execute("DELETE FROM position_snapshots WHERE ts<?", (before_ts,))
            self.conn.execute("DELETE FROM run_log WHERE ts<?", (before_ts,))
            self.conn.execute("DELETE FROM ai_cache WHERE created_ts<?", (before_ts,))
            self.conn.execute("DELETE FROM ai_usage WHERE ts<?", (before_ts,))
            self.conn.execute("DELETE FROM wallet_perf_events WHERE evaluated_ts IS NOT NULL AND evaluated_ts<?", (before_ts,))
        return self.conn.total_changes - before_changes

    def record_wallet_perf_events(
        self,
        ts: int,
        deltas: list[dict[str, Any]],
        *,
        horizons_hours: list[int],
        min_delta_notional: float = 0.0,
    ) -> int:
        """Record wallet-level open/increase decisions for later 24h/72h/7d evaluation."""
        if not deltas or not horizons_hours:
            return 0
        rows = []
        for d in deltas:
            if d.get("event") not in {"NEW_POSITION", "INCREASE_POSITION", "FLIP_POSITION"}:
                continue
            try:
                delta_notional = float(d.get("delta_notional") or 0)
                entry_px = float(d.get("mark_px") or d.get("entry_px") or 0)
            except (TypeError, ValueError):
                continue
            if delta_notional < min_delta_notional or entry_px <= 0:
                continue
            raw_json = json.dumps({
                "event": d.get("event"),
                "wallet_score_at_open": d.get("wallet_score"),
                "effective_weight": d.get("effective_weight"),
                "roe": d.get("roe"),
                "leverage": d.get("leverage"),
            }, ensure_ascii=False, separators=(",", ":"))
            for h in horizons_hours:
                if int(h) <= 0:
                    continue
                rows.append((
                    int(ts),
                    str(d.get("wallet")),
                    str(d.get("group") or ""),
                    str(d.get("coin")),
                    str(d.get("side")),
                    str(d.get("event")),
                    entry_px,
                    delta_notional,
                    float(d.get("weight") or 1.0),
                    int(h),
                    int(ts) + int(h) * 3600,
                    raw_json,
                ))
        if not rows:
            return 0
        before = self.conn.total_changes
        with self.conn:
            self.conn.executemany(
                """
                INSERT OR IGNORE INTO wallet_perf_events
                (ts_open,wallet,wallet_group,coin,side,event,entry_px,delta_notional,weight,horizon_hours,due_ts,raw_json)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                rows,
            )
        return self.conn.total_changes - before

    def update_wallet_perf_outcomes(self, ts: int, mids: dict[str, float], *, max_updates: int = 5000) -> int:
        """Evaluate due wallet-performance events using current mark prices."""
        if not mids:
            return 0
        rows = self.conn.execute(
            """
            SELECT * FROM wallet_perf_events
            WHERE evaluated_ts IS NULL AND due_ts<=?
            ORDER BY due_ts ASC
            LIMIT ?
            """,
            (int(ts), int(max_updates)),
        ).fetchall()
        updates = []
        for r in rows:
            coin = str(r["coin"])
            close_px = mids.get(coin)
            if close_px is None:
                continue
            try:
                entry_px = float(r["entry_px"])
                close_px = float(close_px)
                if entry_px <= 0 or close_px <= 0:
                    continue
                if str(r["side"]) == "LONG":
                    pnl_pct = (close_px - entry_px) / entry_px * 100.0
                else:
                    pnl_pct = (entry_px - close_px) / entry_px * 100.0
            except (TypeError, ValueError):
                continue
            updates.append((int(ts), close_px, pnl_pct, 1 if pnl_pct > 0 else 0, int(r["id"])))
        if not updates:
            return 0
        with self.conn:
            self.conn.executemany(
                """
                UPDATE wallet_perf_events
                SET evaluated_ts=?, close_px=?, pnl_pct=?, win=?
                WHERE id=?
                """,
                updates,
            )
        return len(updates)

    def wallet_perf_summary(self, limit: int = 12) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            """
            SELECT wallet,wallet_group,trades,wins,losses,avg_pnl_pct,score,quality_grade,
                   trades_24h,win_rate_24h,avg_pnl_24h,
                   trades_72h,win_rate_72h,avg_pnl_72h,
                   trades_168h,win_rate_168h,avg_pnl_168h,
                   profit_factor,last_updated_ts
            FROM wallet_scores
            WHERE trades>0
            ORDER BY score DESC, trades DESC
            LIMIT ?
            """,
            (int(limit),),
        ).fetchall()
        return [dict(r) for r in rows]

    def wallet_scores_rows(self, limit: int = 1000) -> list[dict[str, Any]]:
        """Return wallet quality classifications for report export.

        Rows appear only after a wallet has at least one evaluated performance sample.
        Wallets with fewer than WALLET_PERF_MIN_SAMPLE_SIZE samples are marked NEW.
        """
        rows = self.conn.execute(
            """
            SELECT wallet,wallet_group,trades,wins,losses,avg_pnl_pct,score,quality_grade,
                   trades_24h,wins_24h,win_rate_24h,avg_pnl_24h,
                   trades_72h,wins_72h,win_rate_72h,avg_pnl_72h,
                   trades_168h,wins_168h,win_rate_168h,avg_pnl_168h,
                   profit_factor,last_updated_ts
            FROM wallet_scores
            WHERE trades>0
            ORDER BY
                CASE quality_grade
                    WHEN 'S' THEN 1
                    WHEN 'A' THEN 2
                    WHEN 'B' THEN 3
                    WHEN 'C' THEN 4
                    WHEN 'D' THEN 5
                    WHEN 'NEW' THEN 6
                    ELSE 7
                END,
                score DESC,
                trades DESC
            LIMIT ?
            """,
            (int(limit),),
        ).fetchall()
        return [dict(r) for r in rows]

    def refresh_wallet_scores(
        self,
        ts: int,
        min_age_seconds: int = 3600,
        *,
        decay_days: int = 30,
        min_sample_size: int = 5,
    ) -> int:
        """Refresh per-wallet quality scores from evaluated wallet-level outcomes.

        Fallback to old signal-level PnL exists for older databases, but the primary
        score now comes from wallet_perf_events: each wallet's add/open event is judged
        at 24h / 72h / 168h. This makes the signal engine care who is buying/selling,
        not only how much was bought/sold.
        """
        perf_rows = self.conn.execute(
            """
            SELECT wallet, wallet_group, horizon_hours, pnl_pct, win, evaluated_ts, delta_notional
            FROM wallet_perf_events
            WHERE evaluated_ts IS NOT NULL AND pnl_pct IS NOT NULL
            """
        ).fetchall()

        by_wallet: dict[str, list[sqlite3.Row]] = {}
        group_by_wallet: dict[str, str] = {}
        for r in perf_rows:
            wallet = str(r["wallet"])
            by_wallet.setdefault(wallet, []).append(r)
            group_by_wallet[wallet] = str(r["wallet_group"] or "")

        if not by_wallet:
            # Backward-compatible fallback for databases created before wallet_perf_events.
            rows = self.conn.execute(
                """
                SELECT sw.wallet, sw.wallet_group, sp.pnl_pct
                FROM signal_wallets sw
                JOIN (
                    SELECT signal_id, pnl_pct, ROW_NUMBER() OVER (PARTITION BY signal_id ORDER BY ts DESC) rn
                    FROM signal_pnl
                ) sp ON sp.signal_id=sw.signal_id AND sp.rn=1
                JOIN signals s ON s.id=sw.signal_id
                WHERE ? - s.ts >= ?
                """,
                (ts, min_age_seconds),
            ).fetchall()
            legacy: dict[str, list[float]] = {}
            for r in rows:
                wallet = str(r["wallet"])
                group_by_wallet[wallet] = str(r["wallet_group"] or "")
                try:
                    legacy.setdefault(wallet, []).append(float(r["pnl_pct"] or 0))
                except (TypeError, ValueError):
                    continue
            for wallet, pnls in legacy.items():
                trades = len(pnls)
                wins = sum(1 for p in pnls if p > 0)
                losses = sum(1 for p in pnls if p <= 0)
                avg = sum(pnls) / trades if trades else 0.0
                win_rate = wins / trades if trades else 0.0
                score = max(0.45, min(2.20, 0.65 + win_rate * 0.9 + avg / 10.0))
                grade = _wallet_quality_grade(score, trades, min_sample_size)
                self.conn.execute(
                    """
                    INSERT OR REPLACE INTO wallet_scores(wallet,wallet_group,trades,wins,losses,avg_pnl_pct,score,last_updated_ts,quality_grade,perf_json)
                    VALUES (?,?,?,?,?,?,?,?,?,?)
                    """,
                    (wallet, group_by_wallet.get(wallet), trades, wins, losses, avg, score, ts, grade, json.dumps({"legacy": True}, ensure_ascii=False)),
                )
            self.conn.commit()
            return len(legacy)

        decay_seconds = max(1, int(decay_days) * 86400)
        updated = 0
        for wallet, rows in by_wallet.items():
            weighted_total = 0.0
            weighted_wins = 0.0
            weighted_pnl = 0.0
            total_profit = 0.0
            total_loss = 0.0
            by_h: dict[int, list[tuple[float, float]]] = {}
            for r in rows:
                pnl = float(r["pnl_pct"] or 0)
                age = max(0, int(ts) - int(r["evaluated_ts"] or ts))
                recency_weight = 0.5 ** (age / decay_seconds)
                size_weight = min(3.0, max(0.5, (float(r["delta_notional"] or 0) / 100_000) ** 0.35))
                weight = recency_weight * size_weight
                h = int(r["horizon_hours"] or 0)
                by_h.setdefault(h, []).append((pnl, weight))
                weighted_total += weight
                weighted_pnl += pnl * weight
                if pnl > 0:
                    weighted_wins += weight
                    total_profit += pnl * weight
                else:
                    total_loss += abs(pnl) * weight

            trades = len(rows)
            wins = sum(1 for r in rows if float(r["pnl_pct"] or 0) > 0)
            losses = trades - wins
            avg = weighted_pnl / max(weighted_total, 1e-9)
            win_rate = weighted_wins / max(weighted_total, 1e-9)
            profit_factor = total_profit / max(total_loss, 1e-9) if total_loss > 0 else (total_profit if total_profit > 0 else 0.0)

            horizon_stats: dict[str, Any] = {}
            for h in (24, 72, 168):
                vals = by_h.get(h, [])
                if vals:
                    wsum = sum(w for _, w in vals)
                    wr = sum(w for pnl, w in vals if pnl > 0) / max(wsum, 1e-9)
                    ap = sum(pnl * w for pnl, w in vals) / max(wsum, 1e-9)
                    horizon_stats[str(h)] = {"trades": len(vals), "wins": sum(1 for pnl, _ in vals if pnl > 0), "win_rate": wr, "avg_pnl": ap}
                else:
                    horizon_stats[str(h)] = {"trades": 0, "wins": 0, "win_rate": None, "avg_pnl": None}

            # Score clamp: 0.35 - 2.50. Sample confidence prevents tiny samples from dominating.
            sample_conf = min(1.0, trades / max(float(min_sample_size), 1.0))
            expectancy_component = max(-0.45, min(0.65, avg / 12.0))
            pf_component = max(-0.25, min(0.35, (profit_factor - 1.0) / 4.0)) if profit_factor else -0.15
            raw_score = 1.0 + (win_rate - 0.5) * 1.25 + expectancy_component + pf_component
            score = 1.0 + (raw_score - 1.0) * sample_conf
            score = max(0.35, min(2.50, score))
            grade = _wallet_quality_grade(score, trades, min_sample_size)
            perf_json = {
                "sample_confidence": round(sample_conf, 4),
                "weighted_win_rate": round(win_rate, 4),
                "weighted_avg_pnl_pct": round(avg, 4),
                "profit_factor": round(profit_factor, 4),
                "horizons": {
                    k: {
                        "trades": v["trades"],
                        "wins": v["wins"],
                        "win_rate": None if v["win_rate"] is None else round(float(v["win_rate"]), 4),
                        "avg_pnl": None if v["avg_pnl"] is None else round(float(v["avg_pnl"]), 4),
                    }
                    for k, v in horizon_stats.items()
                },
            }

            self.conn.execute(
                """
                INSERT OR REPLACE INTO wallet_scores(
                    wallet,wallet_group,trades,wins,losses,avg_pnl_pct,score,last_updated_ts,
                    trades_24h,wins_24h,win_rate_24h,avg_pnl_24h,
                    trades_72h,wins_72h,win_rate_72h,avg_pnl_72h,
                    trades_168h,wins_168h,win_rate_168h,avg_pnl_168h,
                    profit_factor,quality_grade,perf_json
                )
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    wallet, group_by_wallet.get(wallet), trades, wins, losses, avg, score, ts,
                    horizon_stats["24"]["trades"], horizon_stats["24"]["wins"], horizon_stats["24"]["win_rate"], horizon_stats["24"]["avg_pnl"],
                    horizon_stats["72"]["trades"], horizon_stats["72"]["wins"], horizon_stats["72"]["win_rate"], horizon_stats["72"]["avg_pnl"],
                    horizon_stats["168"]["trades"], horizon_stats["168"]["wins"], horizon_stats["168"]["win_rate"], horizon_stats["168"]["avg_pnl"],
                    profit_factor, grade, json.dumps(perf_json, ensure_ascii=False),
                ),
            )
            updated += 1
        self.conn.commit()
        return updated

    def get_ai_cache(self, cache_key: str, max_age_seconds: int) -> dict[str, Any] | None:
        row = self.conn.execute("SELECT created_ts,response_json FROM ai_cache WHERE cache_key=?", (cache_key,)).fetchone()
        if not row:
            return None
        if max_age_seconds and int(time.time()) - int(row["created_ts"]) > max_age_seconds:
            return None
        try:
            return json.loads(row["response_json"])
        except json.JSONDecodeError:
            return None

    def save_ai_cache(self, cache_key: str, model: str, response: dict[str, Any]) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO ai_cache(cache_key,created_ts,model,response_json) VALUES (?,?,?,?)",
            (cache_key, int(time.time()), model, json.dumps(response, ensure_ascii=False)),
        )
        self.conn.commit()

    def open_virtual_trade(
        self,
        signal_id: int,
        ts: int,
        signal: dict[str, Any],
        notional_usd: float,
        *,
        leverage: float = 1.0,
        margin_usd: float | None = None,
        ai_open_reason: str | None = None,
    ) -> int | None:
        entry_px = signal.get("mark_px") or signal.get("avg_entry_px")
        if not entry_px or float(entry_px) <= 0 or notional_usd <= 0:
            return None
        lev = max(1.0, min(10.0, float(leverage or 1.0)))
        margin = float(margin_usd) if margin_usd is not None else float(notional_usd) / lev
        if margin <= 0:
            return None
        existing = self.conn.execute(
            "SELECT id FROM virtual_trades WHERE status='OPEN' AND coin=? AND side=?", (signal["coin"], signal["side"])
        ).fetchone()
        if existing:
            return None
        cur = self.conn.cursor()
        cur.execute(
            """
            INSERT INTO virtual_trades(signal_id,ts_open,coin,side,entry_px,notional_usd,ai_confidence,leverage,margin_usd,ai_open_reason)
            VALUES (?,?,?,?,?,?,?,?,?,?)
            """,
            (signal_id, ts, signal["coin"], signal["side"], float(entry_px), float(notional_usd), signal.get("ai_confidence"), lev, margin, ai_open_reason),
        )
        self.conn.commit()
        return int(cur.lastrowid)

    def count_open_virtual_trades(self) -> int:
        row = self.conn.execute("SELECT COUNT(*) AS c FROM virtual_trades WHERE status='OPEN'").fetchone()
        return int(row["c"] or 0)

    def virtual_open_notional(self) -> float:
        row = self.conn.execute(
            "SELECT COALESCE(SUM(notional_usd), 0) AS n FROM virtual_trades WHERE status='OPEN'"
        ).fetchone()
        return float(row["n"] or 0.0)

    def virtual_open_margin(self) -> float:
        row = self.conn.execute(
            "SELECT COALESCE(SUM(COALESCE(margin_usd, notional_usd / CASE WHEN COALESCE(leverage, 1) < 1 THEN 1 ELSE COALESCE(leverage, 1) END)), 0) AS n FROM virtual_trades WHERE status='OPEN'"
        ).fetchone()
        return float(row["n"] or 0.0)

    def virtual_open_rows(self) -> list[dict[str, Any]]:
        rows = self.conn.execute("SELECT * FROM virtual_trades WHERE status='OPEN' ORDER BY ts_open ASC").fetchall()
        return [dict(r) for r in rows]

    def update_virtual_trades(
        self,
        ts: int,
        mids: dict[str, float],
        *,
        take_profit_pct: float,
        stop_loss_pct: float,
        max_hold_seconds: int,
        ai_exit_decisions: dict[int, dict[str, Any]] | None = None,
        ai_close_min_confidence: float = 65.0,
        close_warning_enabled: bool = True,
        ai_pre_close_min_confidence: float = 50.0,
        close_warning_tp_ratio: float = 0.75,
        close_warning_sl_ratio: float = 0.75,
        close_warning_max_hold_ratio: float = 0.80,
    ) -> list[dict[str, Any]]:
        from .pnl import calc_pnl

        ai_exit_decisions = ai_exit_decisions or {}
        rows = self.conn.execute("SELECT * FROM virtual_trades WHERE status='OPEN' ORDER BY ts_open ASC").fetchall()
        out: list[dict[str, Any]] = []
        for r in rows:
            current = mids.get(str(r["coin"]))
            if current is None:
                continue
            lev = max(1.0, float(r["leverage"] or 1.0))
            result = calc_pnl(str(r["side"]), float(r["entry_px"]), float(current), leverage=lev, notional_usd=float(r["notional_usd"]))
            max_fav = max(float(r["max_favorable_pct"] or 0), result.pnl_pct)
            max_adv = min(float(r["max_adverse_pct"] or 0), result.pnl_pct)
            status = "OPEN"
            reason = None
            close_warning = False
            close_warning_reason = None
            close_warning_level = None
            ai_exit_conf = None
            ai_exit_reason = None
            age_seconds = max(0, ts - int(r["ts_open"]))

            decision = ai_exit_decisions.get(int(r["id"]))
            if decision:
                ai_exit_conf = float(decision.get("confidence") or 0)
                ai_exit_reason = str(decision.get("reason") or "")
                if str(decision.get("action") or "").upper() == "CLOSE" and ai_exit_conf >= ai_close_min_confidence:
                    status, reason = "CLOSED", "AI_CLOSE"
                elif (
                    close_warning_enabled
                    and str(decision.get("action") or "").upper() == "CLOSE"
                    and ai_exit_conf >= ai_pre_close_min_confidence
                ):
                    close_warning = True
                    close_warning_reason = "AI_PRE_CLOSE"
                    close_warning_level = "AI"

            if close_warning_enabled and status == "OPEN":
                tp_warn = abs(take_profit_pct) * max(0.0, min(0.99, close_warning_tp_ratio))
                sl_warn = abs(stop_loss_pct) * max(0.0, min(0.99, close_warning_sl_ratio))
                max_hold_warn = int(max_hold_seconds * max(0.0, min(0.99, close_warning_max_hold_ratio)))
                if take_profit_pct > 0 and result.pnl_pct >= tp_warn:
                    close_warning = True
                    close_warning_reason = "NEAR_TAKE_PROFIT"
                    close_warning_level = "TP"
                elif stop_loss_pct > 0 and result.pnl_pct <= -sl_warn:
                    close_warning = True
                    close_warning_reason = "NEAR_STOP_LOSS"
                    close_warning_level = "SL"
                elif max_hold_seconds > 0 and age_seconds >= max_hold_warn:
                    close_warning = True
                    close_warning_reason = "NEAR_MAX_HOLD"
                    close_warning_level = "TIME"

            # Hard safety rails still apply even when AI manages exits.
            if status == "OPEN" and result.pnl_pct >= take_profit_pct:
                status, reason = "CLOSED", "TAKE_PROFIT"
            elif status == "OPEN" and result.pnl_pct <= -abs(stop_loss_pct):
                status, reason = "CLOSED", "STOP_LOSS"
            elif status == "OPEN" and ts - int(r["ts_open"]) >= max_hold_seconds:
                status, reason = "CLOSED", "MAX_HOLD"

            self.conn.execute(
                """
                UPDATE virtual_trades
                SET ts_close=?, close_px=?, status=?, reason=?, pnl_pct=?, pnl_usd=?, max_favorable_pct=?, max_adverse_pct=?,
                    ai_exit_confidence=?, ai_exit_reason=?
                WHERE id=?
                """,
                (
                    ts if status == "CLOSED" else None,
                    float(current) if status == "CLOSED" else None,
                    status,
                    reason,
                    result.pnl_pct,
                    result.pnl_usd,
                    max_fav,
                    max_adv,
                    ai_exit_conf,
                    ai_exit_reason,
                    int(r["id"]),
                ),
            )
            out.append({
                "id": int(r["id"]), "coin": r["coin"], "side": r["side"], **result.__dict__,
                "status": status, "reason": reason, "mfe_pct": max_fav, "mae_pct": max_adv,
                "leverage": lev, "margin_usd": float(r["margin_usd"] or (float(r["notional_usd"]) / lev)),
                "ai_open_reason": r["ai_open_reason"], "ai_exit_confidence": ai_exit_conf, "ai_exit_reason": ai_exit_reason,
                "close_warning": close_warning, "close_warning_reason": close_warning_reason,
                "close_warning_level": close_warning_level, "age_hours": age_seconds / 3600.0,
            })
        self.conn.commit()
        return out

    def virtual_summary(self, account_capital_usd: float = 0.0) -> dict[str, Any]:
        row = self.conn.execute(
            """
            SELECT COUNT(*) AS total,
                   SUM(CASE WHEN status='OPEN' THEN 1 ELSE 0 END) AS open_count,
                   SUM(CASE WHEN status='CLOSED' THEN 1 ELSE 0 END) AS closed_count,
                   SUM(CASE WHEN status='CLOSED' AND pnl_pct>0 THEN 1 ELSE 0 END) AS wins,
                   SUM(CASE WHEN status='CLOSED' AND pnl_pct<=0 THEN 1 ELSE 0 END) AS losses,
                   AVG(CASE WHEN status='CLOSED' THEN pnl_pct END) AS avg_closed_pnl_pct,
                   COALESCE(SUM(CASE WHEN status='CLOSED' THEN pnl_usd ELSE 0 END), 0) AS realized_pnl_usd,
                   COALESCE(SUM(CASE WHEN status='OPEN' THEN pnl_usd ELSE 0 END), 0) AS unrealized_pnl_usd,
                   COALESCE(SUM(CASE WHEN status='OPEN' THEN notional_usd ELSE 0 END), 0) AS open_notional_usd,
                   COALESCE(SUM(CASE WHEN status='OPEN' THEN COALESCE(margin_usd, notional_usd / CASE WHEN COALESCE(leverage, 1) < 1 THEN 1 ELSE COALESCE(leverage, 1) END) ELSE 0 END), 0) AS open_margin_usd
            FROM virtual_trades
            """
        ).fetchone()
        if not row:
            return {}
        out = dict(row)
        capital = float(account_capital_usd or 0.0)
        realized = float(out.get("realized_pnl_usd") or 0.0)
        unrealized = float(out.get("unrealized_pnl_usd") or 0.0)
        open_notional = float(out.get("open_notional_usd") or 0.0)
        open_margin = float(out.get("open_margin_usd") or 0.0)
        out["account_capital_usd"] = capital
        out["equity_usd"] = capital + realized + unrealized if capital else realized + unrealized
        out["available_margin_usd"] = max(0.0, capital - open_margin) if capital else 0.0
        out["available_notional_usd"] = out["available_margin_usd"]
        out["used_margin_pct"] = (open_margin / capital * 100.0) if capital > 0 else 0.0
        out["used_notional_pct"] = (open_notional / capital * 100.0) if capital > 0 else 0.0
        closed = int(out.get("closed_count") or 0)
        wins = int(out.get("wins") or 0)
        out["closed_win_rate"] = wins / closed if closed > 0 else None
        return out


    def recent_active_signals_for_lifecycle(self, since_ts: int) -> list[sqlite3.Row]:
        return self.conn.execute(
            """
            SELECT * FROM signals
            WHERE status='OPEN' AND ts>=?
            ORDER BY ts DESC
            """,
            (since_ts,),
        ).fetchall()


    def recent_signal_flow_stats(self, now_ts: int, windows_seconds: list[int]) -> dict[tuple[str, str], dict[int, dict[str, Any]]]:
        """Return historical directional flow for swing-mode scoring.

        The stats are based on previously persisted open/increase signals plus their
        contributing wallets. Current-run signals are added later in signals.attach_swing_context().
        """
        if not windows_seconds:
            return {}
        min_ts = int(now_ts) - max(int(w) for w in windows_seconds)
        rows = self.conn.execute(
            """
            SELECT s.id, s.ts, s.coin, s.side, s.total_delta_notional, s.weighted_score,
                   sw.wallet, sw.wallet_group
            FROM signals s
            LEFT JOIN signal_wallets sw ON sw.signal_id=s.id
            WHERE s.ts>=? AND COALESCE(s.status,'OPEN')!='EXPIRED'
            ORDER BY s.ts DESC
            """,
            (min_ts,),
        ).fetchall()

        # Internal structure keeps sets for deduping. It is converted to plain dicts before return.
        out: dict[tuple[str, str], dict[int, dict[str, Any]]] = {}
        seen_signal_ids: set[tuple[str, str, int, int]] = set()
        for r in rows:
            coin = str(r["coin"])
            side = str(r["side"])
            key = (coin, side)
            sig_id = int(r["id"])
            sig_ts = int(r["ts"])
            for window in windows_seconds:
                if sig_ts < int(now_ts) - int(window):
                    continue
                bucket = out.setdefault(key, {}).setdefault(int(window), {
                    "total_delta_notional": 0.0,
                    "weighted_score": 0.0,
                    "signal_ids": set(),
                    "wallets": set(),
                    "smart_money_wallets": set(),
                    "money_printer_wallets": set(),
                    "last_ts": 0,
                })
                sig_marker = (coin, side, int(window), sig_id)
                if sig_marker not in seen_signal_ids:
                    seen_signal_ids.add(sig_marker)
                    bucket["signal_ids"].add(sig_id)
                    bucket["total_delta_notional"] += float(r["total_delta_notional"] or 0)
                    bucket["weighted_score"] += float(r["weighted_score"] or 0)
                    bucket["last_ts"] = max(int(bucket["last_ts"] or 0), sig_ts)
                wallet = r["wallet"]
                if wallet:
                    wallet = str(wallet)
                    bucket["wallets"].add(wallet)
                    group = str(r["wallet_group"] or "")
                    if group == "smart_money":
                        bucket["smart_money_wallets"].add(wallet)
                    elif group == "money_printer":
                        bucket["money_printer_wallets"].add(wallet)

        plain: dict[tuple[str, str], dict[int, dict[str, Any]]] = {}
        for key, by_window in out.items():
            plain[key] = {}
            for window, b in by_window.items():
                plain[key][window] = {
                    "total_delta_notional": round(float(b["total_delta_notional"]), 2),
                    "weighted_score": round(float(b["weighted_score"]), 4),
                    "signal_count": len(b["signal_ids"]),
                    "wallets": set(b["wallets"]),
                    "wallet_count": len(b["wallets"]),
                    "smart_money_wallets": set(b["smart_money_wallets"]),
                    "smart_money_wallet_count": len(b["smart_money_wallets"]),
                    "money_printer_wallets": set(b["money_printer_wallets"]),
                    "money_printer_wallet_count": len(b["money_printer_wallets"]),
                    "last_ts": int(b["last_ts"] or 0),
                }
        return plain

    def record_ai_usage(
        self,
        *,
        ts: int,
        model: str,
        purpose: str,
        usage: dict[str, Any] | None,
        estimated_points: int,
        cached: bool,
        ok: bool,
    ) -> None:
        usage = usage or {}
        self.conn.execute(
            """
            INSERT INTO ai_usage(ts,model,purpose,prompt_tokens,completion_tokens,total_tokens,estimated_points,cached,ok)
            VALUES (?,?,?,?,?,?,?,?,?)
            """,
            (
                ts,
                model,
                purpose,
                int(usage.get("prompt_tokens") or 0),
                int(usage.get("completion_tokens") or 0),
                int(usage.get("total_tokens") or 0),
                int(estimated_points or 0),
                1 if cached else 0,
                1 if ok else 0,
            ),
        )
        self.conn.commit()

    def estimated_ai_points_since(self, since_ts: int, *, include_cached: bool = False) -> int:
        if include_cached:
            row = self.conn.execute("SELECT COALESCE(SUM(estimated_points),0) AS points FROM ai_usage WHERE ts>=?", (since_ts,)).fetchone()
        else:
            row = self.conn.execute("SELECT COALESCE(SUM(estimated_points),0) AS points FROM ai_usage WHERE ts>=? AND cached=0", (since_ts,)).fetchone()
        return int(row["points"] or 0) if row else 0

    def run_health_summary(self, since_ts: int) -> dict[str, Any]:
        row = self.conn.execute(
            """
            SELECT COUNT(*) AS runs,
                   SUM(CASE WHEN ai_ok=1 THEN 1 ELSE 0 END) AS ai_ok_runs,
                   AVG(duration_sec) AS avg_duration_sec,
                   MAX(duration_sec) AS max_duration_sec,
                   SUM(signals_count) AS signals_count,
                   SUM(positions_count) AS positions_count
            FROM run_log WHERE ts>=?
            """,
            (since_ts,),
        ).fetchone()
        ai = self.conn.execute(
            """
            SELECT COUNT(*) AS calls,
                   SUM(CASE WHEN ok=1 THEN 1 ELSE 0 END) AS ok_calls,
                   SUM(estimated_points) AS estimated_points,
                   SUM(total_tokens) AS total_tokens
            FROM ai_usage WHERE ts>=? AND cached=0
            """,
            (since_ts,),
        ).fetchone()
        def val(r, key, default=0):
            if r is None:
                return default
            try:
                return r[key]
            except Exception:  # noqa: BLE001
                return default
        return {
            "runs": int(val(row, "runs") or 0),
            "ai_ok_runs": int(val(row, "ai_ok_runs") or 0),
            "avg_duration_sec": float(val(row, "avg_duration_sec") or 0),
            "max_duration_sec": float(val(row, "max_duration_sec") or 0),
            "signals_count": int(val(row, "signals_count") or 0),
            "positions_count": int(val(row, "positions_count") or 0),
            "ai_calls": int(val(ai, "calls") or 0),
            "ai_ok_calls": int(val(ai, "ok_calls") or 0),
            "ai_estimated_points": int(val(ai, "estimated_points") or 0),
            "ai_total_tokens": int(val(ai, "total_tokens") or 0),
        }

    def integrity_ok(self) -> bool:
        row = self.conn.execute("PRAGMA integrity_check").fetchone()
        return bool(row and str(row[0]).lower() == "ok")

    def backup_database(self, ts: int, keep: int = 8) -> Path | None:
        if not self.db_path.exists():
            return None
        backup_dir = self.db_path.parent / "backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        out = backup_dir / f"wallet_monitor_{ts}.sqlite3"
        dest = sqlite3.connect(out)
        try:
            self.conn.backup(dest)
        finally:
            dest.close()
        backups = sorted(backup_dir.glob("wallet_monitor_*.sqlite3"), key=lambda p: p.stat().st_mtime, reverse=True)
        for old in backups[max(1, keep):]:
            try:
                old.unlink()
            except FileNotFoundError:
                pass
        return out

    def log_run(self, **kwargs: Any) -> None:
        self.conn.execute(
            """
            INSERT OR REPLACE INTO run_log
            (ts,wallets_total,wallets_scanned,positions_count,signals_count,ai_enabled,ai_ok,duration_sec,note)
            VALUES (?,?,?,?,?,?,?,?,?)
            """,
            (
                kwargs.get("ts", int(time.time())),
                kwargs.get("wallets_total"),
                kwargs.get("wallets_scanned"),
                kwargs.get("positions_count"),
                kwargs.get("signals_count"),
                1 if kwargs.get("ai_enabled") else 0,
                1 if kwargs.get("ai_ok") else 0,
                kwargs.get("duration_sec"),
                kwargs.get("note", ""),
            ),
        )
        self.conn.commit()
