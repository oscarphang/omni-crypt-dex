import unittest
from unittest.mock import MagicMock

from src.services.price_service import PriceService


class TestPriceService(unittest.TestCase):
    def test_get_aggregated_prices(self):
        # Mocking DEX clients
        mock_hyperliquid = MagicMock()
        mock_hyperliquid.get_price.return_value = 50000

        mock_lighter = MagicMock()
        mock_lighter.get_price.return_value = 50100

        mock_drift = MagicMock()
        mock_drift.get_price.return_value = 50050

        dex_clients = {
            "hyperliquid": mock_hyperliquid,
            "lighter": mock_lighter,
            "drift": mock_drift
        }

        price_service = PriceService(dex_clients)
        prices = price_service.get_aggregated_prices("BTC-USD")

        self.assertEqual(len(prices), 3)
        self.assertIn("hyperliquid", prices)
        self.assertIn("lighter", prices)
        self.assertIn("drift", prices)
        self.assertEqual(prices["hyperliquid"], 50000)
        self.assertEqual(prices["lighter"], 50100)
        self.assertEqual(prices["drift"], 50050)

if __name__ == '__main__':
    unittest.main()
