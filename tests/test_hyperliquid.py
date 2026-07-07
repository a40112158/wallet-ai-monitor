import asyncio

from wallet_ai_monitor.hyperliquid import HyperliquidClient
from wallet_ai_monitor.wallets import Wallet


class StubClient(HyperliquidClient):
    async def all_mids(self, session):
        return {"BTC": 100.0}

    async def meta_and_asset_ctxs(self, session):
        return {}

    async def fetch_wallet_positions(self, session, wallet, mids):
        if wallet.address.endswith("2"):
            raise RuntimeError("temporary API failure")
        return []


def test_failed_wallet_is_not_marked_successful():
    wallets = [
        Wallet("0x" + "1" * 40, "smart_money", 1.0),
        Wallet("0x" + "1" * 39 + "2", "smart_money", 1.0),
    ]
    client = StubClient("https://example.invalid")
    mids, ctxs, positions, successful = asyncio.run(client.fetch_all_positions(wallets))
    assert mids == {"BTC": 100.0}
    assert ctxs == {}
    assert positions == []
    assert successful == {wallets[0].address}
