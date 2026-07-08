"""报告生成（全北京时间）。"""
from __future__ import annotations

import json
import os

from .timeutil import fmt_bj

REPORTS = "reports"


def ensure_reports_dir() -> None:
    os.makedirs(REPORTS, exist_ok=True)
    open(os.path.join(REPORTS, ".gitkeep"), "a").close()


def write_diagnostic_report(msg: str) -> None:
    ensure_reports_dir()
    with open(os.path.join(REPORTS, "latest_report.md"), "w", encoding="utf-8") as f:
        f.write(f"# 诊断报告\n\n生成时间(北京): {fmt_bj()}\n\n{msg}\n")


def _fmt_usd(v):
    try:
        return f"${v:,.0f}"
    except (TypeError, ValueError):
        return "-"


def _fmt_flow(flow: dict) -> str:
    if not flow:
        return "-"
    return " ".join(f"{w}={_fmt_usd(flow.get(w))}"
                    for w in ("2h", "6h", "24h", "72h", "168h"))


def _sig_block(s: dict) -> str:
    lc = s.get("lifecycle", {})
    state_line = (f"state={s.get('state','-')} / 第{s.get('round','-')}轮 / "
                  f"持续{s.get('duration_hours','-')}小时 / "
                  f"冷却剩余{s.get('cooldown_remaining_min','-')}分 / "
                  f"金额变化{s.get('amount_change_x','-')}x")
    return "\n".join([
        f"### {s['coin']} {s['direction']}",
        f"- swing={s.get('swing_score')} bucket={s.get('swing_bucket')} "
        f"horizon={s.get('swing_horizon_days')}天",
        f"- AI分={s.get('ai_score')} 综合={s.get('final_score')} "
        f"conf={s.get('ai_confidence')}",
        f"- {state_line}",
        f"- 首次出现(北京): {lc.get('first_seen_bj','-')} | "
        f"上次提醒: {lc.get('last_alert_bj','-')}",
        f"- flow: {_fmt_flow(s.get('flow'))}",
        f"- wallets={s.get('wallet_count')} delta={_fmt_usd(s.get('delta_notional'))} "
        f"max_single={_fmt_usd(s.get('max_single_notional'))} "
        f"quality={s.get('avg_quality')} groups={','.join(s.get('groups',[])) or '-'}",
        f"- AI动作={s.get('ai_action')} 建议杠杆={s.get('suggested_leverage')}x "
        f"保证金={s.get('margin_pct')}% 止盈={s.get('take_profit_pct')}% "
        f"止损={s.get('stop_loss_pct')}% 最大持仓={s.get('max_hold_hours')}h",
        f"- AI理由: {s.get('reason','')}",
        f"- AI评分理由: {s.get('ai_score_reason','')}",
        f"- 风险: {s.get('risks')}",
        f"- 失效条件: {s.get('invalidation','')}",
    ])


