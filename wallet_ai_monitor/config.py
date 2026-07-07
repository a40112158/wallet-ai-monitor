from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv


PARAM_OVERRIDE_ALLOWED_KEYS = {
    "MIN_DELTA_NOTIONAL_USD",
    "MIN_SINGLE_WHALE_DELTA_USD",
    "MIN_WALLET_COUNT",
    "TOP_SIGNALS_FOR_AI",
    "AI_MIN_TOTAL_DELTA_NOTIONAL",
    "AI_MIN_WALLET_COUNT_FOR_CALL",
    "AI_MIN_WEIGHTED_SCORE_FOR_CALL",
    "SIGNAL_COOLDOWN_MINUTES",
    "SIGNAL_REALERT_MULTIPLIER",
    "SIGNAL_EXIT_DECAY_RATIO",
    "MARKET_MAX_CANDLE_COINS",
    "VIRTUAL_ACCOUNT_CAPITAL_USD",
    "VIRTUAL_TRADE_NOTIONAL_USD",
    "VIRTUAL_MIN_AI_CONFIDENCE",
    "VIRTUAL_TAKE_PROFIT_PCT",
    "VIRTUAL_STOP_LOSS_PCT",
    "VIRTUAL_MAX_HOLD_HOURS",
    "SWING_MIN_SCORE_FOR_AI",
    "SWING_WATCH_SCORE",
    "SWING_STRONG_SCORE",
    "SWING_WINDOWS_HOURS",
    "HL_CONCURRENCY",
    "AI_DAILY_TARGET_POINTS",
    "WALLET_PERF_HORIZONS_HOURS",
    "WALLET_PERF_MIN_SAMPLE_SIZE",
    "WALLET_PERF_WEIGHT_IN_SIGNAL",
    "WALLET_PERF_MIN_DELTA_NOTIONAL",
    "AI_TRADE_DECISION_MAX_TOKENS",
    "AI_CONFIDENCE_SCORE_WEIGHT",
    "VIRTUAL_CLOSE_WARNING_MAX_HOLD_RATIO",
    "VIRTUAL_CLOSE_WARNING_SL_RATIO",
    "VIRTUAL_CLOSE_WARNING_TP_RATIO",
    "VIRTUAL_AI_PRE_CLOSE_MIN_CONFIDENCE",
    "VIRTUAL_CLOSE_WARNING_ENABLED",
    "AI_RULE_SCORE_WEIGHT",
    "AI_SCORE_WEIGHT",
    "AI_MIN_FINAL_SCORE_FOR_OPEN",
    "AI_SCORING_ENABLED",
    "AI_CLOSE_MIN_CONFIDENCE",
    "AI_MAX_TOTAL_MARGIN_PCT",
    "AI_MIN_MARGIN_PCT_PER_TRADE",
    "AI_MAX_MARGIN_PCT_PER_TRADE",
    "AI_MIN_LEVERAGE",
    "AI_MAX_LEVERAGE",
    "AI_POSITION_SIZING_ENABLED",
    "AI_TRADE_MANAGEMENT_ENABLED",
}


