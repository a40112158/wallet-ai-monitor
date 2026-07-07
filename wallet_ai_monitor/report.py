from __future__ import annotations

import html
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_ts(ts: int) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def _fmt_minutes(v: Any) -> str:
    if v is None:
        return "-"
    try:
        minutes = float(v)
    except (TypeError, ValueError):
        return "-"
    if minutes < 1:
        return "刚刚"
    if minutes < 60:
        return f"{minutes:.0f}分钟"
    hours = minutes / 60.0
    if hours < 48:
        return f"{hours:.1f}小时"
    return f"{hours / 24.0:.1f}天"


def _fmt_signal_state(s: dict[str, Any]) -> str:
    state = s.get("signal_state") or {}
    status = state.get("status") or s.get("signal_status") or "-"
    seen = state.get("seen_runs") or s.get("signal_seen_runs") or "-"
    age = _fmt_minutes(state.get("age_minutes") if state else s.get("signal_age_minutes"))
    cool = _fmt_minutes(state.get("cooldown_remaining_minutes") if state else s.get("cooldown_remaining_minutes"))
    ratio = state.get("amount_change_ratio") if state else s.get("amount_change_ratio")
    ratio_txt = "-" if ratio is None else f"{float(ratio):.2f}x"
    return f"{status} / 第{seen}轮 / 持续{age} / 冷却剩余{cool} / 金额变化{ratio_txt}"


