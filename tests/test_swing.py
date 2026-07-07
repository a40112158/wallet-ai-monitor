from wallet_ai_monitor.signals import attach_swing_context


def test_swing_score_marks_multi_window_candidate():
    signals = [{
        "coin": "BTC",
        "side": "LONG",
        "direction": "OPEN_LONG",
        "wallet_count": 3,
        "groups": {"smart_money": 2, "money_printer": 1},
        "events": {"INCREASE_POSITION": 3},
        "total_delta_notional": 200000,
        "max_wallet_delta_notional": 100000,
        "weighted_score": 10,
        "net_bias_score": 10,
        "conflict_level": "LOW",
        "conflict_ratio": 0,
        "market": {"funding": 0.0001, "m15": {"return_pct": 1, "volume_ratio": 2}, "h1": {"return_pct": 2}},
        "wallets": [
            {"wallet": "a", "group": "smart_money"},
            {"wallet": "b", "group": "smart_money"},
            {"wallet": "c", "group": "money_printer"},
        ],
        "risk_tags": [],
    }]
    hist = {
        ("BTC", "LONG"): {
            2 * 3600: {"total_delta_notional": 150000, "signal_count": 1, "wallets": {"d"}, "smart_money_wallets": {"d"}, "money_printer_wallets": set(), "weighted_score": 5},
            6 * 3600: {"total_delta_notional": 300000, "signal_count": 2, "wallets": {"d", "e"}, "smart_money_wallets": {"d"}, "money_printer_wallets": {"e"}, "weighted_score": 8},
            24 * 3600: {"total_delta_notional": 500000, "signal_count": 3, "wallets": {"d", "e", "f"}, "smart_money_wallets": {"d"}, "money_printer_wallets": {"e"}, "weighted_score": 12},
        }
    }
    attach_swing_context(signals, hist, windows_hours=[2, 6, 24])
    assert signals[0]["swing_score"] >= 65
    assert signals[0]["swing"]["flow"]["24h"]["total_delta_notional"] == 700000
    assert "money_printer_confirmed" in signals[0]["risk_tags"]
