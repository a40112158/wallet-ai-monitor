from __future__ import annotations

"""
第三层 AI 参数优化器：
- 读取最近报告、虚拟交易表现、运行健康度和当前参数
- 让 Poe 代码/分析模型建议下一轮参数
- 只允许修改 config/ai_param_overrides.env 中的白名单参数
- 所有建议都经过上下限、步进幅度、交叉关系校验
- 不改密钥、不改钱包地址、不加入自动交易
"""

import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from wallet_ai_monitor.budget import estimate_points, usage_from_openai_response
from wallet_ai_monitor.storage import Store

ROOT = Path(__file__).resolve().parents[1]
OVERRIDE_PATH = ROOT / "config" / "ai_param_overrides.env"

# key: (type, min, max)
PARAM_BOUNDS: dict[str, tuple[str, float, float]] = {
    "MIN_DELTA_NOTIONAL_USD": ("int", 50_000, 1_000_000),
    "MIN_SINGLE_WHALE_DELTA_USD": ("int", 100_000, 2_000_000),
    "MIN_WALLET_COUNT": ("int", 2, 8),
    "TOP_SIGNALS_FOR_AI": ("int", 5, 20),
    "AI_MIN_TOTAL_DELTA_NOTIONAL": ("int", 50_000, 1_500_000),
    "AI_MIN_WALLET_COUNT_FOR_CALL": ("int", 1, 6),
    "AI_MIN_WEIGHTED_SCORE_FOR_CALL": ("float", 0, 20),
    "SIGNAL_COOLDOWN_MINUTES": ("int", 120, 1440),
    "SIGNAL_REALERT_MULTIPLIER": ("float", 1.2, 5.0),
    "SIGNAL_EXIT_DECAY_RATIO": ("float", 0.2, 0.9),
    "MARKET_MAX_CANDLE_COINS": ("int", 5, 25),
    "VIRTUAL_ACCOUNT_CAPITAL_USD": ("int", 1_000, 1_000_000),
    "VIRTUAL_TRADE_NOTIONAL_USD": ("int", 0, 1_000_000),
    "VIRTUAL_MIN_AI_CONFIDENCE": ("int", 55, 90),
    "VIRTUAL_TAKE_PROFIT_PCT": ("float", 4, 20),
    "VIRTUAL_STOP_LOSS_PCT": ("float", 1.5, 8),
    "VIRTUAL_MAX_HOLD_HOURS": ("int", 72, 336),
    "SWING_MIN_SCORE_FOR_AI": ("int", 50, 85),
    "SWING_WATCH_SCORE": ("int", 55, 90),
    "SWING_STRONG_SCORE": ("int", 65, 95),
    "HL_CONCURRENCY": ("int", 2, 16),
    "AI_DAILY_TARGET_POINTS": ("int", 10_000, 100_000),
    "WALLET_PERF_MIN_SAMPLE_SIZE": ("int", 3, 30),
    "WALLET_PERF_WEIGHT_IN_SIGNAL": ("float", 0.0, 0.6),
    "WALLET_PERF_MIN_DELTA_NOTIONAL": ("int", 10_000, 500_000),
}

STRING_PARAMS = {
    "SWING_WINDOWS_HOURS": {"2,6,24,72,168"},
    "WALLET_PERF_HORIZONS_HOURS": {"24,72,168"},
}

