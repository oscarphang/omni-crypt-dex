from .abc import Dex


class Lighter(Dex):
    def get_price(self, symbol):
        # In a real implementation, this would connect to the Lighter API
        print(f"Fetching price for {symbol} from Lighter")
        if symbol == "BTC-USD":
            return 50100.0
        elif symbol == "ETH-USD":
            return 3010.0
        else:
            return None

    def place_order(self, order_details):
        # In a real implementation, this would connect to the Lighter API
        print(f"Placing order on Lighter: {order_details}")
        # Simulate a successful order placement
        return {"order_id": "lighter456", "status": "filled"}

    def cancel_order(self, order_id):
        # In a real implementation, this would connect to the Lighter API
        print(f"Cancelling order on Lighter: {order_id}")
        # Simulate a successful order cancellation
        return {"order_id": order_id, "status": "cancelled"}

    def get_balances(self):
        # In a real implementation, this would connect to the Lighter API
        print("Fetching balances from Lighter")
        return {"USD": 2000, "ETH": 10}
