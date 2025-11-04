import unittest
from unittest.mock import MagicMock

from src.services.balance_service import BalanceService


class TestBalanceService(unittest.TestCase):
    def test_get_consolidated_balances(self):
        # Mocking DEX clients
        mock_hyperliquid = MagicMock()
        mock_hyperliquid.get_balances.return_value = {"USD": 1000, "BTC": 0.5}

        mock_lighter = MagicMock()
        mock_lighter.get_balances.return_value = {"USD": 2000, "ETH": 10}

        mock_drift = MagicMock()
        mock_drift.get_balances.return_value = {"USD": 500, "BTC": 0.2}

        dex_clients = {
            "hyperliquid": mock_hyperliquid,
            "lighter": mock_lighter,
            "drift": mock_drift
        }

        balance_service = BalanceService(dex_clients)
        balances = balance_service.get_consolidated_balances()

        self.assertEqual(balances["total_usd"], 3500)
        self.assertEqual(balances["assets"]["BTC"], 0.7)
        self.assertEqual(balances["assets"]["ETH"], 10)

if __name__ == '__main__':
    unittest.main()
