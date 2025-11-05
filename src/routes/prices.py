from flask import Blueprint, jsonify, request

from src.auth import require_api_key
from src.dex.drift import Drift
from src.dex.hyperliquid import Hyperliquid
from src.dex.lighter import Lighter
from src.services.price_service import PriceService

prices_bp = Blueprint('prices', __name__)

# In a real app, you'd likely inject these dependencies
dex_clients = {
    "hyperliquid": Hyperliquid(),
    "lighter": Lighter(),
    "drift": Drift()
}
price_service = PriceService(dex_clients)

@prices_bp.route('/prices', methods=['GET'])
def get_prices():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({"message": "Symbol parameter is required"}), 400

    prices = price_service.get_aggregated_prices(symbol)
    return jsonify(prices)