PARAM_OVERRIDE_NUMERIC_BOUNDS: dict[str, tuple[float, float]] = {
    "MIN_DELTA_NOTIONAL_USD": (50_000, 1_000_000),
    "MIN_SINGLE_WHALE_DELTA_USD": (100_000, 2_000_000),
    "MIN_WALLET_COUNT": (2, 8),
    "TOP_SIGNALS_FOR_AI": (5, 20),
    "AI_MIN_TOTAL_DELTA_NOTIONAL": (50_000, 1_500_000),
    "AI_MIN_WALLET_COUNT_FOR_CALL": (1, 6),
    "AI_MIN_WEIGHTED_SCORE_FOR_CALL": (0, 20),
    "SIGNAL_COOLDOWN_MINUTES": (120, 1440),
    "SIGNAL_REALERT_MULTIPLIER": (1.2, 5.0),
    "SIGNAL_EXIT_DECAY_RATIO": (0.2, 0.9),
    "MARKET_MAX_CANDLE_COINS": (5, 25),
    "VIRTUAL_MIN_AI_CONFIDENCE": (55, 90),
    "VIRTUAL_TAKE_PROFIT_PCT": (4, 20),
    "VIRTUAL_STOP_LOSS_PCT": (1.5, 8),
    "VIRTUAL_MAX_HOLD_HOURS": (72, 336),
    "VIRTUAL_ACCOUNT_CAPITAL_USD": (1_000, 1_000_000),
    "VIRTUAL_TRADE_NOTIONAL_USD": (0, 1_000_000),
    "SWING_MIN_SCORE_FOR_AI": (50, 85),
    "SWING_WATCH_SCORE": (55, 90),
    "SWING_STRONG_SCORE": (65, 95),
    "HL_CONCURRENCY": (2, 16),
    "AI_DAILY_TARGET_POINTS": (10_000, 100_000),
    "WALLET_PERF_MIN_SAMPLE_SIZE": (3, 30),
    "WALLET_PERF_WEIGHT_IN_SIGNAL": (0.0, 0.6),
    "WALLET_PERF_MIN_DELTA_NOTIONAL": (10_000, 500_000),
    "AI_TRADE_DECISION_MAX_TOKENS": (800, 5000),
    "AI_CONFIDENCE_SCORE_WEIGHT": (0, 1),
    "VIRTUAL_CLOSE_WARNING_MAX_HOLD_RATIO": (0.3, 0.98),
    "VIRTUAL_CLOSE_WARNING_SL_RATIO": (0.3, 0.95),
    "VIRTUAL_CLOSE_WARNING_TP_RATIO": (0.3, 0.95),
    "VIRTUAL_AI_PRE_CLOSE_MIN_CONFIDENCE": (40, 90),
    "AI_RULE_SCORE_WEIGHT": (0, 1),
    "AI_SCORE_WEIGHT": (0, 1),
    "AI_MIN_FINAL_SCORE_FOR_OPEN": (50, 95),
    "AI_CLOSE_MIN_CONFIDENCE": (50, 95),
    "AI_MAX_TOTAL_MARGIN_PCT": (5, 80),
    "AI_MIN_MARGIN_PCT_PER_TRADE": (0.1, 5),
    "AI_MAX_MARGIN_PCT_PER_TRADE": (0.5, 15),
    "AI_MIN_LEVERAGE": (1, 10),
    "AI_MAX_LEVERAGE": (1, 10),
}

PARAM_OVERRIDE_BOOL_VALUES = {"AI_TRADE_MANAGEMENT_ENABLED", "AI_POSITION_SIZING_ENABLED", "AI_SCORING_ENABLED", "VIRTUAL_CLOSE_WARNING_ENABLED"}

PARAM_OVERRIDE_STRING_VALUES: dict[str, set[str]] = {
    "SWING_WINDOWS_HOURS": {"2,6,24,72,168"},
    "WALLET_PERF_HORIZONS_HOURS": {"24,72,168"},
}


def _valid_param_override_value(key: str, value: str) -> bool:
    if key in PARAM_OVERRIDE_BOOL_VALUES:
        return value.lower() in {"true", "false", "1", "0", "yes", "no", "on", "off"}
    if key in PARAM_OVERRIDE_STRING_VALUES:
        return value in PARAM_OVERRIDE_STRING_VALUES[key]
    bounds = PARAM_OVERRIDE_NUMERIC_BOUNDS.get(key)
    if not bounds:
        return False
    try:
        number = float(value)
    except ValueError:
        return False
    low, high = bounds
    return low <= number <= high


def _load_param_overrides(path: Path) -> None:
    """Load AI-maintained safe parameter overrides.

    GitHub Variables and .env are useful for manual control, but the third AI layer
    needs a controlled way to tune strategy parameters over time. This loader only
    accepts a strict allowlist and rejects anything secret-like or malformed.
    """
    if not path.exists():
        return
    secret_markers = ("KEY", "TOKEN", "SECRET", "PASSWORD", "PRIVATE")
    for raw_line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key not in PARAM_OVERRIDE_ALLOWED_KEYS:
            continue
        if any(marker in key.upper() for marker in secret_markers):
            continue
        if "\n" in value or "\r" in value:
            continue
        if not _valid_param_override_value(key, value):
            continue
        os.environ[key] = value



