import logging
from collections import defaultdict


class BalanceService:
    def __init__(self, dex_clients):
        self.dex_clients = dex_clients
        self.logger = logging.getLogger(__name__)

    def get_consolidated_balances(self):
        self.logger.info("Fetching consolidated balances")
        total_usd = 0
        assets = defaultdict(float)

        for dex_name, dex_client in self.dex_clients.items():
            try:
                balances = dex_client.get_balances()
                for asset, amount in balances.items():
                    if asset == "USD":
                        total_usd += amount
                    else:
                        assets[asset] += amount
            except Exception as e:
                self.logger.error(f"Error fetching balances from {dex_name}: {e}")

        return {
            "total_usd": total_usd,
            "assets": dict(assets)
        }
