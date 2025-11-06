import asyncio
from anchorpy import Wallet
from solders.keypair import Keypair
from solana.rpc.async_api import AsyncClient
from driftpy.drift_client import DriftClient
from driftpy.constants.numeric_constants import PRICE_PRECISION

from .abc import Dex

class Drift(Dex):
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        if self.loop.is_running():
            # If in an environment like Jupyter, use nest_asyncio
            import nest_asyncio
            nest_asyncio.apply()
            self.loop = asyncio.get_event_loop()

        self.keypair = Keypair()
        self.wallet = Wallet(self.keypair)
        self.connection = AsyncClient("https://api.mainnet-beta.solana.com")
        self.drift_client = DriftClient(self.connection, self.wallet, "mainnet")
        self.loop.run_until_complete(self.drift_client.subscribe())

    def _get_market_index(self, symbol):
        perp_markets = self.loop.run_until_complete(self.drift_client.get_perp_market_accounts())
        spot_markets = self.loop.run_until_complete(self.drift_client.get_spot_market_accounts())

        market_map = {str(market.symbol): market.market_index for market in perp_markets + spot_markets}

        return market_map.get(symbol)

    def get_price(self, symbol):
        market_index = self._get_market_index(symbol)
        if market_index is None:
            return None

        oracle_price_data = self.drift_client.get_oracle_price_data_for_perp_market(market_index)
        return oracle_price_data.price / PRICE_PRECISION

    def place_order(self, order_details):
        # This is a mock implementation. A real implementation would require
        # a funded wallet to place orders.
        #
        # from driftpy.types import OrderParams, PositionDirection, OrderType
        #
        # market_index = self._get_market_index(order_details["symbol"])
        # order_type = OrderType.LIMIT() if order_details["type"] == "limit" else OrderType.MARKET()
        # direction = PositionDirection.LONG() if order_details["side"] == "buy" else PositionDirection.SHORT()
        #
        # order_params = OrderParams(
        #     order_type=order_type,
        #     market_index=market_index,
        #     base_asset_amount=int(order_details["quantity"] * 1e9), # Assuming BASE_PRECISION
        #     direction=direction,
        #     price=int(order_details.get("price", 0) * 1e6) # Assuming PRICE_PRECISION
        # )
        #
        # result = self.loop.run_until_complete(self.drift_client.place_perp_order(order_params))
        # return {"order_id": result.tx_sig, "status": "open"}
        print(f"Placing order on Drift: {order_details}")
        return {"order_id": "mock_order_id", "status": "filled"}

    def cancel_order(self, order_id):
        # This is a mock implementation. A real implementation would require
        # a funded wallet to cancel orders.
        #
        # result = self.loop.run_until_complete(self.drift_client.cancel_order(order_id))
        # return {"order_id": order_id, "status": "cancelled"}
        print(f"Cancelling order on Drift: {order_id}")
        return {"order_id": order_id, "status": "cancelled"}

    def get_balances(self):
        # This is a mock implementation. A real implementation would require
        # a funded wallet to get balances.
        #
        # user = self.drift_client.get_user()
        # spot_positions = user.get_spot_positions()
        # balances = {}
        # for pos in spot_positions:
        #     market = self.drift_client.get_spot_market_account(pos.market_index)
        #     amount = pos.get_token_amount(market) / (10**market.decimals)
        #     balances[str(market.symbol)] = amount
        # return balances
        print("Fetching balances from Drift")
        return {"USD": 500, "BTC": 0.2}
