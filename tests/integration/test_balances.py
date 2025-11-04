import json
import unittest
from unittest.mock import patch

from src.app import create_app


class TestBalancesEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    @patch('src.routes.balances.BalanceService')
    def test_get_balances_success(self, MockBalanceService):
        mock_service_instance = MockBalanceService.return_value
        mock_service_instance.get_consolidated_balances.return_value = {
            "total_usd": 3500,
            "assets": {
                "BTC": 0.7,
                "ETH": 10
            }
        }

        response = self.client.get('/balances')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["total_usd"], 3500)
        self.assertEqual(data["assets"]["BTC"], 0.7)

if __name__ == '__main__':
    unittest.main()
