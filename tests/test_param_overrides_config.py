import os

from wallet_ai_monitor.config import _load_param_overrides


def test_param_overrides_loader_only_allows_safe_keys(tmp_path, monkeypatch):
    path = tmp_path / "ai_param_overrides.env"
    path.write_text(
        "MIN_DELTA_NOTIONAL_USD=123456\n"
        "POE_API_KEY=should_not_load\n"
        "TELEGRAM_BOT_TOKEN=bad\n"
        "SWING_WINDOWS_HOURS=2,6,24,72,168\n",
        encoding="utf-8",
    )
    monkeypatch.delenv("MIN_DELTA_NOTIONAL_USD", raising=False)
    monkeypatch.delenv("POE_API_KEY", raising=False)
    _load_param_overrides(path)
    assert os.environ["MIN_DELTA_NOTIONAL_USD"] == "123456"
    assert os.environ["SWING_WINDOWS_HOURS"] == "2,6,24,72,168"
    assert "POE_API_KEY" not in os.environ


def test_param_overrides_loader_rejects_invalid_values(tmp_path, monkeypatch):
    from wallet_ai_monitor.config import _load_param_overrides

    path = tmp_path / "ai_param_overrides.env"
    path.write_text(
        "HL_CONCURRENCY=9999\n"
        "SWING_WINDOWS_HOURS=1,9999\n"
        "MIN_WALLET_COUNT=4\n",
        encoding="utf-8",
    )
    monkeypatch.delenv("HL_CONCURRENCY", raising=False)
    monkeypatch.delenv("SWING_WINDOWS_HOURS", raising=False)
    monkeypatch.delenv("MIN_WALLET_COUNT", raising=False)
    _load_param_overrides(path)
    assert "HL_CONCURRENCY" not in os.environ
    assert "SWING_WINDOWS_HOURS" not in os.environ
    assert os.environ["MIN_WALLET_COUNT"] == "4"
