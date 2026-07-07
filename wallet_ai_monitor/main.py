from __future__ import annotations

import argparse
import asyncio
import logging
import time

from .ai import PoeAI, merge_ai
from .budget import decide_budget, estimate_points
from .config import load_settings
from .hyperliquid import HyperliquidClient
from .report import prune_old_reports, telegram_text, write_reports
from .signals import (
    aggregate_exit_events,
    aggregate_signals,
    ai_cache_key,
    apply_signal_lifecycle,
    attach_market_context,
    attach_swing_context,
    build_position_deltas,
    filter_signals_for_ai,
    update_open_signal_pnls,
)
from .storage import Store
from .telegram import send_telegram
from .wallets import load_wallets, shard_wallets

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("wallet_ai_monitor")

def _clamp_float(value, default: float, low: float, high: float) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        number = default
    return max(low, min(high, number))


def _ai_position_plan(signal: dict, settings, store: Store, fallback_notional: float) -> dict[str, float | str]:
    """Convert AI's open recommendation into a capped virtual position plan.

    The AI may suggest leverage and margin, but hard rails always win:
    - leverage <= AI_MAX_LEVERAGE and never above 10x
    - single-trade margin <= AI_MAX_MARGIN_PCT_PER_TRADE
    - total used margin <= AI_MAX_TOTAL_MARGIN_PCT
    """
    capital = float(settings.virtual_account_capital_usd or 0.0)
    ai = signal.get("ai") or {}
    conf = float(signal.get("ai_confidence") or 0.0)
    swing = signal.get("swing") or {}
    swing_score = float(swing.get("score") or 0.0)

    max_leverage = max(1.0, min(10.0, float(settings.ai_max_leverage or 10.0)))
    min_leverage = max(1.0, min(max_leverage, float(settings.ai_min_leverage or 1.0)))
    suggested_lev = _clamp_float(ai.get("suggested_leverage"), min_leverage, min_leverage, max_leverage)

    # If the model does not provide margin_pct, derive a conservative value from confidence/swing.
    default_margin_pct = 1.0
    if conf >= 90 and swing_score >= 85:
        default_margin_pct = 5.0
    elif conf >= 80 and swing_score >= 75:
        default_margin_pct = 3.0
    elif conf >= 70:
        default_margin_pct = 2.0

    min_margin_pct = max(0.1, float(settings.ai_min_margin_pct_per_trade or 0.5))
    max_margin_pct = max(min_margin_pct, float(settings.ai_max_margin_pct_per_trade or 8.0))
    margin_pct = _clamp_float(ai.get("margin_pct"), default_margin_pct, min_margin_pct, max_margin_pct)
    margin_usd = capital * margin_pct / 100.0 if capital > 0 else 0.0

    max_total_margin = capital * max(0.0, float(settings.ai_max_total_margin_pct or 35.0)) / 100.0
    used_margin = store.virtual_open_margin()
    remaining_margin = max(0.0, max_total_margin - used_margin)
    margin_usd = min(margin_usd, remaining_margin)

    # Keep backward compatibility: VIRTUAL_TRADE_NOTIONAL_USD can still cap the resulting notional.
    notional_usd = margin_usd * suggested_lev
    if settings.virtual_trade_notional_usd > 0:
        notional_usd = min(notional_usd, float(settings.virtual_trade_notional_usd))
        margin_usd = notional_usd / suggested_lev

    if fallback_notional > 0 and not settings.ai_position_sizing_enabled:
        notional_usd = min(fallback_notional, max(0.0, capital - store.virtual_open_notional()))
        suggested_lev = 1.0
        margin_usd = notional_usd

    reason = str(ai.get("position_reason") or ai.get("reason") or "")[:500]
    return {
        "leverage": suggested_lev,
        "margin_usd": margin_usd,
        "notional_usd": notional_usd,
        "margin_pct": (margin_usd / capital * 100.0) if capital > 0 else 0.0,
        "reason": reason,
    }


