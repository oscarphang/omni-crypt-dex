import json
import unittest
from unittest.mock import patch

from src.app import create_app


class TestOrdersEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    @patch('src.routes.orders.OrderService')
    def test_place_spot_order_success(self, MockOrderService):
        mock_service_instance = MockOrderService.return_value
        mock_service_instance.place_order.return_value = {
            "order_id": "hyper123",
            "status": "filled"
        }

        order_payload = {
            "dex": "hyperliquid",
            "symbol": "BTC-USD",
            "side": "buy",
            "type": "spot",
            "quantity": 0.1
        }

        response = self.client.post('/orders', data=json.dumps(order_payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["order_id"], "hyper_spot_123")

    @patch('src.routes.orders.OrderService')
    def test_place_perp_order_success(self, MockOrderService):
        mock_service_instance = MockOrderService.return_value
        mock_service_instance.place_order.return_value = {
            "order_id": "drift_perp_abc",
            "status": "filled"
        }

        order_payload = {
            "dex": "drift",
            "symbol": "BTC-PERP",
            "side": "buy",
            "type": "perp",
            "quantity": 1
        }

        response = self.client.post('/orders', data=json.dumps(order_payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["order_id"], "drift_perp_abc")

    def test_place_order_missing_data(self):
        response = self.client.post('/orders', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data["message"], "Invalid order payload")

    @patch('src.routes.orders.OrderService')
    def test_place_batch_orders_success(self, MockOrderService):
        mock_service_instance = MockOrderService.return_value
        mock_service_instance.place_batch_orders.return_value = [
            {"order_id": "hyper_spot_123", "status": "filled"},
            {"order_id": "drift_perp_abc", "status": "filled"}
        ]

        orders_payload = [
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

        response = self.client.post('/orders/batch', data=json.dumps(orders_payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["order_id"], "hyper_spot_123")

    @patch('src.routes.orders.OrderService')
    def test_cancel_order_success(self, MockOrderService):
        mock_service_instance = MockOrderService.return_value
        mock_service_instance.cancel_order.return_value = {
            "order_id": "hyper_spot_123",
            "status": "cancelled"
        }

        response = self.client.post('/orders/hyperliquid/hyper_spot_123/cancel')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["status"], "cancelled")

if __name__ == '__main__':
    unittest.main()