DEFAULTS: dict[str, str] = {
    "MIN_DELTA_NOTIONAL_USD": "100000",
    "MIN_SINGLE_WHALE_DELTA_USD": "250000",
    "MIN_WALLET_COUNT": "3",
    "TOP_SIGNALS_FOR_AI": "8",
    "AI_MIN_TOTAL_DELTA_NOTIONAL": "150000",
    "AI_MIN_WALLET_COUNT_FOR_CALL": "2",
    "AI_MIN_WEIGHTED_SCORE_FOR_CALL": "0",
    "SIGNAL_COOLDOWN_MINUTES": "360",
    "SIGNAL_REALERT_MULTIPLIER": "2.0",
    "SIGNAL_EXIT_DECAY_RATIO": "0.5",
    "MARKET_MAX_CANDLE_COINS": "12",
    "VIRTUAL_ACCOUNT_CAPITAL_USD": "10000",
    "VIRTUAL_TRADE_NOTIONAL_USD": "0",
    "VIRTUAL_MIN_AI_CONFIDENCE": "70",
    "VIRTUAL_TAKE_PROFIT_PCT": "8",
    "VIRTUAL_STOP_LOSS_PCT": "3",
    "VIRTUAL_MAX_HOLD_HOURS": "168",
    "SWING_MIN_SCORE_FOR_AI": "60",
    "SWING_WATCH_SCORE": "65",
    "SWING_STRONG_SCORE": "80",
    "SWING_WINDOWS_HOURS": "2,6,24,72,168",
    "HL_CONCURRENCY": "3",
    "AI_DAILY_TARGET_POINTS": "33333",
    "WALLET_PERF_HORIZONS_HOURS": "24,72,168",
    "WALLET_PERF_MIN_SAMPLE_SIZE": "5",
    "WALLET_PERF_WEIGHT_IN_SIGNAL": "0.25",
    "WALLET_PERF_MIN_DELTA_NOTIONAL": "50000",
}


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    overrides: dict[str, str]
    rejected: dict[str, str]


def _parse_env_file(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.exists():
        return out
    for raw_line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def current_params() -> dict[str, str]:
    load_dotenv(ROOT / ".env")
    overrides = _parse_env_file(OVERRIDE_PATH)
    params = dict(DEFAULTS)
    for key in params:
        if os.getenv(key) not in (None, ""):
            params[key] = str(os.getenv(key))
    for key, value in overrides.items():
        if key in params:
            params[key] = value
    return params


def _coerce_value(key: str, value: Any) -> tuple[bool, str, str]:
    if key in STRING_PARAMS:
        normalized = str(value).strip()
        if normalized in STRING_PARAMS[key]:
            return True, normalized, ""
        return False, "", f"{key} only allows {sorted(STRING_PARAMS[key])}"

    if key not in PARAM_BOUNDS:
        return False, "", "not allowed"

    typ, low, high = PARAM_BOUNDS[key]
    try:
        f = float(value)
    except (TypeError, ValueError):
        return False, "", "not numeric"
    if f < low or f > high:
        return False, "", f"out of bounds {low}-{high}"
    if typ == "int":
        return True, str(int(round(f))), ""
    return True, str(round(f, 4)).rstrip("0").rstrip("."), ""


def _within_step_limit(key: str, old: str, new: str) -> tuple[bool, str]:
    if key in STRING_PARAMS:
        return True, ""
    try:
        old_f = float(old)
        new_f = float(new)
    except ValueError:
        return True, ""
    if old_f <= 0:
        return True, ""
    ratio = new_f / old_f
    # 防止 AI 一次把阈值改崩；强制渐进式优化。
    if ratio > 1.75 or ratio < 0.57:
        return False, f"step too large old={old} new={new}"
    return True, ""


def validate_overrides(candidate: dict[str, Any], current: dict[str, str] | None = None) -> ValidationResult:
    current = current or current_params()
    clean: dict[str, str] = {}
    rejected: dict[str, str] = {}
    for key, value in candidate.items():
        if any(x in key.upper() for x in ("KEY", "TOKEN", "SECRET", "PASSWORD", "PRIVATE")):
            rejected[key] = "secret-like key"
            continue
        ok, normalized, reason = _coerce_value(key, value)
        if not ok:
            rejected[key] = reason
            continue
        step_ok, step_reason = _within_step_limit(key, current.get(key, DEFAULTS.get(key, normalized)), normalized)
        if not step_ok:
            rejected[key] = step_reason
            continue
        clean[key] = normalized

    # Cross-parameter constraints.
    def num(k: str, fallback: str = "0") -> float:
        return float(clean.get(k, current.get(k, fallback)))

    if num("SWING_WATCH_SCORE", "65") < num("SWING_MIN_SCORE_FOR_AI", "60"):
        rejected["SWING_WATCH_SCORE"] = "must be >= SWING_MIN_SCORE_FOR_AI"
        clean.pop("SWING_WATCH_SCORE", None)
    if num("SWING_STRONG_SCORE", "80") < num("SWING_WATCH_SCORE", "65"):
        rejected["SWING_STRONG_SCORE"] = "must be >= SWING_WATCH_SCORE"
        clean.pop("SWING_STRONG_SCORE", None)
    if num("MIN_SINGLE_WHALE_DELTA_USD", "250000") < num("MIN_DELTA_NOTIONAL_USD", "100000"):
        rejected["MIN_SINGLE_WHALE_DELTA_USD"] = "must be >= MIN_DELTA_NOTIONAL_USD"
        clean.pop("MIN_SINGLE_WHALE_DELTA_USD", None)
    if num("VIRTUAL_TAKE_PROFIT_PCT", "8") <= num("VIRTUAL_STOP_LOSS_PCT", "3"):
        rejected["VIRTUAL_TAKE_PROFIT_PCT"] = "take profit must be > stop loss"
        clean.pop("VIRTUAL_TAKE_PROFIT_PCT", None)

    return ValidationResult(ok=bool(clean), overrides=clean, rejected=rejected)


def latest_report_text(max_chars: int = 16000) -> str:
    p = ROOT / "reports" / "latest_signals.json"
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")[-max_chars:]


def latest_signals(max_chars: int = 20000) -> Any:
    p = ROOT / "reports" / "latest_signals.json"
    if not p.exists():
        return {}
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")[-max_chars:]
        return json.loads(text)
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}


