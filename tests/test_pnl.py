from wallet_ai_monitor.pnl import calc_pnl


def test_long_pnl():
    r = calc_pnl("LONG", 100, 110, leverage=10, notional_usd=1000)
    assert round(r.pnl_pct, 6) == 10.0
    assert round(r.leveraged_roe_pct, 6) == 100.0
    assert round(r.pnl_usd, 6) == 100.0


def test_short_pnl():
    r = calc_pnl("SHORT", 100, 90, leverage=5, notional_usd=2000)
    assert round(r.pnl_pct, 6) == 10.0
    assert round(r.leveraged_roe_pct, 6) == 50.0
    assert round(r.pnl_usd, 6) == 200.0
