"""持仓 diff -> 事件 -> 聚合信号 -> 噪音过滤。"""
from __future__ import annotations

from .config import Config


def diff_positions(prev: dict, curr: dict) -> list[dict]:
    events: list[dict] = []
    coins = set(prev) | set(curr)
    for coin in coins:
        p = prev.get(coin)
        c = curr.get(coin)
        if c and not p:
            events.append({"kind": "NEW", "coin": coin, "side": c["side"],
                           "delta_notional": c["notional"], "entry_px": c["entry_px"]})
        elif p and not c:
            events.append({"kind": "CLOSE", "coin": coin, "side": p["side"],
                           "delta_notional": p["notional"], "entry_px": p["entry_px"]})
        elif p and c:
            if p["side"] != c["side"]:
                events.append({"kind": "CLOSE", "coin": coin, "side": p["side"],
                               "delta_notional": p["notional"], "entry_px": p["entry_px"]})
                events.append({"kind": "NEW", "coin": coin, "side": c["side"],
                               "delta_notional": c["notional"], "entry_px": c["entry_px"]})
            else:
                dsz = abs(c["szi"]) - abs(p["szi"])
                if abs(p["szi"]) > 0 and abs(dsz) / abs(p["szi"]) < 1e-6:
                    continue
                px = c["entry_px"] or p["entry_px"]
                delta_notional = abs(dsz) * px
                kind = "ADD" if dsz > 0 else "REDUCE"
                events.append({"kind": kind, "coin": coin, "side": c["side"],
                               "delta_notional": delta_notional,
                               "entry_px": c["entry_px"]})
    return events


def build_signals(all_events: dict[str, list[dict]], wallets_meta: dict,
                  wallet_quality: dict, cfg: Config) -> list[dict]:
    agg: dict[str, dict] = {}
    for addr, events in all_events.items():
        for ev in events:
            coin = ev["coin"]
            side = ev["side"]
            kind = ev["kind"]
            dn = ev["delta_notional"]
            bullish = (kind in ("NEW", "ADD") and side == "LONG") or \
                      (kind in ("REDUCE", "CLOSE") and side == "SHORT")
            bearish = (kind in ("NEW", "ADD") and side == "SHORT") or \
                      (kind in ("REDUCE", "CLOSE") and side == "LONG")
            c = agg.setdefault(coin, {"bull": {}, "bear": {}})
            if bullish:
                c["bull"][addr] = c["bull"].get(addr, 0.0) + dn
            elif bearish:
                c["bear"][addr] = c["bear"].get(addr, 0.0) + dn

    signals: list[dict] = []
    for coin, c in agg.items():
        bull = sum(c["bull"].values())
        bear = sum(c["bear"].values())
        if bull >= bear:
            direction, contrib, conflict = "OPEN_LONG", c["bull"], bear
        else:
            direction, contrib, conflict = "OPEN_SHORT", c["bear"], bull
        delta = sum(contrib.values())
        if delta <= 0:
            continue
        quals = [wallet_quality.get(a, 0.5) for a in contrib]
        groups = sorted({g for a in contrib for g in wallets_meta.get(a, [])})
        signals.append({
            "coin": coin,
            "direction": direction,
            "delta_notional": round(delta, 2),
            "conflict_notional": round(conflict, 2),
            "wallet_count": len(contrib),
            "max_single_notional": round(max(contrib.values()), 2),
            "avg_quality": round(sum(quals) / len(quals), 3) if quals else 0.5,
            "groups": groups,
            "wallets": sorted(contrib.keys()),
        })
    signals.sort(key=lambda s: s["delta_notional"], reverse=True)
    return signals


def filter_signals(signals: list[dict], cfg: Config) -> tuple[list[dict], list[dict]]:
    passed, noise = [], []
    for s in signals:
        if (s["delta_notional"] >= cfg.min_delta_notional_usd
                and s["wallet_count"] >= cfg.min_wallet_count
                and s["max_single_notional"] >= cfg.min_single_whale_delta_usd):
            passed.append(s)
        else:
            noise.append(s)
    return passed, noise
