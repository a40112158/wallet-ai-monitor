import os

from wallet_ai_monitor.config import load_settings
from wallet_ai_monitor.hyperliquid import HyperliquidClient


def test_hyperliquid_client_fetch_all_positions_accepts_batch_options():
    client = HyperliquidClient("https://example.invalid", timeout_seconds=30, retries=6, concurrency=3)
    assert "batch_size" in client.fetch_all_positions.__code__.co_varnames
    assert "batch_delay_seconds" in client.fetch_all_positions.__code__.co_varnames


def test_fullscan_stable_defaults(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    for key in ["MAX_WALLETS_PER_RUN", "AUTO_SHARD_ROTATION", "HL_CONCURRENCY", "HL_RETRIES", "HL_TIMEOUT_SECONDS", "HL_BATCH_SIZE"]:
        monkeypatch.delenv(key, raising=False)
    settings = load_settings()
    assert settings.max_wallets_per_run == 999999
    assert settings.auto_shard_rotation is False
    assert settings.hl_concurrency == 3
    assert settings.hl_retries == 6
    assert settings.hl_timeout_seconds == 30
    assert settings.hl_batch_size == 80
