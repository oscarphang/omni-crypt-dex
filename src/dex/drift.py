from .abc import Dex


class Drift(Dex):
    def get_price(self, symbol):
        # In a real implementation, this would connect to the Drift API
        print(f"Fetching price for {symbol} from Drift")
        if symbol == "BTC-USD":
            return 50050.0
        elif symbol == "ETH-USD":
            return 3005.0
        else:
            return None

    def place_order(self, order_details):
        # In a real implementation, this would connect to the Drift API
        order_type = order_details.get("type")
        print(f"Placing {order_type} order on Drift: {order_details}")

        if order_type == "spot":
            # Simulate a successful spot order placement
            return {"order_id": "drift_spot_789", "status": "filled"}
        elif order_type == "perp":
            # Simulate a successful perp order placement
            return {"order_id": "drift_perp_abc", "status": "filled"}
        else:
            raise ValueError("Unsupported order type")

    def cancel_order(self, order_id):
        # In a real implementation, this would connect to the Drift API
        print(f"Cancelling order on Drift: {order_id}")
        # Simulate a successful order cancellation
        return {"order_id": order_id, "status": "cancelled"}

    def get_balances(self):
        # In a real implementation, this would connect to the Drift API
        print("Fetching balances from Drift")
        return {"USD": 500, "BTC": 0.2}
