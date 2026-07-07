from __future__ import annotations

import hashlib
import json
import math
from collections import defaultdict
from dataclasses import asdict
from typing import Any

from .hyperliquid import Position
from .pnl import calc_pnl

OPEN_EVENTS = {"NEW_POSITION", "INCREASE_POSITION", "FLIP_POSITION"}
EXIT_EVENTS = {"REDUCE_POSITION", "CLOSE_POSITION"}


def build_position_deltas(
    prev_latest: dict[tuple[str, str], Any],
    current: list[Position],
    *,
    scanned_wallets: set[str] | None = None,
    baseline_wallets: set[str] | None = None,
    wallet_scores: dict[str, float] | None = None,
    wallet_performance: dict[str, dict[str, Any]] | None = None,
    wallet_perf_weight_in_signal: float = 0.25,
    warmup_missing_wallets: bool = True,
    mids: dict[str, float] | None = None,
) -> list[dict[str, Any]]:
    """Build position change events.

    Warmup behavior is intentional: when a wallet has never been observed before, its existing positions are used
    as baseline and are not emitted as NEW_POSITION. This prevents first GitHub run / first shard run from spamming
    false open signals.
    """
    deltas: list[dict[str, Any]] = []
    current_map = {(p.wallet, p.coin): p for p in current}
    scanned = scanned_wallets or {p.wallet for p in current}
    baseline = baseline_wallets if baseline_wallets is not None else scanned
    scores = wallet_scores or {}
    perf = wallet_performance or {}
    perf_weight = max(0.0, min(1.0, float(wallet_perf_weight_in_signal)))

    for p in current:
        prev = prev_latest.get((p.wallet, p.coin))
        mark = p.mark_px or p.entry_px or 0.0
        if mark <= 0:
            continue

        # Newly added / newly sharded wallet: establish baseline only.
        if prev is None and warmup_missing_wallets and p.wallet not in baseline:
            continue

        prev_size = 0.0
        prev_side = None
        if prev is not None:
            try:
                prev_size = float(prev["size"])
                prev_side = str(prev["side"])
            except Exception:  # noqa: BLE001
                prev_size = 0.0
                prev_side = None

        changed_size = 0.0
        event = "UNCHANGED"
        if prev is None:
            changed_size = abs(p.size)
            event = "NEW_POSITION"
        elif prev_side != p.side:
            changed_size = abs(p.size)
            event = "FLIP_POSITION"
        else:
            inc = abs(p.size) - abs(prev_size)
            if inc > 0:
                changed_size = inc
                event = "INCREASE_POSITION"
            elif inc < 0:
                changed_size = abs(inc)
                event = "REDUCE_POSITION"

        if event == "UNCHANGED" or changed_size <= 0:
            continue
        deltas.append(_event_dict(p, event, changed_size, mark, scores.get(p.wallet, 1.0), perf.get(p.wallet), perf_weight))

    # Positions that disappeared for scanned wallets = closed.
    for key, prev in prev_latest.items():
        wallet, coin = key
        if wallet not in scanned or key in current_map:
            continue
        try:
            prev_side = str(prev["side"])
            prev_size = abs(float(prev["size"]))
            prev_mark = _float_or_none(prev["mark_px"])
            prev_entry = _float_or_none(prev["entry_px"])
            group = str(prev["wallet_group"])
            pos_value = _float_or_none(prev["position_value"]) or 0.0
        except Exception:  # noqa: BLE001
            continue
        mark = (mids or {}).get(coin) or prev_mark or prev_entry or 0.0
        if prev_size <= 0 or mark <= 0:
            continue
        wallet_score = scores.get(wallet, 1.0)
        effective_score = 1.0 + (float(wallet_score) - 1.0) * perf_weight
        perf_row = perf.get(wallet) or {}
        deltas.append({
            "event": "CLOSE_POSITION",
            "wallet": wallet,
            "group": group,
            "weight": 1.0,
            "wallet_score": wallet_score,
            "quality_grade": perf_row.get("quality_grade") or _quality_grade_from_score(wallet_score, int(perf_row.get("trades") or 0)),
            "perf_trades": int(perf_row.get("trades") or 0),
            "win_rate_24h": _float_or_none(perf_row.get("win_rate_24h")),
            "avg_pnl_24h": _float_or_none(perf_row.get("avg_pnl_24h")),
            "trades_24h": int(perf_row.get("trades_24h") or 0),
            "win_rate_72h": _float_or_none(perf_row.get("win_rate_72h")),
            "avg_pnl_72h": _float_or_none(perf_row.get("avg_pnl_72h")),
            "trades_72h": int(perf_row.get("trades_72h") or 0),
            "win_rate_168h": _float_or_none(perf_row.get("win_rate_168h")),
            "avg_pnl_168h": _float_or_none(perf_row.get("avg_pnl_168h")),
            "trades_168h": int(perf_row.get("trades_168h") or 0),
            "profit_factor": _float_or_none(perf_row.get("profit_factor")),
            "raw_wallet_score": wallet_score,
            "effective_weight": 1.0 * effective_score,
            "coin": coin,
            "side": prev_side,
            "opened_size": 0.0,
            "changed_size": prev_size,
            "delta_notional": prev_size * mark,
            "position_value": pos_value,
            "entry_px": prev_entry,
            "mark_px": mark,
            "unrealized_pnl": _float_or_none(prev["unrealized_pnl"]),
            "roe": _float_or_none(prev["roe"]),
            "leverage": _float_or_none(prev["leverage"]),
        })
    return deltas


