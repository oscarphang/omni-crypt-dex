import unittest
from unittest.mock import MagicMock

from src.services.order_service import OrderService


class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.mock_hyperliquid = MagicMock()
        self.mock_drift = MagicMock()
        self.dex_clients = {
            "hyperliquid": self.mock_hyperliquid,
            "drift": self.mock_drift,
        }
        self.order_service = OrderService(self.dex_clients)

    def test_place_spot_order(self):
        self.mock_hyperliquid.place_order.return_value = {"order_id": "hyper123", "status": "filled"}

        order_details = {
            "dex": "hyperliquid",
            "symbol": "BTC-USD",
            "side": "buy",
            "type": "spot",
            "quantity": 0.1
        }

        result = self.order_service.place_order(order_details)

        self.assertIn("order_id", result)
        self.assertEqual(result["order_id"], "hyper123")
        self.mock_hyperliquid.place_order.assert_called_once_with(order_details)

    def test_place_perp_order(self):
        self.mock_drift.place_order.return_value = {"order_id": "drift_perp_abc", "status": "filled"}

        order_details = {
            "dex": "drift",
            "symbol": "BTC-PERP",
            "side": "buy",
            "type": "perp",
            "quantity": 1
        }

        result = self.order_service.place_order(order_details)

        self.assertIn("order_id", result)
        self.assertEqual(result["order_id"], "drift_perp_abc")
        self.mock_drift.place_order.assert_called_once_with(order_details)

    def test_place_batch_orders(self):
        orders = [
            {
                "dex": "hyperliquid",
                "symbol": "BTC-USD",
                "side": "buy",
                "type": "spot",
                "quantity": 0.1
            },
            {
                "dex": "drift",
                "symbol": "BTC-PERP",
                "side": "buy",
                "type": "perp",
                "quantity": 1
            }
        ]

        self.mock_hyperliquid.place_order.return_value = {"order_id": "hyper_spot_123", "status": "filled"}
        self.mock_drift.place_order.return_value = {"order_id": "drift_perp_abc", "status": "filled"}

        results = self.order_service.place_batch_orders(orders)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["order_id"], "hyper_spot_123")
        self.assertEqual(results[1]["order_id"], "drift_perp_abc")

    def test_cancel_order(self):
        self.mock_hyperliquid.cancel_order.return_value = {"order_id": "hyper_spot_123", "status": "cancelled"}

        result = self.order_service.cancel_order("hyperliquid", "hyper_spot_123")

        self.assertEqual(result["status"], "cancelled")
        self.mock_hyperliquid.cancel_order.assert_called_once_with("hyper_spot_123")

if __name__ == '__main__':
    unittest.main()
