from __future__ import annotations

import asyncio
import logging
import random
from dataclasses import dataclass
from typing import Any

import aiohttp

log = logging.getLogger(__name__)


@dataclass
class Position:
    wallet: str
    group: str
    weight: float
    coin: str
    side: str
    size: float
    abs_size: float
    entry_px: float | None
    mark_px: float | None
    position_value: float
    unrealized_pnl: float | None
    roe: float | None
    leverage: float | None
    raw: dict[str, Any]


class HyperliquidClient:
    def __init__(self, info_url: str, timeout_seconds: int = 16, retries: int = 3, concurrency: int = 8):
        self.info_url = info_url
        self.timeout_seconds = timeout_seconds
        self.retries = retries
        self.concurrency = concurrency
        self.sem = asyncio.Semaphore(concurrency)

    async def _post(self, session: aiohttp.ClientSession, payload: dict[str, Any]) -> Any:
        last_exc: Exception | None = None
        for attempt in range(self.retries):
            try:
                retry_after = 0.0
                async with self.sem:
                    async with session.post(self.info_url, json=payload) as resp:
                        if resp.status == 429:
                            await resp.read()
                            last_exc = RuntimeError("rate limited (HTTP 429)")
                            try:
                                retry_after = float(resp.headers.get("Retry-After", "0") or 0)
                            except ValueError:
                                retry_after = 0.0
                        else:
                            resp.raise_for_status()
                            return await resp.json(content_type=None)
                if retry_after >= 0:
                    delay = max(retry_after, 1.5 * (2 ** attempt)) + random.uniform(0, 0.35)
                    log.warning("Hyperliquid rate limited attempt=%d delay=%.2fs", attempt + 1, delay)
                    await asyncio.sleep(delay)
                    continue
            except Exception as exc:  # noqa: BLE001
                last_exc = exc
                if attempt + 1 < self.retries:
                    await asyncio.sleep(0.5 * (2 ** attempt) + random.uniform(0, 0.25))
        request_type = payload.get("type", "unknown")
        raise RuntimeError(f"Hyperliquid request failed type={request_type} err={last_exc}")

    async def all_mids(self, session: aiohttp.ClientSession) -> dict[str, float]:
        data = await self._post(session, {"type": "allMids"})
        out: dict[str, float] = {}
        if isinstance(data, dict):
            for k, v in data.items():
                try:
                    out[str(k)] = float(v)
                except (TypeError, ValueError):
                    continue
        return out

    async def meta_and_asset_ctxs(self, session: aiohttp.ClientSession) -> dict[str, dict[str, Any]]:
        data = await self._post(session, {"type": "metaAndAssetCtxs"})
        ctx_by_coin: dict[str, dict[str, Any]] = {}
        if not isinstance(data, list) or len(data) < 2:
            return ctx_by_coin
        meta, ctxs = data[0], data[1]
        universe = meta.get("universe", []) if isinstance(meta, dict) else []
        if not isinstance(ctxs, list):
            return ctx_by_coin
        for i, asset in enumerate(universe):
            if not isinstance(asset, dict) or i >= len(ctxs):
                continue
            coin = asset.get("name")
            if coin:
                ctx_by_coin[str(coin)] = ctxs[i]
        return ctx_by_coin

    async def clearinghouse_state(self, session: aiohttp.ClientSession, user: str) -> dict[str, Any]:
        data = await self._post(session, {"type": "clearinghouseState", "user": user})
        return data if isinstance(data, dict) else {}

    async def fetch_wallet_positions(self, session: aiohttp.ClientSession, wallet, mids: dict[str, float]) -> list[Position]:
        state = await self.clearinghouse_state(session, wallet.address)
        positions = []
        for item in state.get("assetPositions", []) or []:
            pos = item.get("position", item) if isinstance(item, dict) else {}
            if not isinstance(pos, dict):
                continue
            try:
                szi = float(pos.get("szi", 0) or 0)
            except (TypeError, ValueError):
                continue
            if abs(szi) <= 0:
                continue
            coin = str(pos.get("coin", "")).strip()
            if not coin:
                continue
            side = "LONG" if szi > 0 else "SHORT"
            entry_px = _to_float(pos.get("entryPx"))
            mark_px = mids.get(coin)
            pos_value = _to_float(pos.get("positionValue"))
            if pos_value is None and mark_px is not None:
                pos_value = abs(szi) * mark_px
            leverage = _extract_leverage(pos.get("leverage"))
            positions.append(
                Position(
                    wallet=wallet.address,
                    group=wallet.group,
                    weight=wallet.weight,
                    coin=coin,
                    side=side,
                    size=szi,
                    abs_size=abs(szi),
                    entry_px=entry_px,
                    mark_px=mark_px,
                    position_value=float(pos_value or 0),
                    unrealized_pnl=_to_float(pos.get("unrealizedPnl")),
                    roe=_to_float(pos.get("returnOnEquity")),
                    leverage=leverage,
                    raw=pos,
                )
            )
        return positions


    async def candle_snapshot(
        self,
        session: aiohttp.ClientSession,
        *,
        coin: str,
        interval: str,
        start_time_ms: int,
        end_time_ms: int,
    ) -> list[dict[str, Any]]:
        data = await self._post(session, {
            "type": "candleSnapshot",
            "req": {
                "coin": coin,
                "interval": interval,
                "startTime": int(start_time_ms),
                "endTime": int(end_time_ms),
            },
        })
        return data if isinstance(data, list) else []

    async def fetch_market_candles(
        self,
        coins: list[str],
        *,
        intervals: list[str],
        lookback_minutes: int,
        concurrency: int = 4,
    ) -> dict[str, dict[str, list[dict[str, Any]]]]:
        if not coins or not intervals:
            return {}
        end_ms = int(asyncio.get_running_loop().time() * 1000)
        # event-loop monotonic time is not wall time; use time.time for exchange timestamps.
        import time as _time
        end_ms = int(_time.time() * 1000)
        start_ms = end_ms - int(lookback_minutes) * 60 * 1000
        timeout = aiohttp.ClientTimeout(total=self.timeout_seconds)
        connector = aiohttp.TCPConnector(limit=max(concurrency * 2, 8), ttl_dns_cache=300)
        limiter = asyncio.Semaphore(max(1, concurrency))
        out: dict[str, dict[str, list[dict[str, Any]]]] = {coin: {} for coin in coins}

        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
            async def one(coin: str, interval: str) -> None:
                try:
                    async with limiter:
                        out.setdefault(coin, {})[interval] = await self.candle_snapshot(
                            session, coin=coin, interval=interval, start_time_ms=start_ms, end_time_ms=end_ms
                        )
                except Exception as exc:  # noqa: BLE001
                    log.warning("candle fetch failed coin=%s interval=%s err=%s", coin, interval, exc)
                    out.setdefault(coin, {})[interval] = []

            await asyncio.gather(*(one(coin, interval) for coin in coins for interval in intervals))
        return out

    async def fetch_all_positions(
        self,
        wallets: list,
        *,
        progress_every: int = 100,
        batch_size: int = 80,
        batch_delay_seconds: float = 2.0,
    ) -> tuple[dict[str, float], dict[str, dict[str, Any]], list[Position], set[str]]:
        """Fetch all wallet positions with bounded batches.

        Full-scan mode can include thousands of wallets. Creating all tasks at once
        still overloads Hyperliquid even with a semaphore, because retries bunch up
        after 429 responses. Batches keep pressure steady and make every-run full
        scans more likely to finish with usable coverage.
        """
        timeout = aiohttp.ClientTimeout(total=max(self.timeout_seconds * max(self.retries, 1), self.timeout_seconds + 5))
        connector = aiohttp.TCPConnector(limit=max(self.concurrency * 2, 8), ttl_dns_cache=300)
        positions: list[Position] = []
        successful_wallets: set[str] = set()
        batch_size = max(1, int(batch_size or 80))
        batch_delay_seconds = max(0.0, float(batch_delay_seconds or 0.0))

        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
            mids, ctxs = await asyncio.gather(self.all_mids(session), self.meta_and_asset_ctxs(session))

            async def one(idx: int, wallet):
                if idx and idx % progress_every == 0:
                    log.info("scanned queued=%d/%d", idx, len(wallets))
                return await self.fetch_wallet_positions(session, wallet, mids)

            for start in range(0, len(wallets), batch_size):
                batch = wallets[start : start + batch_size]
                batch_no = start // batch_size + 1
                total_batches = (len(wallets) + batch_size - 1) // batch_size
                log.info(
                    "fetching wallet batch %d/%d size=%d concurrency=%d",
                    batch_no,
                    total_batches,
                    len(batch),
                    self.concurrency,
                )
                results = await asyncio.gather(
                    *(one(start + i + 1, wallet) for i, wallet in enumerate(batch)),
                    return_exceptions=True,
                )
                failed_in_batch = 0
                for wallet, result in zip(batch, results):
                    if isinstance(result, BaseException):
                        failed_in_batch += 1
                        log.warning("wallet fetch failed wallet=%s err=%s", wallet.address, result)
                        continue
                    successful_wallets.add(wallet.address)
                    positions.extend(result)

                if failed_in_batch:
                    log.warning(
                        "wallet batch %d/%d failures=%d/%d",
                        batch_no,
                        total_batches,
                        failed_in_batch,
                        len(batch),
                    )

                if start + batch_size < len(wallets) and batch_delay_seconds > 0:
                    # Add tiny jitter so scheduled workers do not create fixed bursts.
                    await asyncio.sleep(batch_delay_seconds + random.uniform(0, min(0.8, batch_delay_seconds * 0.25)))

        return mids, ctxs, positions, successful_wallets


def _to_float(v: Any) -> float | None:
    try:
        if v is None or v == "":
            return None
        return float(v)
    except (TypeError, ValueError):
        return None


def _extract_leverage(v: Any) -> float | None:
    if isinstance(v, dict):
        return _to_float(v.get("value"))
    return _to_float(v)