def _bool(name: str, default: bool = False) -> bool:
    v = os.getenv(name)
    if v is None:
        return default
    return v.strip().lower() in {"1", "true", "yes", "y", "on"}


def _int(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, str(default)))
    except ValueError:
        return default


def _float(name: str, default: float) -> float:
    try:
        return float(os.getenv(name, str(default)))
    except ValueError:
        return default


@dataclass(frozen=True)
class Settings:
    root_dir: Path
    data_dir: Path
    state_dir: Path
    report_dir: Path
    db_path: Path
    data_retention_days: int
    report_retention_days: int

    poe_api_key: str
    poe_base_url: str
    poe_model_signal: str
    poe_model_code: str
    ai_enabled: bool
    ai_max_output_tokens: int
    ai_temperature: float
    ai_timeout_seconds: int
    ai_cache_ttl_minutes: int
    ai_min_total_delta_notional: float
    ai_min_wallet_count_for_call: int
    ai_min_weighted_score_for_call: float

    hl_info_url: str
    hl_concurrency: int
    hl_timeout_seconds: int
    hl_retries: int
    hl_batch_size: int
    hl_batch_delay_seconds: float
    max_wallets_per_run: int
    scan_offset: int
    auto_shard_rotation: bool
    warmup_missing_wallets: bool

    min_delta_notional_usd: float
    min_single_whale_delta_usd: float
    min_wallet_count: int
    top_signals_for_ai: int
    signal_ttl_hours: int
    default_leverage_for_pnl: float
    conservative_fee_bps: float
    conservative_slippage_bps: float
    smart_money_weight: float
    money_printer_weight: float

    virtual_trading_enabled: bool
    virtual_account_capital_usd: float
    virtual_trade_notional_usd: float
    virtual_max_open_trades: int
    virtual_min_ai_confidence: float
    virtual_take_profit_pct: float
    virtual_stop_loss_pct: float
    virtual_max_hold_hours: int
    ai_trade_management_enabled: bool
    ai_position_sizing_enabled: bool
    ai_min_leverage: float
    ai_max_leverage: float
    ai_min_margin_pct_per_trade: float
    ai_max_margin_pct_per_trade: float
    ai_max_total_margin_pct: float
    ai_close_min_confidence: float
    ai_trade_decision_max_tokens: int
    ai_scoring_enabled: bool
    ai_min_final_score_for_open: float
    ai_score_weight: float
    ai_rule_score_weight: float
    ai_confidence_score_weight: float
    virtual_close_warning_enabled: bool
    virtual_ai_pre_close_min_confidence: float
    virtual_close_warning_tp_ratio: float
    virtual_close_warning_sl_ratio: float
    virtual_close_warning_max_hold_ratio: float

    telegram_bot_token: str
    telegram_chat_id: str
    telegram_enabled: bool
    allow_auto_patch: bool

    # Adaptive Poe budget controller. These are estimates; tune via GitHub Variables.
    ai_budget_adaptive: bool
    ai_daily_target_points: int
    ai_points_per_usd: float
    ai_signal_input_cost_per_million_usd: float
    ai_signal_output_cost_per_million_usd: float
    ai_budget_min_threshold_multiplier: float
    ai_budget_max_threshold_multiplier: float
    ai_budget_min_top_n: int
    ai_budget_max_top_n: int

    # Signal lifecycle / duplicate control.
    signal_cooldown_minutes: int
    signal_realert_multiplier: float
    signal_exit_decay_ratio: float

    # Market confirmation layer.
    market_candles_enabled: bool
    market_candle_intervals: str
    market_candle_lookback_minutes: int
    market_candle_concurrency: int
    market_max_candle_coins: int

    # State hardening.
    state_backup_enabled: bool
    state_backup_keep: int

    # Swing contract mode: medium/long-term futures candidate selection.
    swing_mode_enabled: bool
    swing_windows_hours: str
    swing_min_score_for_ai: float
    swing_watch_score: float
    swing_strong_score: float
    swing_horizon_days: str

    # Wallet performance / win-rate quality layer.
    wallet_performance_enabled: bool
    wallet_perf_horizons_hours: str
    wallet_perf_min_sample_size: int
    wallet_perf_weight_in_signal: float
    wallet_perf_decay_days: int
    wallet_perf_min_delta_notional: float


