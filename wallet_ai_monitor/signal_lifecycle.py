"""信号生命周期与冷却（北京时间展示）。"""
from __future__ import annotations

import time

from .config import Config
from .timeutil import fmt_bj


def _key(sig: dict) -> str:
    return f"{sig['coin']}:{sig['direction']}"


def update_lifecycle(signals: list[dict], lifecycle: dict, cfg: Config) -> None:
    now = time.time()
    cd_sec = cfg.signal_cooldown_minutes * 60
    for sig in signals:
        k = _key(sig)
        rec = lifecycle.get(k)
        dn = sig["delta_notional"]
        if rec is None:
            rec = {"first_seen": now, "last_alert": now, "round": 1,
                   "base_notional": dn}
            sig["state"] = "NEW_SIGNAL"
            sig["cooldown_remaining_min"] = cfg.signal_cooldown_minutes
            sig["amount_change_x"] = 1.0
        else:
            rec["round"] += 1
            since_alert = now - rec.get("last_alert", now)
            in_cooldown = since_alert < cd_sec
            mult = dn / max(rec.get("base_notional", dn), 1)
            sig["amount_change_x"] = round(mult, 2)
            if in_cooldown:
                if mult >= cfg.signal_realert_multiplier:
                    sig["state"] = "RE_ALERT"
                    rec["last_alert"] = now
                    rec["base_notional"] = dn
                else:
                    sig["state"] = "COOLDOWN_REPEAT"
            else:
                sig["state"] = "ACTIVE_REPEAT"
                rec["last_alert"] = now
            sig["cooldown_remaining_min"] = max(
                0, round((cd_sec - since_alert) / 60, 1))

        lifecycle[k] = rec
        dur_h = round((now - rec["first_seen"]) / 3600, 1)
        sig["lifecycle"] = {
            "round": rec["round"], "duration_hours": dur_h,
            "first_seen": rec["first_seen"], "last_alert": rec["last_alert"],
            "first_seen_bj": fmt_bj(rec["first_seen"]),
            "last_alert_bj": fmt_bj(rec["last_alert"]),
        }
        sig["round"] = rec["round"]
        sig["duration_hours"] = dur_h


def should_suppress_open(sig: dict) -> bool:
    return sig.get("state") == "COOLDOWN_REPEAT"