def _event_dict(p: Position, event: str, changed_size: float, mark: float, wallet_score: float, perf_row: dict[str, Any] | None = None, perf_weight: float = 0.25) -> dict[str, Any]:
    perf_row = perf_row or {}
    trades = int(perf_row.get("trades") or 0)
    effective_score = 1.0 + (float(wallet_score) - 1.0) * max(0.0, min(1.0, float(perf_weight)))
    return {
        "event": event,
        "wallet": p.wallet,
        "group": p.group,
        "weight": p.weight,
        "wallet_score": wallet_score,
        "quality_grade": perf_row.get("quality_grade") or _quality_grade_from_score(wallet_score, trades),
        "perf_trades": trades,
        "win_rate_24h": _float_or_none(perf_row.get("win_rate_24h")),
        "avg_pnl_24h": _float_or_none(perf_row.get("avg_pnl_24h")),
        "trades_24h": int(perf_row.get("trades_24h") or 0),
        "win_rate_72h": _float_or_none(perf_row.get("win_rate_72h")),
        "avg_pnl_72h": _float_or_none(perf_row.get("avg_pnl_72h")),
        "trades_72h": int(perf_row.get("trades_72h") or 0),
        "win_rate_168h": _float_or_none(perf_row.get("win_rate_168h")),
        "avg_pnl_168h": _float_or_none(perf_row.get("avg_pnl_168h")),
        "trades_168h": int(perf_row.get("trades_168h") or 0),
        "profit_factor": _float_or_none(perf_row.get("profit_factor")),
        "raw_wallet_score": wallet_score,
        "effective_weight": p.weight * effective_score,
        "coin": p.coin,
        "side": p.side,
        "opened_size": changed_size if event in OPEN_EVENTS else 0.0,
        "changed_size": changed_size,
        "delta_notional": changed_size * mark,
        "position_value": p.position_value,
        "entry_px": p.entry_px,
        "mark_px": mark,
        "unrealized_pnl": p.unrealized_pnl,
        "roe": p.roe,
        "leverage": p.leverage,
    }

def aggregate_signals(
    deltas: list[dict[str, Any]],
    *,
    min_delta_notional_usd: float,
    min_single_whale_delta_usd: float,
    min_wallet_count: int,
    top_n: int = 8,
) -> list[dict[str, Any]]:
    buckets: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for d in deltas:
        if d.get("event") not in OPEN_EVENTS:
            continue
        if d["delta_notional"] >= min_delta_notional_usd:
            buckets[(d["coin"], d["side"])].append(d)

    out = [_bucket_to_signal(coin, side, items, min_single_whale_delta_usd, min_wallet_count) for (coin, side), items in buckets.items()]
    out = [s for s in out if s is not None]
    _attach_conflict_fields(out)
    out.sort(key=lambda x: (x["net_bias_score"], x["weighted_score"], x["total_delta_notional"], x["wallet_count"]), reverse=True)
    return out[:top_n]


def aggregate_exit_events(
    deltas: list[dict[str, Any]],
    *,
    min_delta_notional_usd: float,
    top_n: int = 8,
) -> list[dict[str, Any]]:
    buckets: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for d in deltas:
        if d.get("event") not in EXIT_EVENTS:
            continue
        if d["delta_notional"] >= min_delta_notional_usd:
            buckets[(d["coin"], d["side"])].append(d)
    out: list[dict[str, Any]] = []
    for (coin, side), items in buckets.items():
        total_delta = sum(float(x["delta_notional"]) for x in items)
        wallet_count = len({x["wallet"] for x in items})
        groups: dict[str, int] = defaultdict(int)
        for x in items:
            groups[x.get("group") or "unknown"] += 1
        out.append({
            "coin": coin,
            "side": side,
            "direction": "EXIT_LONG" if side == "LONG" else "EXIT_SHORT",
            "wallet_count": wallet_count,
            "groups": dict(groups),
            "total_delta_notional": round(total_delta, 2),
            "max_wallet_delta_notional": round(max(float(x["delta_notional"]) for x in items), 2),
            "weighted_score": round(_weighted_score(items), 4),
            "mark_px": _weighted_average([x.get("mark_px") for x in items]),
            "wallets": sorted(items, key=lambda x: x["delta_notional"], reverse=True)[:10],
        })
    out.sort(key=lambda x: (x["weighted_score"], x["total_delta_notional"]), reverse=True)
    return out[:top_n]


