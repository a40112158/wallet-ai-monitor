from wallet_ai_monitor.storage import Store


def test_recent_signal_flow_stats_dedupes_wallets(tmp_path):
    s = Store(tmp_path / "swing.sqlite3")
    sig = {
        "coin": "BTC",
        "side": "LONG",
        "direction": "OPEN_LONG",
        "wallet_count": 2,
        "total_delta_notional": 1000,
        "total_position_value": 1000,
        "weighted_score": 5,
        "wallets": [
            {"wallet": "w1", "group": "smart_money", "event": "INCREASE_POSITION", "delta_notional": 600, "weight": 1, "wallet_score": 1},
            {"wallet": "w2", "group": "money_printer", "event": "INCREASE_POSITION", "delta_notional": 400, "weight": 1.35, "wallet_score": 1},
        ],
    }
    s.insert_signal(100, sig)
    stats = s.recent_signal_flow_stats(200, [2 * 3600])
    b = stats[("BTC", "LONG")][2 * 3600]
    assert b["total_delta_notional"] == 1000
    assert b["wallet_count"] == 2
    assert b["money_printer_wallet_count"] == 1
    s.close()
