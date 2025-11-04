from flask import Blueprint, jsonify, request

from src.dex.drift import Drift
from src.dex.hyperliquid import Hyperliquid
from src.dex.lighter import Lighter
from src.services.order_service import OrderService

orders_bp = Blueprint('orders', __name__)

# In a real app, you'd likely inject these dependencies
dex_clients = {
    "hyperliquid": Hyperliquid(),
    "lighter": Lighter(),
    "drift": Drift()
}
order_service = OrderService(dex_clients)

@orders_bp.route('/orders', methods=['POST'])
def place_order():
    order_details = request.get_json()
    if not order_details:
        return jsonify({"message": "Invalid order payload"}), 400

    try:
        result = order_service.place_order(order_details)
        return jsonify(result), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@orders_bp.route('/orders/batch', methods=['POST'])
def place_batch_orders():
    orders = request.get_json()
    if not isinstance(orders, list):
        return jsonify({"message": "Invalid payload: expected a list of orders"}), 400

    try:
        results = order_service.place_batch_orders(orders)
        return jsonify(results), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@orders_bp.route('/orders/<dex_name>/<order_id>/cancel', methods=['POST'])
def cancel_order(dex_name, order_id):
    try:
        result = order_service.cancel_order(dex_name, order_id)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
