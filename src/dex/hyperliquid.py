from .abc import Dex


class Hyperliquid(Dex):
    def get_price(self, symbol):
        # In a real implementation, this would connect to the Hyperliquid API
        print(f"Fetching price for {symbol} from Hyperliquid")
        if symbol == "BTC-USD":
            return 50000.0
        elif symbol == "ETH-USD":
            return 3000.0
        else:
            return None

    def place_order(self, order_details):
        # In a real implementation, this would connect to the Hyperliquid API
        order_type = order_details.get("type")
        print(f"Placing {order_type} order on Hyperliquid: {order_details}")

        if order_type == "spot":
            # Simulate a successful spot order placement
            return {"order_id": "hyper_spot_123", "status": "filled"}
        elif order_type == "perp":
            # Simulate a successful perp order placement
            return {"order_id": "hyper_perp_456", "status": "filled"}
        else:
            raise ValueError("Unsupported order type")

    def cancel_order(self, order_id):
        # In a real implementation, this would connect to the Hyperliquid API
        print(f"Cancelling order on Hyperliquid: {order_id}")
        # Simulate a successful order cancellation
        return {"order_id": order_id, "status": "cancelled"}

    def get_balances(self):
        # In a real implementation, this would connect to the Hyperliquid API
        print("Fetching balances from Hyperliquid")
        return {"USD": 1000, "BTC": 0.5}
