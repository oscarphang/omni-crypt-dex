import logging


class OrderService:
    def __init__(self, dex_clients):
        self.dex_clients = dex_clients
        self.logger = logging.getLogger(__name__)

    def place_order(self, order_details):
        dex_name = order_details.get("dex")
        self.logger.info(f"Placing order on {dex_name}: {order_details}")
        if not dex_name or dex_name not in self.dex_clients:
            self.logger.error(f"Invalid DEX specified: {dex_name}")
            raise ValueError("Invalid DEX specified")

        try:
            dex_client = self.dex_clients[dex_name]
            return dex_client.place_order(order_details)
        except Exception as e:
            self.logger.error(f"Error placing order on {dex_name}: {e}")
            raise

    def place_batch_orders(self, orders):
        self.logger.info(f"Placing batch of {len(orders)} orders")
        results = []
        for order in orders:
            try:
                results.append(self.place_order(order))
            except Exception as e:
                self.logger.error(f"Error in batch order: {e}")
                # Decide if you want to continue or stop on error
        return results

    def cancel_order(self, dex_name, order_id):
        self.logger.info(f"Cancelling order {order_id} on {dex_name}")
        if not dex_name or dex_name not in self.dex_clients:
            self.logger.error(f"Invalid DEX specified: {dex_name}")
            raise ValueError("Invalid DEX specified")

        try:
            dex_client = self.dex_clients[dex_name]
            return dex_client.cancel_order(order_id)
        except Exception as e:
            self.logger.error(f"Error cancelling order on {dex_name}: {e}")
            raise
