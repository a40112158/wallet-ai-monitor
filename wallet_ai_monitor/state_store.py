"""状态持久化。"""
from __future__ import annotations

import json
import os
from typing import Any

from .logging_utils import get_logger

log = get_logger()
STATE_DIR = "data"
STATE_PATH = os.path.join(STATE_DIR, "state.json")

_DEFAULT: dict[str, Any] = {
    "version": 3,
    "last_positions": {},
    "signal_lifecycle": {},
    "flow_ledger": {},
    "virtual_account": {},
    "ai_cache": {},
    "ai_budget": {},
    "wallet_perf": {},
    "run_history": [],
}


def load_state() -> dict[str, Any]:
    if not os.path.exists(STATE_PATH):
        return json.loads(json.dumps(_DEFAULT))
    try:
        with open(STATE_PATH, encoding="utf-8") as f:
            state = json.load(f)
        for k, v in _DEFAULT.items():
            state.setdefault(k, json.loads(json.dumps(v)))
        return state
    except Exception as e:  # noqa: BLE001
        log.warning("状态加载失败，重置: %s", e)
        return json.loads(json.dumps(_DEFAULT))


def save_state(state: dict[str, Any]) -> None:
    os.makedirs(STATE_DIR, exist_ok=True)
    state["run_history"] = state.get("run_history", [])[-200:]
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, STATE_PATH)
