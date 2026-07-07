from pathlib import Path
from wallet_ai_monitor.wallets import read_addresses, load_wallets


def test_uploaded_address_files_exist():
    root = Path(__file__).resolve().parents[1]
    smart = read_addresses(root / "data" / "smart_money_all_addresses.txt")
    money = read_addresses(root / "data" / "money_printer_all_addresses.txt")
    assert len(smart) > 1000
    assert len(money) > 100


def test_load_wallets_dedupes():
    root = Path(__file__).resolve().parents[1]
    wallets = load_wallets(root / "data")
    addresses = [w.address for w in wallets]
    assert len(addresses) == len(set(addresses))
