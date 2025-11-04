from abc import ABC, abstractmethod


class Dex(ABC):
    @abstractmethod
    def get_price(self, symbol):
        pass

    @abstractmethod
    def place_order(self, order_details):
        pass

    @abstractmethod
    def cancel_order(self, order_id):
        pass

    @abstractmethod
    def get_balances(self):
        pass
