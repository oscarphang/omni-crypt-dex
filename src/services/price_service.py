import logging


class PriceService:
    def __init__(self, dex_clients):
        self.dex_clients = dex_clients
        self.logger = logging.getLogger(__name__)

    def get_aggregated_prices(self, symbol):
        self.logger.info(f"Fetching aggregated prices for {symbol}")
        prices = {}
        for dex_name, dex_client in self.dex_clients.items():
            try:
                price = dex_client.get_price(symbol)
                if price is not None:
                    prices[dex_name] = price
            except Exception as e:
                self.logger.error(f"Error fetching price from {dex_name}: {e}")
        return prices