def _build_virtual_trade_context(open_rows: list[dict], mids: dict, signals: list[dict], lifecycle_events: list[dict], exit_events: list[dict]) -> dict:
    relevant = []
    for s in signals[:20]:
        relevant.append({
            "coin": s.get("coin"),
            "side": s.get("side"),
            "direction": s.get("direction"),
            "swing": s.get("swing"),
            "ai": s.get("ai"),
            "ai_confidence": s.get("ai_confidence"),
            "total_delta_notional": s.get("total_delta_notional"),
            "wallet_count": s.get("wallet_count"),
            "groups": s.get("groups"),
        })
    return {
        "mids": {str(k): float(v) for k, v in mids.items() if k in {str(r.get("coin")) for r in open_rows}},
        "recent_signals": relevant,
        "lifecycle_events": lifecycle_events[:20],
        "exit_events": exit_events[:20],
    }


def _apply_ai_composite_scores(signals: list[dict], settings) -> None:
    """Add AI-led composite scores to each signal.

    rule/swing_score is still kept for transparency, but final_score is led by the
    model's independent ai_score when AI scoring is enabled.
    """
    for s in signals:
        swing_score = _clamp_float(s.get("swing_score") or (s.get("swing") or {}).get("score"), 0.0, 0.0, 100.0)
        conf = _clamp_float(s.get("ai_confidence"), 0.0, 0.0, 100.0)
        ai_score_raw = s.get("ai_score")
        ai_score = None
        try:
            ai_score = float(ai_score_raw) if ai_score_raw is not None else None
        except (TypeError, ValueError):
            ai_score = None

        if settings.ai_scoring_enabled and ai_score is not None:
            ai_score = _clamp_float(ai_score, conf, 0.0, 100.0)
            ai_w = max(0.0, float(settings.ai_score_weight or 0.0))
            rule_w = max(0.0, float(settings.ai_rule_score_weight or 0.0))
            conf_w = max(0.0, float(settings.ai_confidence_score_weight or 0.0))
            total_w = ai_w + rule_w + conf_w
            if total_w <= 0:
                ai_w, rule_w, conf_w, total_w = 0.6, 0.25, 0.15, 1.0
            final_score = (ai_score * ai_w + swing_score * rule_w + conf * conf_w) / total_w
            source = "ai_led"
        else:
            # No AI score yet: keep rule score as fallback, but mark the source.
            final_score = swing_score
            source = "rule_fallback"

        s["rule_score"] = round(swing_score, 2)
        s["final_score"] = round(max(0.0, min(100.0, final_score)), 2)
        s["score_source"] = source


async def run_once(args: argparse.Namespace) -> int:
    started = time.time()
    ts = int(started)
    settings = load_settings()
    settings.state_dir.mkdir(parents=True, exist_ok=True)
    settings.report_dir.mkdir(parents=True, exist_ok=True)

    store = Store(settings.db_path)
    if settings.state_backup_enabled:
        backup_path = store.backup_database(ts, keep=settings.state_backup_keep)
        if backup_path:
            log.info("state backup saved: %s", backup_path)
    if not store.integrity_ok():
        log.error("SQLite integrity_check failed; stop before overwriting state")
        return 4
    try:
        return await _run_once_with_store(args, started, ts, settings, store)
    finally:
        store.close()