def collect_metrics() -> dict[str, Any]:
    now = int(datetime.now(timezone.utc).timestamp())
    db_path = ROOT / os.getenv("DB_PATH", ".state/wallet_monitor.sqlite3")
    state: dict[str, Any] = {}
    if db_path.exists():
        try:
            with Store(db_path) as store:
                state = {
                    "integrity_ok": store.integrity_ok(),
                    "virtual_summary": store.virtual_summary(),
                    "health_24h": store.run_health_summary(now - 86400),
                    "health_7d": store.run_health_summary(now - 7 * 86400),
                    "estimated_points_today": store.estimated_ai_points_since(now - (now % 86400)),
                }
        except Exception as exc:  # noqa: BLE001
            state = {"error": str(exc)}
    return {
        "time_utc": datetime.now(timezone.utc).isoformat(),
        "current_params": current_params(),
        "state": state,
        "latest_signals": latest_signals(),
        "latest_signals_tail": latest_report_text(),
    }


def fallback_suggestions(metrics: dict[str, Any]) -> dict[str, Any]:
    """Deterministic safe fallback used when Poe is disabled/unavailable.

    It intentionally changes only a few knobs and only by small steps.
    """
    params = metrics.get("current_params") or current_params()
    state = metrics.get("state") or {}
    health = state.get("health_24h") or {}
    virt = state.get("virtual_summary") or {}
    suggestions: dict[str, Any] = {}

    signals_24h = int(health.get("signals_count") or 0)
    avg_duration = float(health.get("avg_duration_sec") or 0)
    closed_wins = int(virt.get("wins") or 0)
    closed_losses = int(virt.get("losses") or 0)
    closed_total = closed_wins + closed_losses
    avg_pnl = float(virt.get("avg_closed_pnl_pct") or 0)

    def get_float(k: str) -> float:
        try:
            return float(params.get(k, DEFAULTS[k]))
        except Exception:
            return float(DEFAULTS[k])

    # Too many signals: make filters stricter.
    if signals_24h > 60:
        suggestions["MIN_DELTA_NOTIONAL_USD"] = int(get_float("MIN_DELTA_NOTIONAL_USD") * 1.15)
        suggestions["SWING_MIN_SCORE_FOR_AI"] = int(get_float("SWING_MIN_SCORE_FOR_AI") + 3)
        suggestions["SIGNAL_COOLDOWN_MINUTES"] = int(get_float("SIGNAL_COOLDOWN_MINUTES") * 1.15)
    # Too few signals: loosen, but not below bounds.
    elif 0 < signals_24h < 5:
        suggestions["MIN_DELTA_NOTIONAL_USD"] = int(get_float("MIN_DELTA_NOTIONAL_USD") * 0.9)
        suggestions["SWING_MIN_SCORE_FOR_AI"] = int(get_float("SWING_MIN_SCORE_FOR_AI") - 2)

    # If enough closed paper trades and poor result, be more selective.
    if closed_total >= 8:
        win_rate = closed_wins / max(closed_total, 1)
        if win_rate < 0.42 or avg_pnl < -1.0:
            suggestions["VIRTUAL_MIN_AI_CONFIDENCE"] = int(get_float("VIRTUAL_MIN_AI_CONFIDENCE") + 3)
            suggestions["SWING_STRONG_SCORE"] = int(get_float("SWING_STRONG_SCORE") + 2)
            suggestions["VIRTUAL_STOP_LOSS_PCT"] = max(1.5, get_float("VIRTUAL_STOP_LOSS_PCT") * 0.9)
        elif win_rate > 0.58 and avg_pnl > 1.0:
            suggestions["TOP_SIGNALS_FOR_AI"] = int(get_float("TOP_SIGNALS_FOR_AI") + 1)
            suggestions["VIRTUAL_MIN_AI_CONFIDENCE"] = int(get_float("VIRTUAL_MIN_AI_CONFIDENCE") - 2)

    # If run time is high, reduce candle breadth or concurrency a bit.
    if avg_duration > 240:
        suggestions["MARKET_MAX_CANDLE_COINS"] = int(get_float("MARKET_MAX_CANDLE_COINS") * 0.85)
        suggestions["HL_CONCURRENCY"] = int(get_float("HL_CONCURRENCY") * 0.9)

    return suggestions