def write_main_report(ctx: dict) -> None:
    ensure_reports_dir()
    cfg = ctx["cfg"]
    ai_stats = ctx["ai_stats"]
    signals = ctx["signals"]
    acc = ctx["virtual_account"]
    budget = ctx.get("ai_budget", {})
    scan_stats = ctx.get("scan_stats", {})

    def strong(direction):
        return sorted(
            [s for s in signals if s["direction"] == direction
             and (s.get("final_score") or 0) >= cfg.ai_min_final_score_for_open],
            key=lambda x: x["final_score"], reverse=True)

    longs = strong("OPEN_LONG")
    shorts = strong("OPEN_SHORT")
    watch = [s for s in signals if s.get("ai_action") == "WATCH"]

    lines = [
        "# 巨鲸中长期信号报告",
        f"运行时间(北京): {fmt_bj()}",
        f"扫描钱包: {ctx['wallets_scanned']} | 信号数: {len(signals)} | "
        f"噪音过滤: {ctx['noise_count']}",
        f"扫描成功: {scan_stats.get('success', ctx['wallets_scanned'])} | "
        f"失败: {scan_stats.get('failed', 0)} | "
        f"成功率: {scan_stats.get('success_rate', 1.0):.2%}",
        "",
        "## AI 状态",
        f"- 启用: {cfg.ai_enabled} / 评分启用: {cfg.ai_scoring_enabled}",
        f"- 调用: {ai_stats['calls']} 缓存命中: {ai_stats['cache_hits']} "
        f"错误: {ai_stats['errors']}",
        f"- 输入信号数: {ctx['ai_input_count']} | fallback: {ai_stats['fallback_used']}",
        f"- 预算(北京 {budget.get('date','-')}): 已用调用 {budget.get('calls',0)} "
        f"估算点数 {budget.get('points_used',0):.0f} | "
        f"预算封顶: {ai_stats.get('budget_blocked_flag')} "
        f"(被拦 {ai_stats.get('budget_blocked',0)} 次)",
        "",
        "## 开多强候选",
    ]
    lines += [_sig_block(s) for s in longs] or ["（无）"]
    lines += ["", "## 开空强候选"]
    lines += [_sig_block(s) for s in shorts] or ["（无）"]
    lines += ["", "## 观察候选"]
    lines += [_sig_block(s) for s in watch] or ["（无）"]

    lines += ["", "## 虚拟账户",
              f"- 初始本金: {_fmt_usd(acc.get('initial_capital'))}",
              f"- 当前本金: {_fmt_usd(acc.get('capital'))}"]
    open_trades = [t for t in acc.get("trades", []) if t["status"] == "OPEN"]
    lines.append(f"- 持仓数: {len(open_trades)}")
    for t in open_trades:
        warns = ", ".join(w["type"] for w in t.get("pre_close_warnings", [])) or "-"
        lines.append(
            f"  - {t['coin']} {t['side']} lev={t['leverage']}x "
            f"margin={_fmt_usd(t['margin'])} notional={_fmt_usd(t['notional'])} "
            f"entry={t['entry_px']} cur={t.get('current_px')} "
            f"pnl={t.get('pnl_pct')}% ROE={t.get('roe_pct')}% "
            f"开仓(北京)={fmt_bj(t.get('opened_at'))} 准备平仓={warns}")

    closed_now = ctx.get("closed_now", [])
    if closed_now:
        lines += ["", "## 本轮平仓"]
        for t in closed_now:
            lines.append(
                f"- {t['coin']} {t['side']} CLOSED reason={t['close_reason']} "
                f"AI置信度={t.get('close_ai_confidence')} pnl={t.get('pnl_pct')}% "
                f"盈亏={_fmt_usd(t.get('realized_pnl_usd'))} "
                f"平仓(北京)={fmt_bj(t.get('closed_at'))} "
                f"理由={t.get('close_ai_reason','')}")

    warnings = ctx.get("close_warnings", [])
    if warnings:
        lines += ["", "## 准备平仓提示"]
        for w in warnings:
            t = w["trade"]
            for wr in w["warnings"]:
                lines.append(f"- {t['coin']} {t['side']} {wr['type']} "
                             f"pnl={t.get('pnl_pct')}% {wr.get('reason','')}")

    with open(os.path.join(REPORTS, "latest_report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    with open(os.path.join(REPORTS, "latest_signals.json"), "w", encoding="utf-8") as f:
        json.dump({"generated_bj": fmt_bj(), "signals": signals}, f,
                  ensure_ascii=False, indent=2, default=str)


def write_wallet_scores(wallet_perf: dict, wallets_meta: dict) -> None:
    ensure_reports_dir()
    rows = []
    for addr, rec in wallet_perf.items():
        st = rec.get("stats", {})
        wins = st.get("windows", {})
        q = st.get("quality", 0.5)
        rows.append({
            "address": addr,
            "groups": wallets_meta.get(addr, []),
            "quality": q,
            "total_samples": st.get("total_samples", 0),
            "w24h": wins.get("24h", {}),
            "w72h": wins.get("72h", {}),
            "w168h": wins.get("168h", {}),
            "tier": "HIGH" if q >= 0.6 else "LOW" if q < 0.4 else "MID",
        })
    rows.sort(key=lambda r: r["quality"], reverse=True)

    with open(os.path.join(REPORTS, "wallet_scores.json"), "w", encoding="utf-8") as f:
        json.dump({"generated_bj": fmt_bj(), "wallets": rows}, f,
                  ensure_ascii=False, indent=2)

    lines = ["# 钱包表现评分", f"生成时间(北京): {fmt_bj()}", "",
             "| 地址 | 分组 | 质量 | 分级 | 24h胜率 | 72h胜率 | 168h胜率 | 样本 |",
             "|---|---|---|---|---|---|---|---|"]
    for r in rows[:200]:
        def wr(w):
            return f"{w.get('win_rate',0):.0%}({w.get('samples',0)})" if w else "-"
        lines.append(
            f"| {r['address']} | {','.join(r['groups'])} | {r['quality']} | "
            f"{r['tier']} | {wr(r['w24h'])} | {wr(r['w72h'])} | "
            f"{wr(r['w168h'])} | {r['total_samples']} |")
    with open(os.path.join(REPORTS, "wallet_scores.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