async def _run_once_with_store(args, started: float, ts: int, settings, store: Store) -> int:
    wallets_all = load_wallets(settings.data_dir, settings.smart_money_weight, settings.money_printer_weight)
    max_wallets = args.max_wallets if args.max_wallets is not None else settings.max_wallets_per_run
    offset = _resolve_scan_offset(args, settings, store)
    wallets = shard_wallets(wallets_all, max_wallets, offset)
    if not wallets:
        log.error("No wallet addresses loaded from data/*.txt")
        return 2

    candidate_addresses = [w.address for w in wallets]
    prev_latest = store.latest_map()
    baseline_wallets = store.wallets_with_latest(candidate_addresses)
    client = HyperliquidClient(
        settings.hl_info_url,
        timeout_seconds=settings.hl_timeout_seconds,
        retries=settings.hl_retries,
        concurrency=settings.hl_concurrency,
    )
    mids, asset_ctxs, positions, successful_wallets = await client.fetch_all_positions(
        wallets,
        batch_size=settings.hl_batch_size,
        batch_delay_seconds=settings.hl_batch_delay_seconds,
    )
    if not successful_wallets:
        log.error("All wallet requests failed; preserving previous state")
        return 3
    scanned_addresses = [address for address in candidate_addresses if address in successful_wallets]
    scanned_set = set(scanned_addresses)
    failed_wallets = len(candidate_addresses) - len(scanned_addresses)
    warmup_wallets = len(scanned_set - baseline_wallets)
    perf_outcomes_updated = store.update_wallet_perf_outcomes(ts, mids) if settings.wallet_performance_enabled else 0
    pre_scored_wallets = store.refresh_wallet_scores(ts, decay_days=settings.wallet_perf_decay_days, min_sample_size=settings.wallet_perf_min_sample_size) if settings.wallet_performance_enabled and perf_outcomes_updated else 0
    wallet_scores = store.wallet_score_map()
    wallet_performance = store.wallet_performance_map() if settings.wallet_performance_enabled else {}

    log.info(
        "wallets total=%d selected=%d succeeded=%d failed=%d offset=%d baseline=%d warmup=%d positions=%d mids=%d",
        len(wallets_all), len(wallets), len(scanned_addresses), failed_wallets, offset,
        len(baseline_wallets), warmup_wallets, len(positions), len(mids),
    )

    day_start = ts - (ts % 86400)
    estimated_points_today = store.estimated_ai_points_since(day_start)
    budget_decision = decide_budget(
        enabled=settings.ai_budget_adaptive,
        daily_target_points=settings.ai_daily_target_points,
        estimated_points_today=estimated_points_today,
        base_min_delta=settings.ai_min_total_delta_notional,
        base_top_n=settings.top_signals_for_ai,
        base_max_output_tokens=settings.ai_max_output_tokens,
        min_threshold_multiplier=settings.ai_budget_min_threshold_multiplier,
        max_threshold_multiplier=settings.ai_budget_max_threshold_multiplier,
        min_top_n=settings.ai_budget_min_top_n,
        max_top_n=settings.ai_budget_max_top_n,
    )
    adaptive_ai_min_delta = settings.ai_min_total_delta_notional * budget_decision.threshold_multiplier
    adaptive_top_n = budget_decision.top_n
    adaptive_max_tokens = budget_decision.max_output_tokens

    deltas = build_position_deltas(
        prev_latest,
        positions,
        scanned_wallets=scanned_set,
        baseline_wallets=baseline_wallets,
        wallet_scores=wallet_scores,
        wallet_performance=wallet_performance,
        wallet_perf_weight_in_signal=settings.wallet_perf_weight_in_signal,
        warmup_missing_wallets=settings.warmup_missing_wallets,
        mids=mids,
    )
    perf_horizons = [int(x.strip()) for x in settings.wallet_perf_horizons_hours.split(",") if x.strip().isdigit()]
    perf_events_recorded = store.record_wallet_perf_events(
        ts,
        deltas,
        horizons_hours=perf_horizons,
        min_delta_notional=settings.wallet_perf_min_delta_notional,
    ) if settings.wallet_performance_enabled else 0

    signals = aggregate_signals(
        deltas,
        min_delta_notional_usd=settings.min_delta_notional_usd,
        min_single_whale_delta_usd=settings.min_single_whale_delta_usd,
        min_wallet_count=settings.min_wallet_count,
        top_n=settings.top_signals_for_ai,
    )
    exit_events = aggregate_exit_events(deltas, min_delta_notional_usd=settings.min_delta_notional_usd, top_n=settings.top_signals_for_ai)

    candle_ctxs = {}
    if settings.market_candles_enabled and (signals or exit_events):
        candle_coins = []
        for item in [*signals, *exit_events]:
            coin = str(item.get("coin") or "")
            if coin and coin not in candle_coins:
                candle_coins.append(coin)
        candle_coins = candle_coins[:settings.market_max_candle_coins]
        intervals = [x.strip() for x in settings.market_candle_intervals.split(",") if x.strip()]
        candle_ctxs = await client.fetch_market_candles(
            candle_coins,
            intervals=intervals,
            lookback_minutes=settings.market_candle_lookback_minutes,
            concurrency=settings.market_candle_concurrency,
        )

    attach_market_context(signals, asset_ctxs, candle_ctxs)
    attach_market_context(exit_events, asset_ctxs, candle_ctxs)

    lifecycle_since = ts - settings.signal_cooldown_minutes * 60
    recent_lifecycle = store.recent_active_signals_for_lifecycle(lifecycle_since)
    raw_lifecycle_signals = list(signals)
    signals, lifecycle_events = apply_signal_lifecycle(
        signals,
        exit_events,
        recent_active=recent_lifecycle,
        now_ts=ts,
        cooldown_seconds=settings.signal_cooldown_minutes * 60,
        realert_multiplier=settings.signal_realert_multiplier,
        exit_decay_ratio=settings.signal_exit_decay_ratio,
    )
    signal_state_map = store.update_signal_state(
        ts,
        raw_lifecycle_signals,
        signals,
        lifecycle_events,
        cooldown_seconds=settings.signal_cooldown_minutes * 60,
    )

    swing_windows_hours = [int(x.strip()) for x in settings.swing_windows_hours.split(",") if x.strip().isdigit()]
    if settings.swing_mode_enabled and signals:
        historical_flow = store.recent_signal_flow_stats(ts, [h * 3600 for h in swing_windows_hours])
        attach_swing_context(
            signals,
            historical_flow,
            windows_hours=swing_windows_hours or [2, 6, 24],
            min_score_for_ai=settings.swing_min_score_for_ai,
            watch_score=settings.swing_watch_score,
            strong_score=settings.swing_strong_score,
            horizon_days=settings.swing_horizon_days,
        )

    ai_result = {"ok": False, "reason": "AI disabled", "signals": []}
    ai_ok = False
    ai_input = filter_signals_for_ai(
        signals,
        min_total_delta=adaptive_ai_min_delta,
        min_wallet_count=settings.ai_min_wallet_count_for_call,
        min_weighted_score=settings.ai_min_weighted_score_for_call,
        top_n=adaptive_top_n,
    )
    if settings.ai_enabled and settings.poe_api_key and ai_input:
        key = ai_cache_key(ai_input, settings.poe_model_signal)
        cached = store.get_ai_cache(key, max_age_seconds=settings.ai_cache_ttl_minutes * 60)
        if cached:
            ai_result = {**cached, "cached": True}
            merge_ai(signals, ai_result)
            ai_ok = bool(ai_result.get("ok"))
            store.record_ai_usage(
                ts=ts, model=settings.poe_model_signal, purpose="signal", usage=ai_result.get("usage"),
                estimated_points=0, cached=True, ok=ai_ok,
            )
        else:
            ai = PoeAI(
                settings.poe_api_key,
                settings.poe_base_url,
                settings.poe_model_signal,
                max_tokens=adaptive_max_tokens,
                temperature=settings.ai_temperature,
                timeout_seconds=settings.ai_timeout_seconds,
            )
            ai_result = await asyncio.to_thread(ai.analyze_signals, ai_input)
            merge_ai(signals, ai_result)
            ai_ok = bool(ai_result.get("ok"))
            usage = ai_result.get("usage") or {}
            estimated_points = estimate_points(
                prompt_tokens=usage.get("prompt_tokens"),
                completion_tokens=usage.get("completion_tokens"),
                input_cost_per_million_usd=settings.ai_signal_input_cost_per_million_usd,
                output_cost_per_million_usd=settings.ai_signal_output_cost_per_million_usd,
                points_per_usd=settings.ai_points_per_usd,
            )
            store.record_ai_usage(
                ts=ts, model=settings.poe_model_signal, purpose="signal", usage=usage,
                estimated_points=estimated_points, cached=False, ok=ai_ok,
            )
            if ai_ok:
                store.save_ai_cache(key, settings.poe_model_signal, ai_result)
    elif settings.ai_enabled and not settings.poe_api_key:
        ai_result = {"ok": False, "reason": "POE_API_KEY empty", "signals": []}
    elif settings.ai_enabled and not ai_input:
        ai_result = {"ok": False, "reason": "No significant signal met AI trigger", "signals": []}

    _apply_ai_composite_scores(signals, settings)

    # Persist latest after delta calculation so fresh shard baselines do not create fake signals.
    store.replace_latest_for_scanned_wallets(ts, positions, scanned_addresses)

    inserted_ids: list[int] = []
    signal_by_id: dict[int, dict] = {}
    for s in signals:
        sid = store.insert_signal(ts, s)
        inserted_ids.append(sid)
        signal_by_id[sid] = s

    # AI-controlled virtual open decisions. This remains paper trading only:
    # no exchange API keys and no real orders. AI can suggest leverage/margin, but
    # hard rails cap leverage at <=10x and margin at configured account limits.
    virtual_opened = 0
    virtual_per_trade_cap = 0.0
    if settings.virtual_trading_enabled:
        auto_slot_notional = settings.virtual_account_capital_usd / max(1, settings.virtual_max_open_trades)
        configured_cap = settings.virtual_trade_notional_usd if settings.virtual_trade_notional_usd > 0 else auto_slot_notional
        virtual_per_trade_cap = max(0.0, min(float(configured_cap), float(auto_slot_notional)))
        ranked_signal_ids = sorted(
            inserted_ids,
            key=lambda sid: (
                float(signal_by_id[sid].get("final_score") or 0),
                float(signal_by_id[sid].get("ai_confidence") or 0),
                float(signal_by_id[sid].get("swing_score") or 0),
            ),
            reverse=True,
        )
        for sid in ranked_signal_ids:
            if store.count_open_virtual_trades() >= settings.virtual_max_open_trades:
                break
            s = signal_by_id[sid]
            ai = s.get("ai") or {}
            action = str(ai.get("action") or "")
            conf = float(s.get("ai_confidence") or 0)
            final_score = float(s.get("final_score") or 0)
            if (
                action == s.get("direction")
                and conf >= settings.virtual_min_ai_confidence
                and final_score >= settings.ai_min_final_score_for_open
            ):
                plan = _ai_position_plan(s, settings, store, virtual_per_trade_cap)
                if float(plan["notional_usd"]) <= 0 or float(plan["margin_usd"]) <= 0:
                    continue
                if store.open_virtual_trade(
                    sid,
                    ts,
                    s,
                    float(plan["notional_usd"]),
                    leverage=float(plan["leverage"]),
                    margin_usd=float(plan["margin_usd"]),
                    ai_open_reason=str(plan["reason"]),
                ):
                    virtual_opened += 1

    since_ts = ts - settings.signal_ttl_hours * 3600
    store.expire_signals_before(since_ts)
    open_rows = store.recent_open_signals(since_ts)
    pnl_rows = update_open_signal_pnls(
        open_rows,
        mids,
        settings.default_leverage_for_pnl,
        fee_bps=settings.conservative_fee_bps,
        slippage_bps=settings.conservative_slippage_bps,
    )
    pnl_rows = store.save_signal_pnls(ts, pnl_rows)
    scored_wallets = store.refresh_wallet_scores(ts, decay_days=settings.wallet_perf_decay_days, min_sample_size=settings.wallet_perf_min_sample_size) if settings.wallet_performance_enabled else 0
    virtual_rows = []
    virtual_summary = {}
    ai_trade_result = {"ok": False, "reason": "AI trade management disabled", "decisions": []}
    ai_exit_decisions: dict[int, dict] = {}
    if settings.virtual_trading_enabled:
        open_virtual_rows = store.virtual_open_rows()
        if settings.ai_trade_management_enabled and settings.ai_enabled and settings.poe_api_key and open_virtual_rows:
            trade_ai = PoeAI(
                settings.poe_api_key,
                settings.poe_base_url,
                settings.poe_model_signal,
                max_tokens=settings.ai_trade_decision_max_tokens,
                temperature=settings.ai_temperature,
                timeout_seconds=settings.ai_timeout_seconds,
            )
            context = _build_virtual_trade_context(open_virtual_rows, mids, signals, lifecycle_events, exit_events)
            ai_trade_result = await asyncio.to_thread(trade_ai.manage_virtual_trades, open_virtual_rows, context)
            trade_usage = ai_trade_result.get("usage") or {}
            trade_points = estimate_points(
                prompt_tokens=trade_usage.get("prompt_tokens"),
                completion_tokens=trade_usage.get("completion_tokens"),
                input_cost_per_million_usd=settings.ai_signal_input_cost_per_million_usd,
                output_cost_per_million_usd=settings.ai_signal_output_cost_per_million_usd,
                points_per_usd=settings.ai_points_per_usd,
            )
            store.record_ai_usage(
                ts=ts, model=settings.poe_model_signal, purpose="trade_exit", usage=trade_usage,
                estimated_points=trade_points, cached=False, ok=bool(ai_trade_result.get("ok")),
            )
            if ai_trade_result.get("ok"):
                ai_exit_decisions = {int(d.get("id")): d for d in ai_trade_result.get("decisions", []) if isinstance(d, dict) and d.get("id") is not None}

        virtual_rows = store.update_virtual_trades(
            ts,
            mids,
            take_profit_pct=settings.virtual_take_profit_pct,
            stop_loss_pct=settings.virtual_stop_loss_pct,
            max_hold_seconds=settings.virtual_max_hold_hours * 3600,
            ai_exit_decisions=ai_exit_decisions,
            ai_close_min_confidence=settings.ai_close_min_confidence,
            close_warning_enabled=settings.virtual_close_warning_enabled,
            ai_pre_close_min_confidence=settings.virtual_ai_pre_close_min_confidence,
            close_warning_tp_ratio=settings.virtual_close_warning_tp_ratio,
            close_warning_sl_ratio=settings.virtual_close_warning_sl_ratio,
            close_warning_max_hold_ratio=settings.virtual_close_warning_max_hold_ratio,
        )
        virtual_summary = store.virtual_summary(settings.virtual_account_capital_usd)
        virtual_summary["per_trade_cap_usd"] = virtual_per_trade_cap
        virtual_summary["max_open_trades"] = settings.virtual_max_open_trades
        virtual_summary["ai_trade_management_enabled"] = settings.ai_trade_management_enabled
        virtual_summary["ai_position_sizing_enabled"] = settings.ai_position_sizing_enabled
        virtual_summary["ai_max_leverage"] = settings.ai_max_leverage
        virtual_summary["ai_max_margin_pct_per_trade"] = settings.ai_max_margin_pct_per_trade
        virtual_summary["ai_max_total_margin_pct"] = settings.ai_max_total_margin_pct
        virtual_summary["ai_trade_result"] = ai_trade_result

    next_offset = _next_scan_offset(offset, len(wallets), len(wallets_all), max_wallets)
    if settings.auto_shard_rotation and args.offset is None and max_wallets and max_wallets < len(wallets_all):
        store.set_meta("next_scan_offset", next_offset)

    wallet_scores_rows = store.wallet_scores_rows(limit=2000) if settings.wallet_performance_enabled else []

    run_meta = {
        "wallets_total": len(wallets_all),
        "wallets_scanned": len(wallets),
        "wallets_succeeded": len(scanned_addresses),
        "wallets_failed": failed_wallets,
        "hl_concurrency": settings.hl_concurrency,
        "hl_batch_size": settings.hl_batch_size,
        "hl_batch_delay_seconds": settings.hl_batch_delay_seconds,
        "scan_offset": offset,
        "next_scan_offset": next_offset,
        "baseline_wallets": len(baseline_wallets),
        "warmup_wallets": warmup_wallets,
        "deltas": len(deltas),
        "exit_events": len(exit_events),
        "ai_input_signals": len(ai_input),
        "virtual_opened": virtual_opened,
        "virtual_account_capital_usd": settings.virtual_account_capital_usd,
        "virtual_per_trade_cap_usd": virtual_per_trade_cap,
        "virtual_max_open_trades": settings.virtual_max_open_trades,
        "scored_wallets": scored_wallets,
        "wallet_performance_enabled": settings.wallet_performance_enabled,
        "wallet_perf_events_recorded": perf_events_recorded,
        "wallet_perf_outcomes_updated": perf_outcomes_updated,
        "wallet_perf_pre_scored": pre_scored_wallets,
        "wallet_perf_horizons_hours": settings.wallet_perf_horizons_hours,
        "wallet_perf_min_sample_size": settings.wallet_perf_min_sample_size,
        "wallet_perf_summary": store.wallet_perf_summary(limit=10) if settings.wallet_performance_enabled else [],
        "wallet_scores_exported": len(wallet_scores_rows) if settings.wallet_performance_enabled else 0,
        "lifecycle_events": len(lifecycle_events),
        "suppressed_signals": sum(1 for e in lifecycle_events if e.get("event") == "COOLDOWN_MERGED"),
        "signal_states_tracked": len(signal_state_map) if 'signal_state_map' in locals() else 0,
        "signal_new": sum(1 for s in signals if s.get("signal_status") == "NEW_SIGNAL"),
        "signal_realerts": sum(1 for s in signals if s.get("signal_status") == "RE_ALERT"),
        "signal_repeats": sum(1 for s in signals if s.get("signal_status") == "ACTIVE_REPEAT"),
        "market_candle_coins": len(candle_ctxs),
        "budget_mode": budget_decision.mode,
        "budget_usage_ratio": budget_decision.usage_ratio,
        "budget_estimated_points_today": budget_decision.estimated_points_today,
        "budget_daily_target_points": budget_decision.daily_target_points,
        "budget_threshold_multiplier": budget_decision.threshold_multiplier,
        "budget_top_n": budget_decision.top_n,
        "adaptive_ai_min_delta": round(adaptive_ai_min_delta, 2),
        "health_24h": store.run_health_summary(ts - 86400),
        "swing_mode": settings.swing_mode_enabled,
        "swing_windows_hours": settings.swing_windows_hours,
        "swing_strong_candidates": sum(1 for s in signals if float((s.get("swing") or {}).get("score") or 0) >= settings.swing_strong_score),
        "swing_watch_candidates": sum(1 for s in signals if settings.swing_watch_score <= float((s.get("swing") or {}).get("score") or 0) < settings.swing_strong_score),
    }
    paths = write_reports(
        settings.report_dir,
        ts,
        signals,
        pnl_rows,
        ai_result,
        exit_events=exit_events,
        lifecycle_events=lifecycle_events,
        run_meta=run_meta,
        virtual_rows=virtual_rows,
        virtual_summary=virtual_summary,
        wallet_scores_rows=wallet_scores_rows,
    )
    pruned_rows = store.prune_history(ts - settings.data_retention_days * 86400)
    pruned_reports = prune_old_reports(settings.report_dir, ts - settings.report_retention_days * 86400)
    if pruned_rows or pruned_reports:
        log.info("retention cleanup db_rows=%d report_files=%d", pruned_rows, pruned_reports)

    if settings.telegram_enabled and settings.telegram_bot_token and settings.telegram_chat_id:
        await send_telegram(settings.telegram_bot_token, settings.telegram_chat_id, telegram_text(signals, ai_result, exit_events=exit_events, virtual_rows=virtual_rows))

    duration = time.time() - started
    store.log_run(
        ts=ts,
        wallets_total=len(wallets_all),
        wallets_scanned=len(wallets),
        positions_count=len(positions),
        signals_count=len(signals),
        ai_enabled=settings.ai_enabled,
        ai_ok=ai_ok,
        duration_sec=duration,
        note=f"report={paths.get('latest_md', paths['latest_json'])} offset={offset} next={next_offset} warmup={warmup_wallets}",
    )
    log.info("done signals=%d exits=%d ai_ok=%s duration=%.1fs report=%s", len(signals), len(exit_events), ai_ok, duration, paths.get("latest_md", paths["latest_json"]))
    return 0


def _resolve_scan_offset(args: argparse.Namespace, settings, store: Store) -> int:
    if args.offset is not None:
        return max(0, int(args.offset))
    max_wallets = args.max_wallets if args.max_wallets is not None else settings.max_wallets_per_run
    if settings.auto_shard_rotation and max_wallets and max_wallets > 0:
        try:
            return max(0, int(store.get_meta("next_scan_offset", str(settings.scan_offset)) or settings.scan_offset))
        except ValueError:
            return settings.scan_offset
    return settings.scan_offset


def _next_scan_offset(offset: int, scanned: int, total: int, max_wallets: int) -> int:
    if not max_wallets or max_wallets <= 0 or max_wallets >= total:
        return 0
    return (offset + scanned) % max(total, 1)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Hyperliquid wallet monitor with Poe AI analysis")
    p.add_argument("--max-wallets", type=int, default=None, help="Override MAX_WALLETS_PER_RUN")
    p.add_argument("--offset", type=int, default=None, help="Override SCAN_OFFSET")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    raise SystemExit(asyncio.run(run_once(args)))


if __name__ == "__main__":
    main()
