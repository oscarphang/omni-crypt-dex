import unittest
from unittest.mock import MagicMock

from src.services.price_service import PriceService


from driftpy.types import OraclePriceData
from src.dex.drift import Drift

class TestPriceService(unittest.TestCase):
    @patch('src.dex.drift.DriftClient')
    def test_get_aggregated_prices(self, MockDriftClient):
        # Mocking DEX clients
        mock_hyperliquid = MagicMock()
        mock_hyperliquid.get_price.return_value = 50000.0

        mock_lighter = MagicMock()
        mock_lighter.get_price.return_value = 50100.0

        # Mock the DriftClient's methods
        mock_drift_client_instance = MockDriftClient.return_value
        mock_drift_client_instance.get_oracle_price_data_for_perp_market.return_value = OraclePriceData(
            price=50050 * 1e6, # PRICE_PRECISION
            slot=0,
            confidence=0,
            has_sufficient_number_of_data_points=True
        )
        mock_drift = Drift()

        dex_clients = {
            "hyperliquid": mock_hyperliquid,
            "lighter": mock_lighter,
            "drift": mock_drift,
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
