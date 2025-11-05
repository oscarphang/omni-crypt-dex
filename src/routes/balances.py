from flask import Blueprint, jsonify

from src.auth import require_api_key
from src.dex.drift import Drift
from src.dex.hyperliquid import Hyperliquid
from src.dex.lighter import Lighter
from src.services.balance_service import BalanceService

balances_bp = Blueprint('balances', __name__)

# In a real app, you'd likely inject these dependencies
dex_clients = {
    "hyperliquid": Hyperliquid(),
    "lighter": Lighter(),
    "drift": Drift()
}
balance_service = BalanceService(dex_clients)

@balances_bp.route('/balances', methods=['GET'])
def get_balances():
    balances = balance_service.get_consolidated_balances()
    return jsonify(balances)
