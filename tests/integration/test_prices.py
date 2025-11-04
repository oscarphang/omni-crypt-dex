import json
import unittest
from unittest.mock import patch

from src.app import create_app


class TestPricesEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    @patch('src.routes.prices.PriceService')
    def test_get_prices_success(self, MockPriceService):
        mock_service_instance = MockPriceService.return_value
        mock_service_instance.get_aggregated_prices.return_value = {
            "hyperliquid": 50000,
            "lighter": 50100,
            "drift": 50050
        }

        response = self.client.get('/prices?symbol=BTC-USD')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 3)
        self.assertEqual(data["hyperliquid"], 50000)

    def test_get_prices_no_symbol(self):
        response = self.client.get('/prices')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data["message"], "Symbol parameter is required")

if __name__ == '__main__':
    unittest.main()
