"""主编排。"""
from __future__ import annotations

import time

from . import reporting, telegram
from .ai_client import AIClient
from .ai_scoring import score_signals, _fallback
from .config import load_config
from .flow_ledger import record as flow_record, windows_for
from .hyperliquid_client import scan_wallets
from .logging_utils import get_logger
from .market_data import fetch_market_ctx
from .param_optimizer import load_overrides, run_optimizer
from .position_manager import manage_positions
from .scoring import compute_swing_score
from .signal_lifecycle import update_lifecycle
from .signals import build_signals, diff_positions, filter_signals
from .state_store import load_state, save_state
from .timeutil import fmt_bj
from .virtual_account import mark_to_market, try_open_trades
from .wallet_performance import record_events, resolve_and_score
from .wallets import load_wallets, select_wallets

log = get_logger()


def run(force_param_optimizer: bool = False) -> None:
    reporting.ensure_reports_dir()
    now = time.time()
    log.info("运行开始(北京): %s", fmt_bj(now))

    cfg = load_config()
    cfg.apply_overrides(load_overrides())
    state = load_state()

    wallets_meta = load_wallets(cfg.wallet_dir)
    if not wallets_meta:
        reporting.write_diagnostic_report("未加载到任何钱包，请检查 wallets/ 目录。")
        save_state(state)
        return
    addrs = select_wallets(wallets_meta, cfg.max_wallets_per_run,
                           cfg.auto_shard_rotation)
    log.info("将扫描 %d 个钱包", len(addrs))

    curr_positions, scan_stats = scan_wallets(addrs, cfg)

    success_rate = scan_stats.get("success_rate", 0.0)
    if scan_stats.get("success", 0) == 0 or success_rate < cfg.hl_min_success_rate:
        msg = (
            "Hyperliquid 扫描成功率过低，本轮不覆盖 state.json，避免把 API 失败误判为空仓。\n\n"
            f"- 应扫钱包: {scan_stats.get('total', 0)}\n"
            f"- 成功: {scan_stats.get('success', 0)}\n"
            f"- 失败: {scan_stats.get('failed', 0)}\n"
            f"- 成功率: {success_rate:.2%}\n"
            f"- 最低要求: {cfg.hl_min_success_rate:.2%}\n"
            f"- 失败样本: {scan_stats.get('failed_wallets_sample', [])}"
        )
        reporting.write_diagnostic_report(msg)
        state["run_history"].append({
            "ts": now, "ts_bj": fmt_bj(now), "wallets": len(addrs),
            "signals": 0, "opened": 0, "closed": 0,
            "scan_success_rate": success_rate, "skipped_state_update": True})
        save_state(state)
        log.warning(msg)
        return

    market = fetch_market_ctx(cfg)

    prev_positions = state["last_positions"]
    ok_wallets = set(scan_stats.get("ok_wallets", []))
    all_events: dict[str, list[dict]] = {}
    for addr in addrs:
        if addr not in ok_wallets:
            continue
        events = diff_positions(prev_positions.get(addr, {}),
                                curr_positions.get(addr, {}))
        if events:
            all_events[addr] = events

    record_events(all_events, market, state["wallet_perf"], now)
    wallet_quality = resolve_and_score(state["wallet_perf"], cfg, now)

    raw_signals = build_signals(all_events, wallets_meta, wallet_quality, cfg)
    flow_record(raw_signals, state["flow_ledger"], now)

    passed, noise = filter_signals(raw_signals, cfg)
    update_lifecycle(passed, state["signal_lifecycle"], cfg)

    for s in passed:
        lc = state["signal_lifecycle"].get(f"{s['coin']}:{s['direction']}", {})
        fw = windows_for(s["coin"], s["direction"], state["flow_ledger"], now)
        s.update(compute_swing_score(s, market, lc, fw, cfg))

    passed.sort(key=lambda x: x["swing_score"], reverse=True)

    ai = AIClient(cfg, state["ai_cache"], state["ai_budget"])
    ai_input = [s for s in passed[:cfg.top_signals_for_ai]
                if s["delta_notional"] >= cfg.ai_min_total_delta_notional
                and s["wallet_count"] >= cfg.ai_min_wallet_count_for_call]
    if not ai_input and passed:
        ai_input = passed[:3]
    score_signals(ai_input, market, ai, cfg)

    for s in passed:
        if "final_score" not in s:
            _fallback(s, cfg)

    opened = try_open_trades(passed, market, state, cfg)
    acc = state["virtual_account"]
    mark_to_market(acc, market)

    closed_now, close_warnings = manage_positions(acc, market, passed, ai, cfg)
    mark_to_market(acc, market)

    if cfg.param_optimizer_enabled or force_param_optimizer:
        run_optimizer(state, cfg)

    ctx = {
        "cfg": cfg,
        "wallets_scanned": len(addrs),
        "signals": passed,
        "noise_count": len(noise),
        "ai_stats": ai.stats,
        "ai_budget": state["ai_budget"],
        "ai_input_count": len(ai_input),
        "virtual_account": acc,
        "opened": opened,
        "closed_now": closed_now,
        "close_warnings": close_warnings,
        "scan_stats": scan_stats,
    }
    reporting.write_main_report(ctx)
    reporting.write_wallet_scores(state["wallet_perf"], wallets_meta)
    telegram.send_report(ctx, cfg)

    # 只覆盖成功读取的钱包；失败钱包保留上一轮快照，避免假减仓/假重新开仓。
    merged_positions = {addr: prev_positions.get(addr, {}) for addr in wallets_meta}
    for addr in ok_wallets:
        merged_positions[addr] = curr_positions.get(addr, {})
    state["last_positions"] = merged_positions
    state["run_history"].append({
        "ts": now, "ts_bj": fmt_bj(now), "wallets": len(addrs),
        "scan_success": scan_stats.get("success", 0),
        "scan_failed": scan_stats.get("failed", 0),
        "scan_success_rate": scan_stats.get("success_rate", 0.0),
        "signals": len(passed), "opened": len(opened),
        "closed": len(closed_now)})
    save_state(state)
    log.info("完成(北京 %s)：信号 %d，开仓 %d，平仓 %d",
             fmt_bj(), len(passed), len(opened), len(closed_now))