def load_settings() -> Settings:
    root = Path.cwd()
    load_dotenv(root / ".env")
    if _bool("AI_PARAM_OVERRIDES_ENABLED", True):
        _load_param_overrides(root / "config" / "ai_param_overrides.env")

    state_dir = Path(os.getenv("STATE_DIR", ".state"))
    report_dir = Path(os.getenv("REPORT_DIR", "reports"))
    db_path = Path(os.getenv("DB_PATH", str(state_dir / "wallet_monitor.sqlite3")))

    return Settings(
        root_dir=root,
        data_dir=root / "data",
        state_dir=state_dir,
        report_dir=report_dir,
        db_path=db_path,
        data_retention_days=max(7, _int("DATA_RETENTION_DAYS", 180)),
        report_retention_days=max(1, _int("REPORT_RETENTION_DAYS", 30)),
        poe_api_key=os.getenv("POE_API_KEY", ""),
        poe_base_url=os.getenv("POE_BASE_URL", "https://api.poe.com/v1"),
        poe_model_signal=os.getenv("POE_MODEL_SIGNAL", "gpt-5.4-mini"),
        poe_model_code=os.getenv("POE_MODEL_CODE", "Claude-Sonnet-4.6"),
        ai_enabled=_bool("AI_ENABLED", True),
        ai_max_output_tokens=_int("AI_MAX_OUTPUT_TOKENS", 900),
        ai_temperature=_float("AI_TEMPERATURE", 0.15),
        ai_timeout_seconds=max(10, _int("AI_TIMEOUT_SECONDS", 60)),
        ai_cache_ttl_minutes=max(0, _int("AI_CACHE_TTL_MINUTES", 90)),
        ai_min_total_delta_notional=_float("AI_MIN_TOTAL_DELTA_NOTIONAL", 100000.0),
        ai_min_wallet_count_for_call=max(1, _int("AI_MIN_WALLET_COUNT_FOR_CALL", 2)),
        ai_min_weighted_score_for_call=_float("AI_MIN_WEIGHTED_SCORE_FOR_CALL", 0.0),
        hl_info_url=os.getenv("HL_INFO_URL", "https://api.hyperliquid.xyz/info"),
        hl_concurrency=max(1, _int("HL_CONCURRENCY", 3)),
        hl_timeout_seconds=max(3, _int("HL_TIMEOUT_SECONDS", 30)),
        hl_retries=max(1, _int("HL_RETRIES", 6)),
        hl_batch_size=max(1, _int("HL_BATCH_SIZE", 80)),
        hl_batch_delay_seconds=max(0.0, _float("HL_BATCH_DELAY_SECONDS", 2.0)),
        max_wallets_per_run=max(0, _int("MAX_WALLETS_PER_RUN", 999999)),
        scan_offset=max(0, _int("SCAN_OFFSET", 0)),
        auto_shard_rotation=_bool("AUTO_SHARD_ROTATION", False),
        warmup_missing_wallets=_bool("WARMUP_MISSING_WALLETS", True),
        min_delta_notional_usd=_float("MIN_DELTA_NOTIONAL_USD", 100000.0),
        min_single_whale_delta_usd=_float("MIN_SINGLE_WHALE_DELTA_USD", 250000.0),
        min_wallet_count=max(1, _int("MIN_WALLET_COUNT", 3)),
        top_signals_for_ai=max(1, _int("TOP_SIGNALS_FOR_AI", 8)),
        signal_ttl_hours=max(1, _int("SIGNAL_TTL_HOURS", 336)),
        default_leverage_for_pnl=max(1.0, _float("DEFAULT_LEVERAGE_FOR_PNL", 1.0)),
        conservative_fee_bps=max(0.0, _float("CONSERVATIVE_FEE_BPS", 5.0)),
        conservative_slippage_bps=max(0.0, _float("CONSERVATIVE_SLIPPAGE_BPS", 8.0)),
        smart_money_weight=_float("SMART_MONEY_WEIGHT", 1.0),
        money_printer_weight=_float("MONEY_PRINTER_WEIGHT", 1.35),
        virtual_trading_enabled=_bool("VIRTUAL_TRADING_ENABLED", True),
        virtual_account_capital_usd=max(1.0, _float("VIRTUAL_ACCOUNT_CAPITAL_USD", 10000.0)),
        # 0 means auto allocation: account capital / max open trades. Any larger value is capped by that auto allocation.
        virtual_trade_notional_usd=max(0.0, _float("VIRTUAL_TRADE_NOTIONAL_USD", 0.0)),
        virtual_max_open_trades=max(1, _int("VIRTUAL_MAX_OPEN_TRADES", 6)),
        virtual_min_ai_confidence=max(0.0, _float("VIRTUAL_MIN_AI_CONFIDENCE", 70.0)),
        virtual_take_profit_pct=max(0.1, _float("VIRTUAL_TAKE_PROFIT_PCT", 8.0)),
        virtual_stop_loss_pct=max(0.1, _float("VIRTUAL_STOP_LOSS_PCT", 3.0)),
        virtual_max_hold_hours=max(1, _int("VIRTUAL_MAX_HOLD_HOURS", 168)),
        ai_trade_management_enabled=_bool("AI_TRADE_MANAGEMENT_ENABLED", True),
        ai_position_sizing_enabled=_bool("AI_POSITION_SIZING_ENABLED", True),
        ai_min_leverage=max(1.0, min(10.0, _float("AI_MIN_LEVERAGE", 1.0))),
        ai_max_leverage=max(1.0, min(10.0, _float("AI_MAX_LEVERAGE", 10.0))),
        ai_min_margin_pct_per_trade=max(0.1, _float("AI_MIN_MARGIN_PCT_PER_TRADE", 0.5)),
        ai_max_margin_pct_per_trade=max(0.1, _float("AI_MAX_MARGIN_PCT_PER_TRADE", 8.0)),
        ai_max_total_margin_pct=max(1.0, min(100.0, _float("AI_MAX_TOTAL_MARGIN_PCT", 35.0))),
        ai_close_min_confidence=max(0.0, min(100.0, _float("AI_CLOSE_MIN_CONFIDENCE", 65.0))),
        ai_trade_decision_max_tokens=max(500, _int("AI_TRADE_DECISION_MAX_TOKENS", 1800)),
        ai_scoring_enabled=_bool("AI_SCORING_ENABLED", True),
        ai_min_final_score_for_open=max(0.0, min(100.0, _float("AI_MIN_FINAL_SCORE_FOR_OPEN", 65.0))),
        ai_score_weight=max(0.0, min(1.0, _float("AI_SCORE_WEIGHT", 0.60))),
        ai_rule_score_weight=max(0.0, min(1.0, _float("AI_RULE_SCORE_WEIGHT", 0.25))),
        ai_confidence_score_weight=max(0.0, min(1.0, _float("AI_CONFIDENCE_SCORE_WEIGHT", 0.15))),
        virtual_close_warning_enabled=_bool("VIRTUAL_CLOSE_WARNING_ENABLED", True),
        virtual_ai_pre_close_min_confidence=max(0.0, min(100.0, _float("VIRTUAL_AI_PRE_CLOSE_MIN_CONFIDENCE", 50.0))),
        virtual_close_warning_tp_ratio=max(0.1, min(0.99, _float("VIRTUAL_CLOSE_WARNING_TP_RATIO", 0.75))),
        virtual_close_warning_sl_ratio=max(0.1, min(0.99, _float("VIRTUAL_CLOSE_WARNING_SL_RATIO", 0.75))),
        virtual_close_warning_max_hold_ratio=max(0.1, min(0.99, _float("VIRTUAL_CLOSE_WARNING_MAX_HOLD_RATIO", 0.80))),
        telegram_bot_token=os.getenv("TELEGRAM_BOT_TOKEN", ""),
        telegram_chat_id=os.getenv("TELEGRAM_CHAT_ID", ""),
        telegram_enabled=_bool("TELEGRAM_ENABLED", False),
        allow_auto_patch=_bool("ALLOW_AUTO_PATCH", False),

        ai_budget_adaptive=_bool("AI_BUDGET_ADAPTIVE", True),
        ai_daily_target_points=max(0, _int("AI_DAILY_TARGET_POINTS", 33333)),
        ai_points_per_usd=max(1.0, _float("AI_POINTS_PER_USD", 33333.0)),
        ai_signal_input_cost_per_million_usd=max(0.0, _float("AI_SIGNAL_INPUT_COST_PER_MILLION_USD", 0.68)),
        ai_signal_output_cost_per_million_usd=max(0.0, _float("AI_SIGNAL_OUTPUT_COST_PER_MILLION_USD", 4.09)),
        ai_budget_min_threshold_multiplier=max(0.1, _float("AI_BUDGET_MIN_THRESHOLD_MULTIPLIER", 0.45)),
        ai_budget_max_threshold_multiplier=max(1.0, _float("AI_BUDGET_MAX_THRESHOLD_MULTIPLIER", 2.5)),
        ai_budget_min_top_n=max(1, _int("AI_BUDGET_MIN_TOP_N", 3)),
        ai_budget_max_top_n=max(1, _int("AI_BUDGET_MAX_TOP_N", 14)),
        signal_cooldown_minutes=max(0, _int("SIGNAL_COOLDOWN_MINUTES", 360)),
        signal_realert_multiplier=max(1.0, _float("SIGNAL_REALERT_MULTIPLIER", 2.0)),
        signal_exit_decay_ratio=max(0.05, _float("SIGNAL_EXIT_DECAY_RATIO", 0.5)),
        market_candles_enabled=_bool("MARKET_CANDLES_ENABLED", True),
        market_candle_intervals=os.getenv("MARKET_CANDLE_INTERVALS", "5m,15m,1h"),
        market_candle_lookback_minutes=max(5, _int("MARKET_CANDLE_LOOKBACK_MINUTES", 180)),
        market_candle_concurrency=max(1, _int("MARKET_CANDLE_CONCURRENCY", 4)),
        market_max_candle_coins=max(1, _int("MARKET_MAX_CANDLE_COINS", 12)),
        state_backup_enabled=_bool("STATE_BACKUP_ENABLED", True),
        state_backup_keep=max(1, _int("STATE_BACKUP_KEEP", 8)),

        swing_mode_enabled=_bool("SWING_MODE_ENABLED", True),
        swing_windows_hours=os.getenv("SWING_WINDOWS_HOURS", "2,6,24,72,168"),
        swing_min_score_for_ai=max(0.0, _float("SWING_MIN_SCORE_FOR_AI", 60.0)),
        swing_watch_score=max(0.0, _float("SWING_WATCH_SCORE", 65.0)),
        swing_strong_score=max(0.0, _float("SWING_STRONG_SCORE", 80.0)),
        swing_horizon_days=os.getenv("SWING_HORIZON_DAYS", "3-14"),
        wallet_performance_enabled=_bool("WALLET_PERFORMANCE_ENABLED", True),
        wallet_perf_horizons_hours=os.getenv("WALLET_PERF_HORIZONS_HOURS", "24,72,168"),
        wallet_perf_min_sample_size=max(1, _int("WALLET_PERF_MIN_SAMPLE_SIZE", 5)),
        wallet_perf_weight_in_signal=max(0.0, min(0.8, _float("WALLET_PERF_WEIGHT_IN_SIGNAL", 0.25))),
        wallet_perf_decay_days=max(1, _int("WALLET_PERF_DECAY_DAYS", 30)),
        wallet_perf_min_delta_notional=max(0.0, _float("WALLET_PERF_MIN_DELTA_NOTIONAL", 50000.0)),
    )
