from wallet_ai_monitor.hyperliquid import Position
from wallet_ai_monitor.signals import aggregate_exit_events, aggregate_signals, build_position_deltas


def pos(wallet="0x" + "1" * 40, coin="BTC", size=1.0, mark=100.0, group="smart_money"):
    return Position(
        wallet=wallet,
        group=group,
        weight=1.0,
        coin=coin,
        side="LONG" if size > 0 else "SHORT",
        size=size,
        abs_size=abs(size),
        entry_px=mark,
        mark_px=mark,
        position_value=abs(size) * mark,
        unrealized_pnl=0,
        roe=0,
        leverage=1,
        raw={},
    )


def test_warmup_missing_wallet_skips_fake_new_position():
    p = pos()
    deltas = build_position_deltas({}, [p], scanned_wallets={p.wallet}, baseline_wallets=set(), warmup_missing_wallets=True)
    assert deltas == []


def test_existing_wallet_new_position_emits_signal():
    p = pos()
    deltas = build_position_deltas({}, [p], scanned_wallets={p.wallet}, baseline_wallets={p.wallet}, warmup_missing_wallets=True)
    signals = aggregate_signals(deltas, min_delta_notional_usd=10, min_single_whale_delta_usd=10, min_wallet_count=1)
    assert len(signals) == 1
    assert signals[0]["direction"] == "OPEN_LONG"


def test_reduce_and_close_events_are_aggregated():
    wallet = "0x" + "2" * 40
    prev = {(wallet, "ETH"): {"size": 2.0, "side": "LONG", "mark_px": 100.0, "entry_px": 100.0, "wallet_group": "smart_money", "position_value": 200.0, "unrealized_pnl": 0, "roe": 0, "leverage": 1}}
    cur = [pos(wallet=wallet, coin="ETH", size=1.0, mark=100.0)]
    deltas = build_position_deltas(prev, cur, scanned_wallets={wallet}, baseline_wallets={wallet})
    exits = aggregate_exit_events(deltas, min_delta_notional_usd=10)
    assert exits[0]["direction"] == "EXIT_LONG"
    assert exits[0]["total_delta_notional"] == 100.0

    deltas = build_position_deltas(prev, [], scanned_wallets={wallet}, baseline_wallets={wallet}, mids={"ETH": 90.0})
    exits = aggregate_exit_events(deltas, min_delta_notional_usd=10)
    assert exits[0]["direction"] == "EXIT_LONG"
    assert exits[0]["total_delta_notional"] == 180.0

from wallet_ai_monitor.signals import apply_signal_lifecycle, attach_market_context


def test_lifecycle_suppresses_duplicate_inside_cooldown():
    class Row(dict):
        def __getitem__(self, key):
            return dict.__getitem__(self, key)

    signals = [{"coin": "BTC", "side": "LONG", "direction": "OPEN_LONG", "total_delta_notional": 1000, "risk_tags": []}]
    recent = [Row({"id": 7, "ts": 1000, "coin": "BTC", "side": "LONG", "total_delta_notional": 900})]
    kept, events = apply_signal_lifecycle(
        signals, [], recent_active=recent, now_ts=1050, cooldown_seconds=3600, realert_multiplier=2.0, exit_decay_ratio=0.5
    )
    assert kept == []
    assert events[0]["event"] == "COOLDOWN_MERGED"


def test_market_candle_metrics_adds_risk_tags():
    s = [{"coin": "BTC", "side": "LONG", "direction": "OPEN_LONG", "conflict_level": "LOW"}]
    candles = {
        "BTC": {
            "15m": [
                {"o": "100", "h": "101", "l": "99", "c": "100", "v": "10"},
                {"o": "100", "h": "110", "l": "99", "c": "106", "v": "40"},
            ],
            "1h": [
                {"o": "100", "h": "101", "l": "99", "c": "100", "v": "10"},
                {"o": "100", "h": "109", "l": "99", "c": "109", "v": "10"},
            ],
        }
    }
    attach_market_context(s, {"BTC": {"funding": "0.0004"}}, candles)
    assert "long_crowded_funding" in s[0]["risk_tags"]
    assert "long_chasing_pump" in s[0]["risk_tags"]
    assert s[0]["market"]["m15"]["return_pct"] == 6.0