def _bucket_to_signal(coin: str, side: str, items: list[dict[str, Any]], min_single_whale_delta_usd: float, min_wallet_count: int) -> dict[str, Any] | None:
    wallet_count = len({x["wallet"] for x in items})
    total_delta = sum(float(x["delta_notional"]) for x in items)
    max_delta = max(float(x["delta_notional"]) for x in items)
    if wallet_count < min_wallet_count and max_delta < min_single_whale_delta_usd:
        return None
    total_position_value = sum(float(x.get("position_value") or 0) for x in items)
    entries = [float(x["entry_px"]) for x in items if x.get("entry_px")]
    marks = [float(x["mark_px"]) for x in items if x.get("mark_px")]
    groups: dict[str, int] = defaultdict(int)
    events: dict[str, int] = defaultdict(int)
    for x in items:
        groups[x.get("group") or "unknown"] += 1
        events[x.get("event") or "unknown"] += 1
    weighted_score = _weighted_score(items)
    quality = _wallet_quality_summary(items)
    direction = "OPEN_LONG" if side == "LONG" else "OPEN_SHORT"
    return {
        "coin": coin,
        "side": side,
        "direction": direction,
        "wallet_count": wallet_count,
        "groups": dict(groups),
        "events": dict(events),
        "total_delta_notional": round(total_delta, 2),
        "max_wallet_delta_notional": round(max_delta, 2),
        "total_position_value": round(total_position_value, 2),
        "weighted_score": round(weighted_score, 4),
        "net_bias_score": round(weighted_score, 4),
        "wallet_quality": quality,
        "wallet_quality_score": quality.get("score"),
        "high_quality_wallet_count": quality.get("high_quality_wallet_count"),
        "low_quality_wallet_count": quality.get("low_quality_wallet_count"),
        "avg_wallet_score": quality.get("avg_wallet_score"),
        "weighted_win_rate_72h": quality.get("weighted_win_rate_72h"),
        "weighted_win_rate_168h": quality.get("weighted_win_rate_168h"),
        "opposite_delta_notional": 0.0,
        "opposite_wallet_count": 0,
        "conflict_ratio": 0.0,
        "avg_entry_px": round(sum(entries) / len(entries), 8) if entries else None,
        "mark_px": round(sum(marks) / len(marks), 8) if marks else None,
        "wallets": sorted(items, key=lambda x: x["delta_notional"], reverse=True)[:10],
        "status": "OPEN",
    }


def _weighted_score(items: list[dict[str, Any]]) -> float:
    return sum(
        float(x.get("effective_weight") or x.get("weight") or 1) * math.log10(max(float(x["delta_notional"]), 1.0))
        for x in items
    )