def extract_json(text: str) -> dict[str, Any]:
    blocks = re.findall(r"```(?:json)?\s*(.*?)```", text, flags=re.S | re.I)
    for b in blocks:
        try:
            return json.loads(b.strip())
        except json.JSONDecodeError:
            continue
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        try:
            return json.loads(text[start : end + 1])
        except json.JSONDecodeError:
            pass
    return {}


def ai_suggestions(metrics: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    api_key = os.getenv("POE_API_KEY", "")
    if not api_key:
        return fallback_suggestions(metrics), {"ok": False, "reason": "POE_API_KEY empty; used fallback rules"}
    try:
        from openai import OpenAI
    except ModuleNotFoundError:
        return fallback_suggestions(metrics), {"ok": False, "reason": "openai missing; used fallback rules"}

    client = OpenAI(api_key=api_key, base_url=os.getenv("POE_BASE_URL", "https://api.poe.com/v1"))
    model = os.getenv("POE_MODEL_PARAM", os.getenv("POE_MODEL_CODE", "Claude-Sonnet-4.6"))
    max_tokens = int(os.getenv("AI_PARAM_OPTIMIZER_MAX_TOKENS", "2500"))
    system = (
        "你是量化监控系统的参数优化器。你只能建议安全参数，不许写代码，不许要求自动交易。"
        "目标是基于钱包信号报告、虚拟交易结果和运行健康度，优化下一轮筛选阈值。"
        "必须只输出 JSON：{summary:string, overrides:{KEY:value}, rationale:{KEY:string}, risk:string}。"
        "只能使用允许的参数和范围，不要输出密钥、token、地址或非白名单字段。"
    )
    allowed = {
        "numeric_bounds": PARAM_BOUNDS,
        "string_params": {k: sorted(v) for k, v in STRING_PARAMS.items()},
        "rules": [
            "逐步优化，不要一次大幅调整。",
            "信号太多且质量差：提高金额/评分/置信度/冷却。",
            "信号太少：小幅降低金额/评分。",
            "虚拟交易胜率差：提高置信度和强候选分数，收紧止损。",
            "运行耗时高：降低 MARKET_MAX_CANDLE_COINS 或 HL_CONCURRENCY。",
            "必须保留 SWING_WINDOWS_HOURS=2,6,24,72,168。",
        ],
    }
    prompt = {
        "allowed": allowed,
        "metrics": metrics,
    }
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(prompt, ensure_ascii=False)},
        ],
        temperature=0.08,
        max_tokens=max_tokens,
    )
    text = resp.choices[0].message.content or "{}"
    parsed = extract_json(text)
    usage = usage_from_openai_response(resp)
    points = estimate_points(
        prompt_tokens=usage.get("prompt_tokens"),
        completion_tokens=usage.get("completion_tokens"),
        input_cost_per_million_usd=float(os.getenv("AI_CODE_INPUT_COST_PER_MILLION_USD", "2.58")),
        output_cost_per_million_usd=float(os.getenv("AI_CODE_OUTPUT_COST_PER_MILLION_USD", "12.88")),
        points_per_usd=float(os.getenv("AI_POINTS_PER_USD", "33333")),
    )
    try:
        with Store(ROOT / os.getenv("DB_PATH", ".state/wallet_monitor.sqlite3")) as store:
            store.record_ai_usage(
                ts=int(datetime.now(timezone.utc).timestamp()),
                model=model,
                purpose="param_optimizer",
                usage=usage,
                estimated_points=points,
                cached=False,
                ok=True,
            )
    except Exception:
        pass
    return (parsed.get("overrides") or {}), {
        "ok": True,
        "model": model,
        "usage": usage,
        "estimated_points": points,
        "raw": parsed,
    }


