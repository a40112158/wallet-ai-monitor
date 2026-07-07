from wallet_ai_monitor.signals import attach_swing_context


def test_swing_context_supports_72h_and_7d_windows():
    signals = [{
        "coin": "HYPE",
        "side": "LONG",
        "direction": "OPEN_LONG",
        "wallet_count": 4,
        "groups": {"smart_money": 2, "money_printer": 2},
        "events": {"INCREASE_POSITION": 4},
        "total_delta_notional": 300000,
        "max_wallet_delta_notional": 120000,
        "weighted_score": 12,
        "net_bias_score": 12,
        "conflict_level": "LOW",
        "conflict_ratio": 0,
        "market": {"funding": 0.0001},
        "wallets": [
            {"wallet": "w1", "group": "smart_money"},
            {"wallet": "w2", "group": "smart_money"},
            {"wallet": "w3", "group": "money_printer"},
            {"wallet": "w4", "group": "money_printer"},
        ],
        "risk_tags": [],
    }]
    hist = {
        ("HYPE", "LONG"): {
            72 * 3600: {
                "total_delta_notional": 700000,
                "signal_count": 4,
                "wallets": {"a", "b"},
                "smart_money_wallets": {"a"},
                "money_printer_wallets": {"b"},
                "weighted_score": 20,
            },
            168 * 3600: {
                "total_delta_notional": 1500000,
                "signal_count": 8,
                "wallets": {"a", "b", "c"},
                "smart_money_wallets": {"a", "c"},
                "money_printer_wallets": {"b"},
                "weighted_score": 35,
            },
        }
    }
    attach_swing_context(signals, hist, windows_hours=[2, 6, 24, 72, 168])
    flow = signals[0]["swing"]["flow"]
    assert "72h" in flow
    assert "168h" in flow
    assert flow["72h"]["total_delta_notional"] == 1000000
    assert flow["168h"]["total_delta_notional"] == 1800000