def _wallet_quality_summary(items: list[dict[str, Any]]) -> dict[str, Any]:
    if not items:
        return {
            "score": 50.0,
            "avg_wallet_score": 1.0,
            "high_quality_wallet_count": 0,
            "low_quality_wallet_count": 0,
            "sampled_wallet_count": 0,
        }
    seen: dict[str, dict[str, Any]] = {}
    for x in items:
        wallet = str(x.get("wallet") or "")
        if wallet and wallet not in seen:
            seen[wallet] = x
    wallets = list(seen.values())
    scores = [float(w.get("wallet_score") or 1.0) for w in wallets]
    avg_score = sum(scores) / max(len(scores), 1)
    high = sum(1 for w in wallets if float(w.get("wallet_score") or 1.0) >= 1.25 or str(w.get("quality_grade") or "") in {"S", "A"})
    low = sum(1 for w in wallets if float(w.get("wallet_score") or 1.0) <= 0.75 or str(w.get("quality_grade") or "") == "D")
    sampled = sum(1 for w in wallets if int(w.get("perf_trades") or 0) > 0)
    total_delta = sum(float(w.get("delta_notional") or 0) for w in wallets)
    wr72 = _weighted_metric(wallets, "win_rate_72h")
    wr168 = _weighted_metric(wallets, "win_rate_168h")
    avg72 = _weighted_metric(wallets, "avg_pnl_72h")
    avg168 = _weighted_metric(wallets, "avg_pnl_168h")

    # Convert wallet score to a human 0-100 quality rating. Unsampled wallets stay near neutral.
    base = 50.0 + (avg_score - 1.0) * 35.0
    base += min(15.0, high * 4.0)
    base -= min(15.0, low * 5.0)
    if wr72 is not None:
        base += (float(wr72) - 0.5) * 18.0
    if avg72 is not None:
        base += max(-8.0, min(8.0, float(avg72) / 2.0))
    if sampled < max(2, len(wallets) // 2):
        base = 50.0 + (base - 50.0) * 0.65
    return {
        "score": round(max(0.0, min(100.0, base)), 2),
        "avg_wallet_score": round(avg_score, 4),
        "high_quality_wallet_count": high,
        "low_quality_wallet_count": low,
        "sampled_wallet_count": sampled,
        "wallet_count": len(wallets),
        "weighted_win_rate_72h": None if wr72 is None else round(float(wr72), 4),
        "weighted_win_rate_168h": None if wr168 is None else round(float(wr168), 4),
        "weighted_avg_pnl_72h": None if avg72 is None else round(float(avg72), 4),
        "weighted_avg_pnl_168h": None if avg168 is None else round(float(avg168), 4),
        "total_delta_notional": round(total_delta, 2),
    }


def _weighted_metric(items: list[dict[str, Any]], key: str) -> float | None:
    num = 0.0
    den = 0.0
    for w in items:
        val = _float_or_none(w.get(key))
        if val is None:
            continue
        weight = max(float(w.get("delta_notional") or 0), 1.0)
        num += val * weight
        den += weight
    if den <= 0:
        return None
    return num / den


def _quality_grade_from_score(score: float, trades: int = 0) -> str:
    if trades <= 0:
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


def _attach_conflict_fields(signals: list[dict[str, Any]]) -> None:
    by_coin: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for s in signals:
        by_coin[str(s["coin"])].append(s)
    for coin_signals in by_coin.values():
        if len(coin_signals) < 2:
            continue
        for s in coin_signals:
            opponents = [x for x in coin_signals if x["side"] != s["side"]]
            opposite_delta = sum(float(x["total_delta_notional"]) for x in opponents)
            opposite_wallets = sum(int(x["wallet_count"]) for x in opponents)
            this_delta = max(float(s["total_delta_notional"]), 1.0)
            ratio = opposite_delta / this_delta
            s["opposite_delta_notional"] = round(opposite_delta, 2)
            s["opposite_wallet_count"] = opposite_wallets
            s["conflict_ratio"] = round(ratio, 4)
            s["net_bias_score"] = round(float(s["weighted_score"]) * max(0.25, 1.0 - min(ratio, 1.0) * 0.75), 4)
            if ratio >= 0.65:
                s["conflict_level"] = "HIGH"
            elif ratio >= 0.25:
                s["conflict_level"] = "MEDIUM"
            else:
                s["conflict_level"] = "LOW"


def attach_market_context(
    signals: list[dict[str, Any]],
    asset_ctxs: dict[str, dict[str, Any]],
    candle_ctxs: dict[str, dict[str, list[dict[str, Any]]]] | None = None,
) -> None:
    candle_ctxs = candle_ctxs or {}
    for s in signals:
        ctx = asset_ctxs.get(s["coin"], {})
        funding = _float_or_none(ctx.get("funding"))
        oi = _float_or_none(ctx.get("openInterest"))
        oracle = _float_or_none(ctx.get("oraclePx"))
        mark = _float_or_none(ctx.get("markPx"))
        premium = _float_or_none(ctx.get("premium"))
        candle_metrics = _market_candle_metrics(candle_ctxs.get(str(s["coin"]), {}))
        s["market"] = {
            "funding": funding,
            "open_interest": oi,
            "oracle_px": oracle,
            "mark_px_ctx": mark,
            "premium": premium,
            **candle_metrics,
        }
        # Simple risk tags for AI and report; do not overfit.
        tags: list[str] = []
        if funding is not None:
            if s.get("side") == "LONG" and funding > 0.0003:
                tags.append("long_crowded_funding")
            if s.get("side") == "SHORT" and funding < -0.0003:
                tags.append("short_crowded_funding")
        if s.get("conflict_level") == "HIGH":
            tags.append("high_long_short_conflict")
        m15 = candle_metrics.get("m15") or {}
        h1 = candle_metrics.get("h1") or {}
        try:
            m15_ret = float(m15.get("return_pct") or 0)
            h1_ret = float(h1.get("return_pct") or 0)
            m15_vol = float(m15.get("volume_ratio") or 1)
            wick_up = float(m15.get("upper_wick_ratio") or 0)
            wick_down = float(m15.get("lower_wick_ratio") or 0)
            if s.get("side") == "LONG" and (m15_ret > 4.0 or h1_ret > 8.0):
                tags.append("long_chasing_pump")
            if s.get("side") == "SHORT" and (m15_ret < -4.0 or h1_ret < -8.0):
                tags.append("short_chasing_dump")
            if m15_vol >= 2.0:
                tags.append("volume_expansion")
            if s.get("side") == "LONG" and wick_up >= 0.45:
                tags.append("long_upper_wick_risk")
            if s.get("side") == "SHORT" and wick_down >= 0.45:
                tags.append("short_lower_wick_risk")
        except (TypeError, ValueError):
            pass
        s["risk_tags"] = sorted(set(tags))


def _market_candle_metrics(intervals: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    alias = {"5m": "m5", "15m": "m15", "1h": "h1", "4h": "h4"}
    for interval, candles in (intervals or {}).items():
        key = alias.get(interval, interval.replace(" ", "_"))
        metrics = _one_interval_metrics(candles)
        if metrics:
            out[key] = metrics
    return out


def _one_interval_metrics(candles: list[dict[str, Any]]) -> dict[str, Any]:
    clean = []
    for c in candles or []:
        if not isinstance(c, dict):
            continue
        o = _float_or_none(c.get("o") or c.get("open"))
        h = _float_or_none(c.get("h") or c.get("high"))
        l = _float_or_none(c.get("l") or c.get("low"))
        close = _float_or_none(c.get("c") or c.get("close"))
        v = _float_or_none(c.get("v") or c.get("volume"))
        if o and h and l and close:
            clean.append({"o": o, "h": h, "l": l, "c": close, "v": v or 0.0})
    if len(clean) < 2:
        return {}
    first = clean[0]
    last = clean[-1]
    if first["o"] <= 0:
        return {}
    ret = (last["c"] - first["o"]) / first["o"] * 100.0
    high = max(x["h"] for x in clean)
    low = min(x["l"] for x in clean)
    rng = max(high - low, 1e-12)
    body_high = max(last["o"], last["c"])
    body_low = min(last["o"], last["c"])
    upper_wick = max(0.0, last["h"] - body_high) / max(last["h"] - last["l"], 1e-12)
    lower_wick = max(0.0, body_low - last["l"]) / max(last["h"] - last["l"], 1e-12)
    vols = [float(x["v"] or 0) for x in clean]
    recent_vol = sum(vols[-3:]) / max(len(vols[-3:]), 1)
    base_vol = sum(vols[:-3]) / max(len(vols[:-3]), 1) if len(vols) > 3 else sum(vols) / len(vols)
    volume_ratio = recent_vol / max(base_vol, 1e-9) if base_vol else 0.0
    return {
        "return_pct": round(ret, 4),
        "range_pct": round((high - low) / first["o"] * 100.0, 4),
        "volume_ratio": round(volume_ratio, 4),
        "upper_wick_ratio": round(upper_wick, 4),
        "lower_wick_ratio": round(lower_wick, 4),
        "last_close": round(last["c"], 8),
    }


def apply_signal_lifecycle(
    signals: list[dict[str, Any]],
    exit_events: list[dict[str, Any]],
    *,
    recent_active: list[Any],
    now_ts: int,
    cooldown_seconds: int,
    realert_multiplier: float,
    exit_decay_ratio: float,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Merge/cooldown duplicate signals and tag exit pressure against active signals."""
    active_by_key: dict[tuple[str, str], Any] = {}
    for row in recent_active or []:
        active_by_key[(str(row["coin"]), str(row["side"]))] = row
    kept: list[dict[str, Any]] = []
    lifecycle: list[dict[str, Any]] = []
    for s in signals:
        key = (str(s.get("coin")), str(s.get("side")))
        prev = active_by_key.get(key)
        if prev is None or cooldown_seconds <= 0:
            kept.append(s)
            continue
        age = now_ts - int(prev["ts"])
        prev_delta = max(float(prev["total_delta_notional"] or 0), 1.0)
        this_delta = float(s.get("total_delta_notional") or 0)
        if age < cooldown_seconds and this_delta < prev_delta * max(1.0, realert_multiplier):
            s.setdefault("risk_tags", []).append("cooldown_merged_duplicate")
            s["suppressed_by_signal_id"] = int(prev["id"])
            lifecycle.append({
                "event": "COOLDOWN_MERGED",
                "coin": key[0],
                "side": key[1],
                "direction": s.get("direction"),
                "amount": round(this_delta, 2),
                "previous_signal_id": int(prev["id"]),
                "previous_amount": round(prev_delta, 2),
                "age_minutes": round(age / 60.0, 1),
            })
            continue
        if age < cooldown_seconds:
            s.setdefault("risk_tags", []).append("cooldown_realert_large_add")
        kept.append(s)

    exit_by_key = {(str(e.get("coin")), str(e.get("side"))): e for e in exit_events or []}
    for key, prev in active_by_key.items():
        ex = exit_by_key.get(key)
        if not ex:
            continue
        prev_delta = max(float(prev["total_delta_notional"] or 0), 1.0)
        exit_delta = float(ex.get("total_delta_notional") or 0)
        ratio = exit_delta / prev_delta
        if ratio >= exit_decay_ratio:
            lifecycle.append({
                "event": "ACTIVE_SIGNAL_DECAY",
                "coin": key[0],
                "side": key[1],
                "direction": "EXIT_LONG" if key[1] == "LONG" else "EXIT_SHORT",
                "amount": round(exit_delta, 2),
                "previous_signal_id": int(prev["id"]),
                "previous_amount": round(prev_delta, 2),
                "exit_ratio": round(ratio, 4),
            })
    return kept, lifecycle


def filter_signals_for_ai(
    signals: list[dict[str, Any]],
    *,
    min_total_delta: float,
    min_wallet_count: int,
    min_weighted_score: float,
    top_n: int,
) -> list[dict[str, Any]]:
    out = []
    for s in signals:
        swing = s.get("swing") or {}
        swing_score = float(swing.get("score") or s.get("swing_score") or 0)
        if swing_score >= float(s.get("swing_min_score_for_ai") or 60):
            out.append(s)
            continue
        if float(s.get("total_delta_notional") or 0) >= min_total_delta:
            out.append(s)
            continue
        if int(s.get("wallet_count") or 0) >= min_wallet_count and float(s.get("weighted_score") or 0) >= min_weighted_score:
            out.append(s)
            continue
        if (s.get("groups") or {}).get("money_printer"):
            out.append(s)
    out.sort(key=lambda x: (float((x.get("swing") or {}).get("score") or 0), float(x.get("net_bias_score") or 0), float(x.get("total_delta_notional") or 0)), reverse=True)
    return out[:top_n]


def ai_cache_key(signals: list[dict[str, Any]], model: str) -> str:
    compact = []
    for s in signals:
        compact.append({
            "coin": s.get("coin"),
            "direction": s.get("direction"),
            "wallet_count": s.get("wallet_count"),
            "groups": s.get("groups"),
            "events": s.get("events"),
            "total_delta_notional_bucket": round(float(s.get("total_delta_notional") or 0) / 10000),
            "weighted_score_bucket": round(float(s.get("weighted_score") or 0), 1),
            "conflict_level": s.get("conflict_level"),
            "funding": round(float((s.get("market") or {}).get("funding") or 0), 6),
            "m15_return": round(float(((s.get("market") or {}).get("m15") or {}).get("return_pct") or 0), 2),
            "h1_return": round(float(((s.get("market") or {}).get("h1") or {}).get("return_pct") or 0), 2),
            "risk_tags": sorted(s.get("risk_tags") or []),
            "wallet_quality": s.get("wallet_quality"),
            "wallet_fingerprint": sorted(
                (
                    str(w.get("wallet") or ""),
                    str(w.get("event") or ""),
                    round(float(w.get("delta_notional") or 0) / 10000),
                )
                for w in (s.get("wallets") or [])[:5]
            ),
        })
    raw = json.dumps({"model": model, "signals": compact}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def update_open_signal_pnls(
    open_signals: list[Any],
    mids: dict[str, float],
    leverage: float,
    *,
    fee_bps: float = 0.0,
    slippage_bps: float = 0.0,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    cost_pct = (fee_bps + slippage_bps) / 100.0
    for r in open_signals:
        coin = r["coin"]
        mark = mids.get(coin)
        entry = r["mark_px"] or r["avg_entry_px"]
        if mark is None or entry is None:
            continue
        try:
            result = calc_pnl(r["side"], float(entry), float(mark), leverage=leverage, notional_usd=r["total_delta_notional"])
        except Exception:  # noqa: BLE001
            continue
        conservative_pct = result.pnl_pct - cost_pct
        conservative_usd = None if result.notional_usd is None else result.notional_usd * (conservative_pct / 100.0)
        rows.append({
            "signal_id": r["id"],
            "coin": coin,
            **asdict(result),
            "conservative_pnl_pct": conservative_pct,
            "conservative_pnl_usd": conservative_usd,
        })
    return rows


def _weighted_average(values: list[Any]) -> float | None:
    nums = [float(v) for v in values if v is not None]
    return round(sum(nums) / len(nums), 8) if nums else None


def _float_or_none(v: Any) -> float | None:
    try:
        if v is None or v == "":
            return None
        return float(v)
    except (TypeError, ValueError):
        return None


def attach_swing_context(
    signals: list[dict[str, Any]],
    historical_flow: dict[tuple[str, str], dict[int, dict[str, Any]]],
    *,
    windows_hours: list[int],
    min_score_for_ai: float = 60.0,
    watch_score: float = 65.0,
    strong_score: float = 80.0,
    horizon_days: str = "3-14",
) -> None:
    """Attach medium/long-term contract signal context.

    The goal is not to react to every wallet event. It scores whether the coin looks
    like a 3-14 day futures candidate based on repeated directional accumulation,
    wallet resonance, money_printer participation, price extension, funding, and
    long/short conflict.
    """
    if not signals:
        return
    windows_seconds = [int(h) * 3600 for h in windows_hours if int(h) > 0]
    if not windows_seconds:
        windows_seconds = [2 * 3600, 6 * 3600, 24 * 3600]
        windows_hours = [2, 6, 24]

    for s in signals:
        coin = str(s.get("coin"))
        side = str(s.get("side"))
        current_wallets = {str(w.get("wallet")) for w in (s.get("wallets") or []) if w.get("wallet")}
        current_smart = {str(w.get("wallet")) for w in (s.get("wallets") or []) if w.get("wallet") and w.get("group") == "smart_money"}
        current_money = {str(w.get("wallet")) for w in (s.get("wallets") or []) if w.get("wallet") and w.get("group") == "money_printer"}

        flow: dict[str, dict[str, Any]] = {}
        for h in windows_hours:
            sec = int(h) * 3600
            hist = (historical_flow.get((coin, side), {}) or {}).get(sec, {}) or {}
            wallets = set(hist.get("wallets") or set()) | current_wallets
            smart = set(hist.get("smart_money_wallets") or set()) | current_smart
            money = set(hist.get("money_printer_wallets") or set()) | current_money
            flow[f"{h}h"] = {
                "total_delta_notional": round(float(hist.get("total_delta_notional") or 0) + float(s.get("total_delta_notional") or 0), 2),
                "wallet_count": len(wallets),
                "smart_money_wallet_count": len(smart),
                "money_printer_wallet_count": len(money),
                "signal_count": int(hist.get("signal_count") or 0) + 1,
                "weighted_score": round(float(hist.get("weighted_score") or 0) + float(s.get("weighted_score") or 0), 4),
                "last_ts": hist.get("last_ts"),
            }

        # Direction dominance versus opposite historical/current flow.
        opposite_side = "SHORT" if side == "LONG" else "LONG"
        dominance: dict[str, float] = {}
        for h in windows_hours:
            sec = int(h) * 3600
            same = float(flow[f"{h}h"]["total_delta_notional"] or 0)
            opp_hist = (historical_flow.get((coin, opposite_side), {}) or {}).get(sec, {}) or {}
            opp = float(opp_hist.get("total_delta_notional") or 0)
            if s.get("opposite_delta_notional") and h <= 2:
                opp += float(s.get("opposite_delta_notional") or 0)
            dominance[f"{h}h"] = round(same / max(same + opp, 1.0), 4)

        score_parts = _swing_score_parts(s, flow, dominance)
        score = round(min(100.0, sum(score_parts.values())), 2)
        if score >= strong_score:
            bucket = "STRONG_CANDIDATE"
        elif score >= watch_score:
            bucket = "WATCHLIST_CANDIDATE"
        else:
            bucket = "WEAK_OR_SHORT_TERM"

        swing_tags = []
        if score >= strong_score:
            swing_tags.append("swing_strong")
        elif score >= watch_score:
            swing_tags.append("swing_watch")
        if flow.get("24h", {}).get("signal_count", 0) >= 3:
            swing_tags.append("multi_round_accumulation")
        if flow.get("24h", {}).get("money_printer_wallet_count", 0) >= 1:
            swing_tags.append("money_printer_confirmed")
        if min(dominance.values() or [1.0]) < 0.58:
            swing_tags.append("direction_conflict")
        if "long_chasing_pump" in (s.get("risk_tags") or []) or "short_chasing_dump" in (s.get("risk_tags") or []):
            swing_tags.append("price_extended_wait_pullback")

        s["swing_score"] = score
        s["swing_min_score_for_ai"] = float(min_score_for_ai)
        s["swing_bucket"] = bucket
        s["swing_horizon_days"] = horizon_days
        s["swing"] = {
            "score": score,
            "bucket": bucket,
            "score_parts": {k: round(v, 2) for k, v in score_parts.items()},
            "horizon_days": horizon_days,
            "flow": flow,
            "direction_dominance": dominance,
            "suggested_style": "medium_long_contract",
            "decision_hint": "OPEN_CANDIDATE" if score >= strong_score else "WATCH_CANDIDATE" if score >= watch_score else "FILTER_OR_WAIT",
        }
        s.setdefault("risk_tags", [])
        s["risk_tags"] = sorted(set([*s.get("risk_tags", []), *swing_tags]))


def _swing_score_parts(s: dict[str, Any], flow: dict[str, dict[str, Any]], dominance: dict[str, float]) -> dict[str, float]:
    f2 = flow.get("2h", {})
    f6 = flow.get("6h", {})
    f24 = flow.get("24h", {})
    wallet_count_24h = int(f24.get("wallet_count") or s.get("wallet_count") or 0)
    money_count_24h = int(f24.get("money_printer_wallet_count") or 0)
    signal_count_24h = int(f24.get("signal_count") or 1)
    total_2h = float(f2.get("total_delta_notional") or 0)
    total_6h = float(f6.get("total_delta_notional") or total_2h)
    total_24h = float(f24.get("total_delta_notional") or total_6h)

    wallet_resonance = min(23.0, wallet_count_24h / 6.0 * 23.0)
    accumulation = 0.0
    if total_2h >= 50_000:
        accumulation += 6.0
    if total_6h >= max(total_2h, 1.0) and total_6h >= 100_000:
        accumulation += 7.0
    if total_24h >= max(total_6h, 1.0) and total_24h >= 200_000:
        accumulation += 7.0
    accumulation += min(5.0, max(0, signal_count_24h - 1) * 2.5)
    accumulation = min(25.0, accumulation)

    money_printer = min(12.0, money_count_24h * 6.0)
    wallet_quality = _wallet_quality_score_part(s)
    price_health = min(13.0, _price_health_score(s))
    oi_funding = _oi_funding_score(s)
    conflict = min(10.0, max(0.0, (float(dominance.get("24h") or 1.0) - 0.5) / 0.5 * 10.0))
    if s.get("conflict_level") == "HIGH":
        conflict = min(conflict, 2.5)
    elif s.get("conflict_level") == "MEDIUM":
        conflict = min(conflict, 6.5)

    return {
        "wallet_resonance": wallet_resonance,
        "wallet_quality": wallet_quality,
        "multi_window_accumulation": accumulation,
        "money_printer_weight": money_printer,
        "price_position_health": price_health,
        "oi_funding_health": oi_funding,
        "low_direction_conflict": conflict,
    }



def _wallet_quality_score_part(s: dict[str, Any]) -> float:
    q = s.get("wallet_quality") or {}
    try:
        score = float(q.get("score") or 50.0)
    except (TypeError, ValueError):
        score = 50.0
    sampled = int(q.get("sampled_wallet_count") or 0)
    # 0-10: unsampled groups are neutral; proven groups can boost or penalize.
    part = 5.0 + (score - 50.0) / 50.0 * 5.0
    if sampled <= 0:
        part = 5.0
    return max(0.0, min(10.0, part))


def _price_health_score(s: dict[str, Any]) -> float:
    market = s.get("market") or {}
    m15 = market.get("m15") or {}
    h1 = market.get("h1") or {}
    try:
        m15_ret = float(m15.get("return_pct") or 0)
        h1_ret = float(h1.get("return_pct") or 0)
        m15_vol = float(m15.get("volume_ratio") or 1)
    except (TypeError, ValueError):
        return 10.0
    side = s.get("side")
    score = 15.0
    if side == "LONG":
        if m15_ret > 4 or h1_ret > 8:
            score -= 7
        elif m15_ret > 2.5 or h1_ret > 5:
            score -= 3
    else:
        if m15_ret < -4 or h1_ret < -8:
            score -= 7
        elif m15_ret < -2.5 or h1_ret < -5:
            score -= 3
    if m15_vol >= 2.5:
        score += 1.5
    return max(0.0, min(15.0, score))


def _oi_funding_score(s: dict[str, Any]) -> float:
    market = s.get("market") or {}
    funding = _float_or_none(market.get("funding"))
    score = 7.0
    if funding is None:
        return score
    side = s.get("side")
    if side == "LONG":
        if funding <= 0:
            score += 3
        elif funding < 0.00025:
            score += 2
        elif funding > 0.0006:
            score -= 4
    else:
        if funding >= 0:
            score += 3
        elif funding > -0.00025:
            score += 2
        elif funding < -0.0006:
            score -= 4
    return max(0.0, min(10.0, score))
