from wallet_ai_monitor.report import write_reports


def test_write_reports_creates_latest_and_history(tmp_path):
    paths = write_reports(
        tmp_path,
        1700000000,
        signals=[{
            "coin": "BTC", "side": "LONG", "direction": "OPEN_LONG", "wallet_count": 3,
            "total_delta_notional": 250000, "max_wallet_delta_notional": 120000,
            "total_position_value": 300000, "weighted_score": 10, "net_bias_score": 10,
            "avg_entry_px": 50000, "mark_px": 50100, "wallets": [], "swing_score": 82,
            "swing_bucket": "STRONG_CANDIDATE", "ai_confidence": 75,
            "ai": {"action": "OPEN_LONG", "reason": "test"}
        }],
        pnl_rows=[],
        ai_result={"ok": True, "signals": []},
    )
    assert (tmp_path / "latest_report.md").exists()
    assert (tmp_path / "latest_signals.json").exists()
    assert (tmp_path / "latest_signals.json").exists()
    assert not (tmp_path / "latest_signals.csv").exists()
    assert (tmp_path / "wallet_scores.md").exists()
    assert not (tmp_path / "wallet_scores.csv").exists()
    assert (tmp_path / "wallet_scores.json").exists()
    assert not (tmp_path / "history").exists()
    assert paths["latest_json"].name == "latest_signals.json"


def test_report_labels_virtual_vs_signal_tracking(tmp_path):
    write_reports(
        tmp_path,
        1700000000,
        signals=[],
        pnl_rows=[{
            "signal_id": 1, "coin": "BTC", "side": "LONG", "entry_px": 100.0, "current_px": 101.0,
            "pnl_pct": 1.0, "leveraged_roe_pct": 1.0, "pnl_usd": 100.0,
            "conservative_pnl_pct": 0.8, "mfe_pct": 1.0, "mae_pct": 0.0,
        }],
        ai_result={"ok": False, "reason": "test"},
        virtual_rows=[{
            "id": 1, "coin": "BTC", "side": "LONG", "entry_px": 100.0, "current_px": 101.0,
            "pnl_pct": 1.0, "pnl_usd": 16.67, "notional_usd": 1666.67,
            "status": "OPEN", "reason": None, "mfe_pct": 1.0, "mae_pct": 0.0,
        }],
        virtual_summary={
            "account_capital_usd": 10000, "equity_usd": 10016.67, "realized_pnl_usd": 0,
            "unrealized_pnl_usd": 16.67, "open_notional_usd": 1666.67,
            "available_notional_usd": 8333.33, "used_notional_pct": 16.67,
            "per_trade_cap_usd": 1666.67, "max_open_trades": 6,
            "total": 1, "open_count": 1, "closed_count": 0, "wins": 0, "losses": 0,
        },
    )
    text = (tmp_path / "latest_report.md").read_text(encoding="utf-8")
    assert "虚拟跟单账户（总本金模式）" in text
    assert "不是每个仓位 $10,000" in text
    assert "信号方向追踪（非模拟账户）" in text


def test_wallet_scores_report_is_written_even_when_empty(tmp_path):
    write_reports(
        tmp_path,
        1700000000,
        signals=[],
        pnl_rows=[],
        ai_result={"ok": False, "reason": "test"},
        run_meta={"wallet_perf_min_sample_size": 5},
        wallet_scores_rows=[],
    )
    text = (tmp_path / "wallet_scores.md").read_text(encoding="utf-8")
    assert "暂无可分类钱包" in text
    assert "继续运行一段时间" in text


def test_wallet_scores_report_groups_grades(tmp_path):
    write_reports(
        tmp_path,
        1700000000,
        signals=[],
        pnl_rows=[],
        ai_result={"ok": False, "reason": "test"},
        run_meta={"wallet_perf_min_sample_size": 5},
        wallet_scores_rows=[{
            "wallet": "0x" + "a" * 40,
            "wallet_group": "smart_money",
            "quality_grade": "A",
            "score": 1.33,
            "trades": 8,
            "wins": 5,
            "losses": 3,
            "win_rate_24h": 0.6,
            "avg_pnl_24h": 1.2,
            "win_rate_72h": 0.7,
            "avg_pnl_72h": 3.4,
            "win_rate_168h": 0.5,
            "avg_pnl_168h": 2.1,
        }],
    )
    text = (tmp_path / "wallet_scores.md").read_text(encoding="utf-8")
    assert "## A 级钱包" in text
    assert "70.0%" in text