def write_reports(
    report_dir: Path,
    ts: int,
    signals: list[dict[str, Any]],
    pnl_rows: list[dict[str, Any]],
    ai_result: dict[str, Any],
    *,
    exit_events: list[dict[str, Any]] | None = None,
    lifecycle_events: list[dict[str, Any]] | None = None,
    run_meta: dict[str, Any] | None = None,
    virtual_rows: list[dict[str, Any]] | None = None,
    virtual_summary: dict[str, Any] | None = None,
    wallet_scores_rows: list[dict[str, Any]] | None = None,
) -> dict[str, Path]:
    """Write only the important report files.

    Kept in reports/:
    - latest_report.md: human-readable signal + virtual account report
    - latest_signals.json: machine-readable latest run data
    - wallet_scores.md/json: wallet classification
    - param_optimizer_latest.json: written by the parameter optimizer when it runs

    Removed from reports/: history dumps, CSV duplicates, optimizer patches/logs, and old per-run files.
    """
    report_dir.mkdir(parents=True, exist_ok=True)
    latest_md = report_dir / "latest_report.md"
    latest_json = report_dir / "latest_signals.json"
    wallet_scores_md = report_dir / "wallet_scores.md"
    wallet_scores_json = report_dir / "wallet_scores.json"

    exit_events = exit_events or []
    virtual_rows = virtual_rows or []
    lifecycle_events = lifecycle_events or []
    run_meta = run_meta or {}
    virtual_rows = virtual_rows or []
    virtual_summary = virtual_summary or {}
    wallet_scores_rows = wallet_scores_rows or []

    obj = {
        "ts": ts,
        "time": utc_ts(ts),
        "run_meta": run_meta,
        "signals": signals,
        "exit_events": exit_events,
        "lifecycle_events": lifecycle_events,
        "pnl": pnl_rows,
        "virtual_rows": virtual_rows,
        "virtual_summary": virtual_summary,
        "wallet_scores": wallet_scores_rows,
        "ai": ai_result,
    }
    latest_json.write_text(json.dumps(obj, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    md = render_markdown(
        ts,
        signals,
        pnl_rows,
        ai_result,
        exit_events=exit_events,
        lifecycle_events=lifecycle_events,
        run_meta=run_meta,
        virtual_rows=virtual_rows,
        virtual_summary=virtual_summary,
    )
    latest_md.write_text(md, encoding="utf-8")

    write_wallet_score_reports(
        wallet_scores_md,
        wallet_scores_json,
        wallet_scores_rows,
        ts=ts,
        min_sample_size=(run_meta or {}).get("wallet_perf_min_sample_size"),
    )
    cleanup_unimportant_reports(report_dir)

    return {
        "latest_md": latest_md,
        "latest_json": latest_json,
        "wallet_scores_md": wallet_scores_md,
        "wallet_scores_json": wallet_scores_json,
    }



def write_wallet_score_reports(
    md_path: Path,
    json_path: Path,
    rows: list[dict[str, Any]],
    *,
    ts: int,
    min_sample_size: int | None = None,
) -> None:
    """Write standalone wallet classification reports for direct GitHub viewing."""
    payload = {
        "ts": ts,
        "time": utc_ts(ts),
        "note": "Wallet rows appear after at least one evaluated 24h/72h/168h sample. NEW means sample size is still below the configured minimum.",
        "min_sample_size": min_sample_size,
        "wallets": rows,
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    lines = ["# 钱包分类 / 胜率评分", "", f"Time: **{utc_ts(ts)}**", ""]
    lines += [
        "## 怎么看",
        "",
        "- `grade=S/A`：历史表现较好的钱包，信号里出现时应提高关注。",
        "- `grade=B`：普通可参考。",
        "- `grade=C/D`：噪音或低质量钱包，信号里出现时应降权。",
        "- `grade=NEW`：已经有样本，但样本数还不够，暂时不能下结论。",
        "",
    ]
    if min_sample_size:
        lines.append(f"- 当前最低有效样本数：`{min_sample_size}`。少于这个数量会显示 `NEW`。")
        lines.append("")
    if not rows:
        lines += [
            "## 暂无可分类钱包",
            "",
            "原因通常是：",
            "",
            "1. 胜率层刚启用，还没有等到 24h / 72h / 168h 的结果回填。",
            "2. 钱包动作金额低于 `WALLET_PERF_MIN_DELTA_NOTIONAL`，没有纳入样本。",
            "3. 还没有出现足够的开仓/加仓动作。",
            "",
            "继续运行一段时间后，这里会自动出现 S/A/B/C/D/NEW 分类。",
            "",
        ]
        md_path.write_text("\n".join(lines), encoding="utf-8")
        return

    buckets: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        buckets.setdefault(str(row.get("quality_grade") or "UNKNOWN"), []).append(row)

    for grade in ["S", "A", "B", "C", "D", "NEW", "UNKNOWN"]:
        items = buckets.get(grade) or []
        if not items:
            continue
        lines += [f"## {grade} 级钱包", ""]
        lines.append("| wallet | group | score | trades | win24 | avg24 | win72 | avg72 | win7d | avg7d |")
        lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for w in items[:200]:
            lines.append(
                f"| {_mask_wallet(str(w.get('wallet') or ''))} | {w.get('wallet_group') or ''} | "
                f"{float(w.get('score') or 0):.2f} | {int(w.get('trades') or 0)} | "
                f"{_fmt_rate(w.get('win_rate_24h'))} | {_fmt_pct(w.get('avg_pnl_24h'))} | "
                f"{_fmt_rate(w.get('win_rate_72h'))} | {_fmt_pct(w.get('avg_pnl_72h'))} | "
                f"{_fmt_rate(w.get('win_rate_168h'))} | {_fmt_pct(w.get('avg_pnl_168h'))} |"
            )
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")


IMPORTANT_REPORT_FILES = {
    "latest_report.md",
    "latest_signals.json",
    "wallet_scores.md",
    "wallet_scores.json",
    "param_optimizer_latest.json",
}


def cleanup_unimportant_reports(report_dir: Path) -> int:
    """Remove old/noisy report artifacts so the GitHub reports folder stays readable."""
    removed = 0
    if not report_dir.exists():
        return removed
    for path in list(report_dir.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(report_dir).as_posix()
        if "/" in rel or path.name not in IMPORTANT_REPORT_FILES:
            try:
                path.unlink()
                removed += 1
            except FileNotFoundError:
                pass
    # Remove empty subdirectories such as reports/history.
    for d in sorted([p for p in report_dir.rglob("*") if p.is_dir()], key=lambda p: len(p.parts), reverse=True):
        try:
            d.rmdir()
        except OSError:
            pass
    return removed


def prune_old_reports(report_dir: Path, before_ts: int) -> int:
    # Minimal-report mode has no per-run history to prune; just keep the folder clean.
    return cleanup_unimportant_reports(report_dir)


def render_markdown(
    ts: int,
    signals: list[dict[str, Any]],
    pnl_rows: list[dict[str, Any]],
    ai_result: dict[str, Any],
    *,
    exit_events: list[dict[str, Any]] | None = None,
    lifecycle_events: list[dict[str, Any]] | None = None,
    run_meta: dict[str, Any] | None = None,
    virtual_rows: list[dict[str, Any]] | None = None,
    virtual_summary: dict[str, Any] | None = None,
) -> str:
    exit_events = exit_events or []
    virtual_rows = virtual_rows or []
    lifecycle_events = lifecycle_events or []
    run_meta = run_meta or {}
    virtual_rows = virtual_rows or []
    virtual_summary = virtual_summary or {}
    lines = ["# 钱包合约信号报告", "", f"Time: **{utc_ts(ts)}**", ""]
    if run_meta:
        lines += [
            "## 运行状态",
            "",
            f"- 钱包：总数 {run_meta.get('wallets_total')}，本轮扫描 {run_meta.get('wallets_scanned')}，offset={run_meta.get('scan_offset')}，next={run_meta.get('next_scan_offset')}",
            f"- 请求：成功 {run_meta.get('wallets_succeeded', run_meta.get('wallets_scanned'))}，失败 {run_meta.get('wallets_failed', 0)}（失败钱包保留旧基线）",
            f"- 基线钱包：{run_meta.get('baseline_wallets')}，本轮 warmup 钱包：{run_meta.get('warmup_wallets')}，变动事件：{run_meta.get('deltas')}",
            f"- AI 输入信号：{run_meta.get('ai_input_signals')}，虚拟开仓：{run_meta.get('virtual_opened')}，动态评分钱包：{run_meta.get('scored_wallets')}",
            f"- 钱包胜率层：enabled={run_meta.get('wallet_performance_enabled')}，新记录={run_meta.get('wallet_perf_events_recorded')}，本轮评估={run_meta.get('wallet_perf_outcomes_updated')}，窗口={run_meta.get('wallet_perf_horizons_hours')}h",
            f"- AI预算：mode={run_meta.get('budget_mode')}，今日估算 {run_meta.get('budget_estimated_points_today')}/{run_meta.get('budget_daily_target_points')} points，阈值倍率={run_meta.get('budget_threshold_multiplier')}，AI阈值=${float(run_meta.get('adaptive_ai_min_delta') or 0):,.0f}",
            f"- 市场确认：K线币数 {run_meta.get('market_candle_coins')}，生命周期事件 {run_meta.get('lifecycle_events')}，冷却合并 {run_meta.get('suppressed_signals')}",
            f"- 信号状态：NEW={run_meta.get('signal_new', 0)}，RE_ALERT={run_meta.get('signal_realerts', 0)}，REPEAT={run_meta.get('signal_repeats', 0)}，追踪状态={run_meta.get('signal_states_tracked', 0)}",
            f"- 中长期模式：{run_meta.get('swing_mode')}，窗口={run_meta.get('swing_windows_hours')}h，强候选={run_meta.get('swing_strong_candidates')}，观察候选={run_meta.get('swing_watch_candidates')}",
            "",
        ]
        health = run_meta.get('health_24h') or {}
        if health:
            lines += [
                "### 24h运行健康",
                "",
                f"- runs={health.get('runs')}，signals={health.get('signals_count')}，avg_duration={float(health.get('avg_duration_sec') or 0):.1f}s，AI calls={health.get('ai_calls')}，AI estimated points={health.get('ai_estimated_points')}",
                "",
            ]
        wallet_perf_summary = run_meta.get("wallet_perf_summary") or []
        lines += ["### 钱包分类/胜率", ""]
        lines.append("- 完整分类文件：`reports/wallet_scores.md`、`reports/wallet_scores.json`。")
        if wallet_perf_summary:
            lines.append("")
            lines.append("| wallet | group | grade | score | trades | win72 | avg72 | win7d | avg7d |")
            lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|")
            for w in wallet_perf_summary[:10]:
                lines.append(
                    f"| {_mask_wallet(str(w.get('wallet') or ''))} | {w.get('wallet_group') or ''} | {w.get('quality_grade') or '-'} | "
                    f"{float(w.get('score') or 0):.2f} | {int(w.get('trades') or 0)} | "
                    f"{_fmt_rate(w.get('win_rate_72h'))} | {_fmt_pct(w.get('avg_pnl_72h'))} | "
                    f"{_fmt_rate(w.get('win_rate_168h'))} | {_fmt_pct(w.get('avg_pnl_168h'))} |"
                )
        else:
            lines.append("")
            lines.append("- 当前还没有可分类钱包。通常是胜率层刚启用，还没等到 24h/72h/168h 结果回填。")
        lines.append("")
    if ai_result.get("summary"):
        cached = "（缓存）" if ai_result.get("cached") else ""
        lines += [f"## AI 总结{cached}", "", str(ai_result.get("summary")), ""]
    elif ai_result.get("reason"):
        lines += ["## AI 状态", "", str(ai_result.get("reason")), ""]


    if signals:
        strong_long = [s for s in signals if s.get("side") == "LONG" and float((s.get("swing") or {}).get("score") or 0) >= 80]
        strong_short = [s for s in signals if s.get("side") == "SHORT" and float((s.get("swing") or {}).get("score") or 0) >= 80]
        watch = [s for s in signals if 65 <= float((s.get("swing") or {}).get("score") or 0) < 80]
        weak = [s for s in signals if float((s.get("swing") or {}).get("score") or 0) < 65]
        lines += ["## 中长期合约开单候选池", ""]
        if strong_long:
            lines += ["### 开多强候选", ""]
            for s in strong_long[:8]:
                ai = s.get("ai") or {}
                lines.append(f"- **{s['coin']} LONG** [{_fmt_signal_state(s)}] swing={s.get('swing_score')} AI={ai.get('action','-')} conf={_fmt_pct(s.get('ai_confidence'))} AI分={s.get('ai_score','-')} 综合={s.get('final_score','-')} delta=${s['total_delta_notional']:,.0f} wallets={s['wallet_count']} q={_fmt_quality(s)} horizon={(s.get('swing') or {}).get('horizon_days')}")
        if strong_short:
            lines += ["", "### 开空强候选", ""]
            for s in strong_short[:8]:
                ai = s.get("ai") or {}
                lines.append(f"- **{s['coin']} SHORT** [{_fmt_signal_state(s)}] swing={s.get('swing_score')} AI={ai.get('action','-')} conf={_fmt_pct(s.get('ai_confidence'))} AI分={s.get('ai_score','-')} 综合={s.get('final_score','-')} delta=${s['total_delta_notional']:,.0f} wallets={s['wallet_count']} q={_fmt_quality(s)} horizon={(s.get('swing') or {}).get('horizon_days')}")
        if watch:
            lines += ["", "### 观察候选", ""]
            for s in watch[:10]:
                lines.append(f"- **{s['coin']} {s['side']}** [{_fmt_signal_state(s)}] swing={s.get('swing_score')} bucket={s.get('swing_bucket')} AI分={s.get('ai_score','-')} 综合={s.get('final_score','-')} delta=${s['total_delta_notional']:,.0f} q={_fmt_quality(s)} risk={','.join(s.get('risk_tags') or [])}")
        if weak:
            lines += ["", "### 过滤/短线噪音", ""]
            for s in weak[:8]:
                lines.append(f"- {s['coin']} {s['side']} [{_fmt_signal_state(s)}] swing={s.get('swing_score')}：中长期条件不足，默认不作为主开单候选。")
        lines.append("")

    if not signals:
        lines += ["## 本轮开仓/加仓信号", "", "本轮没有达到阈值的开多/开空信号。", ""]
    else:
        lines += ["## 本轮开仓/加仓信号", ""]
        for i, s in enumerate(signals, 1):
            ai = s.get("ai") or {}
            conf = s.get("ai_confidence")
            conf_txt = "-" if conf is None else f"{conf:.0f}"
            lines += [
                f"### {i}. {s['coin']} {s['direction']} / Swing {s.get('swing_score', '-')} / AI评分 {s.get('ai_score', '-')} / 综合 {s.get('final_score', '-')} / AI置信度 {conf_txt}",
                "",
                f"- 钱包数：{s['wallet_count']}，分组：{s.get('groups')}，事件：{s.get('events')}，中长期桶：{s.get('swing_bucket', '-')}",
                f"- 新增/加仓名义金额：${s['total_delta_notional']:,.0f}，最大单钱包：${s['max_wallet_delta_notional']:,.0f}",
                f"- 标记价：{s.get('mark_px')}，均价：{s.get('avg_entry_px')}，权重分：{s.get('weighted_score')}，净偏向分：{s.get('net_bias_score')}",
                f"- AI独立评分：{s.get('ai_score', '-')}，规则评分：{s.get('rule_score', s.get('swing_score', '-'))}，综合开仓评分：{s.get('final_score', '-')}，评分来源：{s.get('score_source', '-')}",
                f"- 信号状态：{_fmt_signal_state(s)}",
                f"- 钱包质量：{_fmt_quality(s)}，高质量钱包={s.get('high_quality_wallet_count', 0)}，低质量钱包={s.get('low_quality_wallet_count', 0)}，72h胜率={_fmt_rate(s.get('weighted_win_rate_72h'))}，7d胜率={_fmt_rate(s.get('weighted_win_rate_168h'))}",
            ]
            if s.get("opposite_delta_notional"):
                lines.append(f"- 多空冲突：{s.get('conflict_level')}，反向金额=${float(s.get('opposite_delta_notional') or 0):,.0f}，冲突比={s.get('conflict_ratio')}")
            market = s.get("market") or {}
            if market:
                lines.append(f"- 市场：funding={market.get('funding')}，OI={market.get('open_interest')}，oracle={market.get('oracle_px')}，15m={((market.get('m15') or {}).get('return_pct'))}% ，1h={((market.get('h1') or {}).get('return_pct'))}% ，volRatio={((market.get('m15') or {}).get('volume_ratio'))}")
            swing = s.get("swing") or {}
            if swing:
                flow = swing.get("flow") or {}
                parts = swing.get("score_parts") or {}
                lines.append(f"- 中长期评分：{s.get('swing_score')} / 桶={s.get('swing_bucket')} / 周期={s.get('swing_horizon_days')}天")
                lines.append(f"- 钱包净流：2h=${float((flow.get('2h') or {}).get('total_delta_notional') or 0):,.0f}，6h=${float((flow.get('6h') or {}).get('total_delta_notional') or 0):,.0f}，24h=${float((flow.get('24h') or {}).get('total_delta_notional') or 0):,.0f}")
                lines.append(f"- 评分拆解：{parts}")
            if s.get("risk_tags"):
                lines.append(f"- 风险标签：{', '.join(s.get('risk_tags') or [])}")
            if ai:
                lines += [
                    f"- AI动作：{ai.get('action')}，AI评分：{ai.get('ai_score', s.get('ai_score', '-'))}",
                    f"- AI评分理由：{ai.get('ai_score_reason', s.get('ai_score_reason', '-'))}",
                    f"- AI评分因子：{ai.get('score_factors', s.get('score_factors', {}))}",
                    f"- 理由：{ai.get('reason')}",
                    f"- 风险：{ai.get('risks')}",
                    f"- 失效条件：{ai.get('invalidation')}",
                    f"- 入场区间：{ai.get('entry_zone', '-')}，建议持有：{ai.get('hold_period_days', '-')}天",
                ]
            top = s.get("wallets", [])[:3]
            if top:
                lines.append("- Top wallets：")
                for w in top:
                    lines.append(f"  - {w.get('wallet')} {w.get('group')} {w.get('event')} ${float(w.get('delta_notional') or 0):,.0f} score={float(w.get('wallet_score') or 1):.2f} grade={w.get('quality_grade', '-')} win72={_fmt_rate(w.get('win_rate_72h'))} avg72={_fmt_pct(w.get('avg_pnl_72h'))}")
            lines.append("")

    if exit_events:
        lines += ["## 减仓/平仓风险信号", ""]
        for e in exit_events[:8]:
            lines.append(f"- **{e['coin']} {e['direction']}** wallets={e['wallet_count']} amount=${e['total_delta_notional']:,.0f} score={e['weighted_score']} groups={e.get('groups')}")
        lines.append("")

    if lifecycle_events:
        lines += ["## 信号生命周期/冷却", ""]
        for e in lifecycle_events[:12]:
            state = e.get("signal_state") or {}
            seen = e.get("seen_runs", state.get("seen_runs", "-"))
            cool = _fmt_minutes(e.get("cooldown_remaining_minutes", state.get("cooldown_remaining_minutes")))
            ratio = e.get("amount_change_ratio", state.get("amount_change_ratio"))
            ratio_txt = "-" if ratio is None else f"{float(ratio):.2f}x"
            lines.append(
                f"- **{e.get('event')}** {e.get('coin')} {e.get('side')} 第{seen}轮 amount=${float(e.get('amount') or 0):,.0f} "
                f"prev={e.get('previous_signal_id')} exit_ratio={e.get('exit_ratio', '-')} amount_ratio={ratio_txt} "
                f"age={e.get('age_minutes', '-')}m cooldown_left={cool}"
            )
        lines.append("")

    if virtual_summary:
        capital = float(virtual_summary.get("account_capital_usd") or run_meta.get("virtual_account_capital_usd") or 0)
        equity = float(virtual_summary.get("equity_usd") or 0)
        open_notional = float(virtual_summary.get("open_notional_usd") or 0)
        open_margin = float(virtual_summary.get("open_margin_usd") or 0)
        available = float(virtual_summary.get("available_margin_usd") or virtual_summary.get("available_notional_usd") or 0)
        realized = float(virtual_summary.get("realized_pnl_usd") or 0)
        unrealized = float(virtual_summary.get("unrealized_pnl_usd") or 0)
        per_trade_cap = float(virtual_summary.get("per_trade_cap_usd") or run_meta.get("virtual_per_trade_cap_usd") or 0)
        total_pnl = realized + unrealized
        lines += ["## 虚拟跟单账户（总本金模式）", ""]
        lines.append("> 这部分才是模拟账户表现。它只做纸面验证，不会真实下单；AI 可决定开仓/平仓/仓位/杠杆，但杠杆被硬限制为不超过 10x。")
        lines.append("")
        lines.append(
            f"- 模拟本金：${capital:,.2f}，当前权益：${equity:,.2f}，总PnL：${total_pnl:,.2f} "
            f"（已实现 ${realized:,.2f} / 未实现 ${unrealized:,.2f}）"
        )
        lines.append(
            f"- 保证金占用：${open_margin:,.2f} / ${capital:,.2f} "
            f"（{float(virtual_summary.get('used_margin_pct') or 0):.1f}%），名义仓位：${open_notional:,.2f}，可用保证金：${available:,.2f}"
        )
        lines.append(
            f"- 仓位规则：最多 {virtual_summary.get('max_open_trades') or run_meta.get('virtual_max_open_trades') or '-'} 个未平仓，"
            f"AI仓位={'开' if virtual_summary.get('ai_position_sizing_enabled') else '关'}，AI平仓={'开' if virtual_summary.get('ai_trade_management_enabled') else '关'}，"
            f"最低综合开仓分 {float(run_meta.get('ai_min_final_score_for_open') or 0):.1f}，"
            f"最大杠杆 {float(virtual_summary.get('ai_max_leverage') or run_meta.get('ai_max_leverage') or 10):.1f}x，"
            f"单笔保证金上限 {float(virtual_summary.get('ai_max_margin_pct_per_trade') or run_meta.get('ai_max_margin_pct_per_trade') or 0):.1f}%，"
            f"总保证金上限 {float(virtual_summary.get('ai_max_total_margin_pct') or run_meta.get('ai_max_total_margin_pct') or 0):.1f}%；"
            f"不是每个仓位 ${capital:,.0f}"
        )
        lines.append(
            f"- 交易统计：总交易 {virtual_summary.get('total') or 0}，未平 {virtual_summary.get('open_count') or 0}，"
            f"已平 {virtual_summary.get('closed_count') or 0}，胜 {virtual_summary.get('wins') or 0}，负 {virtual_summary.get('losses') or 0}，"
            f"平仓胜率 {_fmt_rate(virtual_summary.get('closed_win_rate'))}，平均平仓收益 {_fmt_pct(virtual_summary.get('avg_closed_pnl_pct'))}"
        )
        if virtual_rows:
            warning_rows = [v for v in virtual_rows if v.get("close_warning") and v.get("status") == "OPEN"]
            if warning_rows:
                lines += ["", "### 准备平仓提示", ""]
                lines.append("> 这些不是已经平仓，而是 AI 或硬风控接近触发，下一轮可能平仓。")
                lines.append("")
                for v in warning_rows[:10]:
                    ai_part = ""
                    if v.get("ai_exit_confidence") is not None:
                        ai_part = f"，AI平仓置信度={float(v.get('ai_exit_confidence') or 0):.0f}，AI理由={str(v.get('ai_exit_reason') or '')[:80]}"
                    lines.append(
                        f"- **{v.get('coin')} {v.get('side')}** 准备平仓={v.get('close_warning_reason')}，"
                        f"当前PnL={float(v.get('pnl_pct') or 0):.2f}%，ROE={float(v.get('leveraged_roe_pct') or 0):.2f}%{ai_part}"
                    )
            lines.append("")
            lines.append("| id | coin | side | lev | margin | notional | entry | current | pnl% | ROE% | pnl_usd | status | 准备平仓 | reason | AI平仓 | MFE% | MAE% |")
            lines.append("|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|")
            for v in virtual_rows[:20]:
                pnl_usd = "" if v.get("pnl_usd") is None else f"{float(v.get('pnl_usd') or 0):.2f}"
                ai_exit = ""
                if v.get("ai_exit_confidence") is not None:
                    ai_exit = f"{float(v.get('ai_exit_confidence') or 0):.0f}: {str(v.get('ai_exit_reason') or '')[:40]}"
                warn = v.get("close_warning_reason") if v.get("close_warning") else ""
                lines.append(
                    f"| {v['id']} | {v['coin']} | {v['side']} | {float(v.get('leverage') or 1):.1f}x | "
                    f"${float(v.get('margin_usd') or 0):,.2f} | ${float(v.get('notional_usd') or 0):,.2f} | "
                    f"{v['entry_px']:.6g} | {v['current_px']:.6g} | {v['pnl_pct']:.2f} | {float(v.get('leveraged_roe_pct') or 0):.2f} | {pnl_usd} | "
                    f"{v['status']} | {warn} | {v.get('reason') or ''} | {ai_exit} | {v['mfe_pct']:.2f} | {v['mae_pct']:.2f} |"
                )
        lines.append("")

    if pnl_rows:
        rows_sorted = sorted(pnl_rows, key=lambda x: abs(float(x.get("pnl_pct") or 0)), reverse=True)
        wins = sum(1 for p in pnl_rows if float(p.get("pnl_pct") or 0) > 0)
        losses = sum(1 for p in pnl_rows if float(p.get("pnl_pct") or 0) <= 0)
        avg_pnl = sum(float(p.get("pnl_pct") or 0) for p in pnl_rows) / max(len(pnl_rows), 1)
        best = max((float(p.get("pnl_pct") or 0) for p in pnl_rows), default=0.0)
        worst = min((float(p.get("pnl_pct") or 0) for p in pnl_rows), default=0.0)
        lines += ["## 信号方向追踪（非模拟账户）", ""]
        lines.append("> 这部分只是追踪历史信号方向对不对，不占用虚拟本金，也不是实际开仓盈亏。模拟账户表现请看上面的“虚拟跟单账户”。")
        lines.append("")
        lines.append(
            f"- 追踪信号：{len(pnl_rows)} 条，方向正确 {wins}，方向错误 {losses}，"
            f"平均方向收益 {avg_pnl:.2f}%，最好 {best:.2f}%，最差 {worst:.2f}%"
        )
        lines.append("")
        lines.append("<details>")
        lines.append("<summary>展开查看最近/波动最大的信号方向追踪明细</summary>")
        lines.append("")
        lines.append("| signal_id | coin | side | entry | current | pnl% | 保守pnl% | MFE% | MAE% |")
        lines.append("|---:|---|---|---:|---:|---:|---:|---:|---:|")
        for p in rows_sorted[:30]:
            lines.append(
                f"| {p['signal_id']} | {p['coin']} | {p['side']} | {p['entry_px']:.6g} | {p['current_px']:.6g} | "
                f"{p['pnl_pct']:.2f} | {p.get('conservative_pnl_pct', 0):.2f} | "
                f"{p.get('mfe_pct', p['pnl_pct']):.2f} | {p.get('mae_pct', p['pnl_pct']):.2f} |"
            )
        lines.append("")
        lines.append("</details>")
        lines.append("")
    return "\n".join(lines)


def telegram_text(
    signals: list[dict[str, Any]],
    ai_result: dict[str, Any],
    *,
    exit_events: list[dict[str, Any]] | None = None,
    virtual_rows: list[dict[str, Any]] | None = None,
) -> str:
    """Build a compact HTML-safe Telegram message.

    The full JSON/CSV report is written under reports/. Telegram only
    needs the strongest candidates and must never fail the whole monitor run.
    """
    exit_events = exit_events or []
    virtual_rows = virtual_rows or []

    if not signals:
        text = "<b>Wallet Swing Contract Monitor</b>\n本轮无达标开仓信号。"
        if exit_events:
            text += "\n但有减仓/平仓事件：" + ", ".join(
                f"{html.escape(str(e.get('coin')))} {html.escape(str(e.get('direction')))} ${float(e.get('total_delta_notional') or 0):,.0f}"
                for e in exit_events[:4]
            )
        warnings = [v for v in virtual_rows if v.get("close_warning") and v.get("status") == "OPEN"]
        if warnings:
            text += "\n\n<b>准备平仓提示</b>"
            for v in warnings[:5]:
                text += f"\n{html.escape(str(v.get('coin')))} {html.escape(str(v.get('side')))} {html.escape(str(v.get('close_warning_reason')))} pnl={float(v.get('pnl_pct') or 0):.2f}%"
        return text

    strong = [s for s in signals if float((s.get("swing") or {}).get("score") or s.get("swing_score") or 0) >= 80]
    watch = [s for s in signals if 65 <= float((s.get("swing") or {}).get("score") or s.get("swing_score") or 0) < 80]
    selected = (strong + [s for s in watch if s not in strong] + [s for s in signals if s not in strong and s not in watch])[:8]

    lines = ["<b>Wallet Swing Contract Monitor</b>"]
    if strong:
        lines.append(f"强候选：{len(strong)} 个")
    if watch:
        lines.append(f"观察候选：{len(watch)} 个")
    if ai_result.get("summary"):
        lines.append(html.escape(str(ai_result.get("summary"))[:500]))

    for s in selected:
        ai = s.get("ai") or {}
        conf = "-" if s.get("ai_confidence") is None else f"{float(s.get('ai_confidence') or 0):.0f}"
        swing_score = s.get("swing_score", (s.get("swing") or {}).get("score", "-"))
        ai_score = s.get("ai_score", "-")
        final_score = s.get("final_score", "-")
        horizon = s.get("swing_horizon_days") or (s.get("swing") or {}).get("horizon_days") or "-"
        state_txt = _fmt_signal_state(s)
        conflict = f" conflict={s.get('conflict_level')}" if s.get("conflict_level") else ""
        lines.append(
            f"\n<b>{html.escape(str(s.get('coin')))} {html.escape(str(s.get('direction')))}</b> "
            f"swing={html.escape(str(swing_score))} AI分={html.escape(str(ai_score))} 综合={html.escape(str(final_score))} conf={conf}{html.escape(conflict)}\n"
            f"wallets={int(s.get('wallet_count') or 0)} "
            f"delta=${float(s.get('total_delta_notional') or 0):,.0f} "
            f"max=${float(s.get('max_wallet_delta_notional') or 0):,.0f}\n"
            f"state={html.escape(state_txt)}\n"
            f"horizon={html.escape(str(horizon))} quality={html.escape(_fmt_quality(s))} mark={html.escape(str(s.get('mark_px')))}\n"
            f"AI={html.escape(str(ai.get('action', '-')))} "
            f"reason={html.escape(str(ai.get('reason', '-'))[:220])}"
        )

    if exit_events:
        lines.append("\n<b>减仓/平仓</b> " + ", ".join(
            f"{html.escape(str(e.get('coin')))} {html.escape(str(e.get('direction')))} ${float(e.get('total_delta_notional') or 0):,.0f}"
            for e in exit_events[:4]
        ))
    return "\n".join(lines)



def _fmt_rate(v: Any) -> str:
    if v is None:
        return "-"
    try:
        return f"{float(v) * 100:.1f}%"
    except (TypeError, ValueError):
        return "-"


def _fmt_quality(s: dict[str, Any]) -> str:
    q = s.get("wallet_quality") or {}
    score = q.get("score", s.get("wallet_quality_score"))
    sampled = q.get("sampled_wallet_count")
    high = q.get("high_quality_wallet_count", s.get("high_quality_wallet_count"))
    try:
        score_txt = f"{float(score):.0f}"
    except (TypeError, ValueError):
        score_txt = "-"
    return f"{score_txt}/100 高质={high or 0} 样本={sampled or 0}"


def _mask_wallet(addr: str) -> str:
    if len(addr) < 14:
        return addr
    return addr[:8] + "..." + addr[-6:]


def _fmt_pct(v: Any) -> str:
    try:
        return f"{float(v):.2f}%"
    except (TypeError, ValueError):
        return "-"
