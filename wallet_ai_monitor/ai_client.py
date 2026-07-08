"""Poe API 调用 + schema 缓存 + 每日预算限流(北京时间日切)。"""
from __future__ import annotations

import hashlib
import json
import time
from typing import Any

import requests

from .config import Config
from .logging_utils import get_logger
from .timeutil import date_bj

log = get_logger()

_EST_POINTS_PER_CALL = 400.0


class AIClient:
    def __init__(self, cfg: Config, ai_cache: dict[str, Any],
                 budget_state: dict[str, Any]):
        self.cfg = cfg
        self.cache = ai_cache
        self.budget = budget_state
        self.stats = {"calls": 0, "cache_hits": 0, "errors": 0,
                      "fallback_used": False, "budget_blocked": 0,
                      "budget_blocked_flag": False}
        self._init_budget()

    def _init_budget(self) -> None:
        today = date_bj()
        if self.budget.get("date") != today:
            self.budget.clear()
            self.budget.update({"date": today, "calls": 0, "points_used": 0.0})
        self.max_calls = None
        if self.cfg.ai_budget_adaptive and self.cfg.ai_daily_target_points > 0:
            self.max_calls = max(1, int(self.cfg.ai_daily_target_points /
                                        _EST_POINTS_PER_CALL))

    def _cache_key(self, prompt_obj: dict) -> str:
        raw = self.cfg.ai_cache_schema + "|" + json.dumps(prompt_obj, sort_keys=True)
        return hashlib.sha256(raw.encode()).hexdigest()[:24]

    def _cache_valid(self, entry: dict) -> bool:
        if entry.get("schema") != self.cfg.ai_cache_schema:
            return False
        res = entry.get("result") or {}
        if not any(k in res for k in ("ai_score", "decisions", "action")):
            return False
        age_min = (time.time() - entry.get("ts", 0)) / 60.0
        return age_min <= self.cfg.ai_cache_ttl_minutes

    def _budget_exhausted(self) -> bool:
        if self.max_calls is None:
            return False
        return self.budget.get("calls", 0) >= self.max_calls

    def chat_json(self, system: str, user_obj: dict) -> dict | None:
        key = self._cache_key({"s": system, "u": user_obj})
        cached = self.cache.get(key)
        if cached and self._cache_valid(cached):
            self.stats["cache_hits"] += 1
            r = dict(cached["result"])
            r["_from_cache"] = True
            return r

        if not self.cfg.ai_enabled or not self.cfg.poe_api_key:
            return None

        if self._budget_exhausted():
            self.stats["budget_blocked"] += 1
            self.stats["budget_blocked_flag"] = True
            return None

        payload = {
            "model": self.cfg.poe_model_signal,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": json.dumps(user_obj, ensure_ascii=False)},
            ],
            "temperature": 0.2,
            "response_format": {"type": "json_object"},
        }
        try:
            self.stats["calls"] += 1
            self.budget["calls"] = self.budget.get("calls", 0) + 1
            self.budget["points_used"] = self.budget.get("points_used", 0.0) + \
                _EST_POINTS_PER_CALL
            r = requests.post(
                f"{self.cfg.poe_base_url}/chat/completions",
                headers={"Authorization": f"Bearer {self.cfg.poe_api_key}",
                         "Content-Type": "application/json"},
                json=payload, timeout=60,
            )
            r.raise_for_status()
            content = r.json()["choices"][0]["message"]["content"]
            result = json.loads(content)
            self.cache[key] = {"schema": self.cfg.ai_cache_schema,
                               "ts": time.time(), "result": result}
            result["_from_cache"] = False
            return result
        except Exception as e:  # noqa: BLE001
            self.stats["errors"] += 1
            log.warning("AI 调用失败: %s", e)
            return None