def write_override_file(overrides: dict[str, str], metrics: dict[str, Any], meta: dict[str, Any], rejected: dict[str, str]) -> None:
    OVERRIDE_PATH.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    if overrides:
        lines = [
            "# AI 参数优化层自动生成。可手动编辑，但不要放任何密钥。",
            f"# Updated: {now}",
            "# Disable by setting GitHub Variable AI_PARAM_OVERRIDES_ENABLED=false",
            "# Purpose: tune signal filters / swing scoring / paper-trade risk controls only.",
            "",
        ]
        for key in sorted(overrides):
            lines.append(f"{key}={overrides[key]}")
        lines.append("")
        OVERRIDE_PATH.write_text("\n".join(lines), encoding="utf-8")

    report_dir = ROOT / "reports"
    report_dir.mkdir(exist_ok=True)
    payload = {
        "updated_at": now,
        "overrides": overrides,
        "rejected": rejected,
        "meta": meta,
        "metrics_digest": {
            "current_params": metrics.get("current_params"),
            "state": metrics.get("state"),
        },
    }
    (report_dir / "param_optimizer_latest.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    # Minimal-report mode: keep only param_optimizer_latest.json in reports/.


def main() -> int:
    load_dotenv(ROOT / ".env")
    if os.getenv("AI_PARAM_OPTIMIZER_ENABLED", "true").strip().lower() not in {"1", "true", "yes", "on"}:
        print("AI_PARAM_OPTIMIZER_ENABLED is false; skip")
        return 0
    metrics = collect_metrics()
    candidate, meta = ai_suggestions(metrics)
    validation = validate_overrides(candidate, metrics.get("current_params") or current_params())

    # If AI gave nothing valid, use deterministic fallback once more.
    if not validation.overrides:
        fallback = fallback_suggestions(metrics)
        validation = validate_overrides(fallback, metrics.get("current_params") or current_params())
        meta = {**meta, "fallback_used_after_validation": True}

    write_override_file(validation.overrides, metrics, meta, validation.rejected)
    print("AI parameter optimizer wrote", OVERRIDE_PATH)
    print(json.dumps({"overrides": validation.overrides, "rejected": validation.rejected, "meta": {k: v for k, v in meta.items() if k != "raw"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
