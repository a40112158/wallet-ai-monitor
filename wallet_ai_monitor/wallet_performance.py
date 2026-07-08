"""钱包表现真实回测：1h K 线，事件后 24h/72h/168h 判断方向对错。"""
from __future__ import annotations

import time

from .config import Config
from .market_data import fetch_candles

WINDOWS = {"24h": 86400, "72h": 259200, "168h": 604800}


def record_events(all_events: dict[str, list[dict]], market: dict,
                  wallet_perf: dict, now: float | None = None) -> None:
    now = now or time.time()
    for addr, events in all_events.items():
        rec = wallet_perf.setdefault(addr, {"events": [], "stats": {}})
        for ev in events:
            if ev["kind"] not in ("NEW", "ADD"):
                continue
            mark = market.get(ev["coin"], {}).get("mark", 0)
            if mark <= 0:
                continue
            rec["events"].append({"coin": ev["coin"], "side": ev["side"],
                                  "px": mark, "ts": now})
        cutoff = now - (WINDOWS["168h"] + 86400)
        rec["events"] = [e for e in rec["events"] if e["ts"] >= cutoff][-200:]


def _build_candle_cache(wallet_perf: dict, cfg: Config, now: float) -> dict[str, list]:
    coins: dict[str, float] = {}
    for rec in wallet_perf.values():
        for e in rec["events"]:
            coins[e["coin"]] = min(coins.get(e["coin"], now), e["ts"])
    cache: dict[str, list] = {}
    for coin, earliest in coins.items():
        start_ms = int((earliest - 3600) * 1000)
        end_ms = int(now * 1000)
        candles = fetch_candles(coin, "1h", start_ms, end_ms, cfg)
        series = []
        for c in candles:
            try:
                series.append((int(c["t"]), float(c["c"])))
            except (KeyError, TypeError, ValueError):
                continue
        series.sort()
        cache[coin] = series
    return cache


def _price_at(series: list, ts_sec: float) -> float | None:
    target = ts_sec * 1000
    best = None
    for t, c in series:
        if t <= target:
            best = c
        else:
            break
    return best


def resolve_and_score(wallet_perf: dict, cfg: Config,
                      now: float | None = None) -> dict[str, float]:
    now = now or time.time()
    cache = _build_candle_cache(wallet_perf, cfg, now)
    quality: dict[str, float] = {}

    for addr, rec in wallet_perf.items():
        win_stat = {w: {"win": 0, "loss": 0, "ret": 0.0} for w in WINDOWS}
        for e in rec["events"]:
            series = cache.get(e["coin"], [])
            entry = e["px"]
            if entry <= 0:
                continue
            for w, sec in WINDOWS.items():
                if now - e["ts"] < sec:
                    continue
                px = _price_at(series, e["ts"] + sec)
                if not px:
                    continue
                move = (px - entry) / entry
                if e["side"] == "SHORT":
                    move = -move
                win_stat[w]["ret"] += move
                if move > 0:
                    win_stat[w]["win"] += 1
                else:
                    win_stat[w]["loss"] += 1

        stats_windows = {}
        q_parts = []
        total_n = 0
        for w in WINDOWS:
            n = win_stat[w]["win"] + win_stat[w]["loss"]
            wr = win_stat[w]["win"] / n if n else 0.0
            ar = win_stat[w]["ret"] / n if n else 0.0
            stats_windows[w] = {"samples": n, "win_rate": round(wr, 3),
                                "avg_return": round(ar, 4)}
            if n >= 2:
                q_parts.append(0.5 + (wr - 0.5) * 0.8 + ar * 2)
                total_n += n
        q = max(0.0, min(1.0, sum(q_parts) / len(q_parts))) if q_parts else 0.5
        rec["stats"] = {"windows": stats_windows, "quality": round(q, 3),
                        "total_samples": total_n}
        quality[addr] = q

    return quality
