"""配置加载：环境变量 + 硬风控上限（不可被优化器突破）。"""
from __future__ import annotations

import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:  # noqa: BLE001
    pass

HARD_MAX_LEVERAGE = 10
HARD_MAX_MARGIN_PCT_PER_TRADE = 20
HARD_MAX_TOTAL_MARGIN_PCT = 60


def _s(k: str, d: str = "") -> str:
    # GitHub Actions 中未配置的 vars 会传入空字符串；空值应继续使用默认配置。
    v = os.getenv(k)
    if v is None or v.strip() == "":
        return d
    return v.strip()


def _b(k: str, d: bool) -> bool:
    # 空字符串不应把默认 True 误改成 False。
    v = os.getenv(k)
    if v is None or v.strip() == "":
        return d
    return v.strip().lower() in ("1", "true", "yes", "on")


def _f(k: str, d: float) -> float:
    try:
        v = os.getenv(k)
        if v is None or v.strip() == "":
            return d
        return float(v)
    except (TypeError, ValueError):
        return d


def _i(k: str, d: int) -> int:
    try:
        v = os.getenv(k)
        if v is None or v.strip() == "":
            return d
        return int(float(v))
    except (TypeError, ValueError):
        return d


class Config:
    def __init__(self) -> None:
        self.hl_api_url = _s("HL_API_URL", "https://api.hyperliquid.xyz/info")
        self.hl_timeout = _i("HL_TIMEOUT", 15)
        self.hl_request_delay = _f("HL_REQUEST_DELAY", 0.12)
        self.hl_min_success_rate = _f("HL_MIN_SUCCESS_RATE", 0.75)
        self.wallet_dir = _s("WALLET_DIR", "wallets")
        self.max_wallets_per_run = _i("MAX_WALLETS_PER_RUN", 999999)
        self.auto_shard_rotation = _b("AUTO_SHARD_ROTATION", False)
        self.min_delta_notional_usd = _f("MIN_DELTA_NOTIONAL_USD", 200000)
        self.min_single_whale_delta_usd = _f("MIN_SINGLE_WHALE_DELTA_USD", 80000)
        self.min_wallet_count = _i("MIN_WALLET_COUNT", 1)
        self.min_position_change_pct = _f("MIN_POSITION_CHANGE_PCT", 0.05)
        self.top_signals_for_ai = _i("TOP_SIGNALS_FOR_AI", 10)
        self.signal_cooldown_minutes = _i("SIGNAL_COOLDOWN_MINUTES", 240)
        self.signal_realert_multiplier = _f("SIGNAL_REALERT_MULTIPLIER", 1.8)
        self.ai_enabled = _b("AI_ENABLED", True)
        self.ai_scoring_enabled = _b("AI_SCORING_ENABLED", True)
        self.poe_api_key = _s("POE_API_KEY", "")
        self.poe_base_url = _s("POE_BASE_URL", "https://api.poe.com/v1")
        self.poe_model_signal = _s("POE_MODEL_SIGNAL", "Claude-Sonnet-4.5")
        self.ai_cache_schema = _s("AI_CACHE_SCHEMA", "v3")
        self.ai_cache_ttl_minutes = _i("AI_CACHE_TTL_MINUTES", 180)
        self.ai_min_total_delta_notional = _f("AI_MIN_TOTAL_DELTA_NOTIONAL", 300000)
        self.ai_min_wallet_count_for_call = _i("AI_MIN_WALLET_COUNT_FOR_CALL", 1)
        self.ai_min_final_score_for_open = _f("AI_MIN_FINAL_SCORE_FOR_OPEN", 65)
        self.ai_budget_adaptive = _b("AI_BUDGET_ADAPTIVE", True)
        self.ai_daily_target_points = _f("AI_DAILY_TARGET_POINTS", 20000)
        self.ai_max_leverage = _f("AI_MAX_LEVERAGE", 5)
        self.ai_max_margin_pct = _f("AI_MAX_MARGIN_PCT_PER_TRADE", 10)
        self.ai_max_total_margin_pct = _f("AI_MAX_TOTAL_MARGIN_PCT", 50)
        self.virtual_capital_usd = _f("VIRTUAL_CAPITAL_USD", 100000)
        self.telegram_enabled = _b("TELEGRAM_ENABLED", False)
        self.telegram_bot_token = _s("TELEGRAM_BOT_TOKEN", "")
        self.telegram_chat_id = _s("TELEGRAM_CHAT_ID", "")
        self.param_optimizer_enabled = _b("PARAM_OPTIMIZER_ENABLED", True)
        self._enforce_hard_limits()

    def _enforce_hard_limits(self) -> None:
        self.ai_max_leverage = min(self.ai_max_leverage, HARD_MAX_LEVERAGE)
        self.ai_max_margin_pct = min(self.ai_max_margin_pct,
                                     HARD_MAX_MARGIN_PCT_PER_TRADE)
        self.ai_max_total_margin_pct = min(self.ai_max_total_margin_pct,
                                           HARD_MAX_TOTAL_MARGIN_PCT)

    def apply_overrides(self, overrides: dict) -> None:
        for k, v in overrides.items():
            if hasattr(self, k):
                cur = getattr(self, k)
                try:
                    setattr(self, k, type(cur)(v) if isinstance(cur, (int, float))
                            else v)
                except (TypeError, ValueError):
                    pass
        self._enforce_hard_limits()


def load_config() -> Config:
    return Config()
