MENU = [
{"name": "Espresso", "price": 200},
{"name": "Cappuccino", "price": 200},
{"name": "Latte", "price": 250}
]

from typing import List, Optional

class Coffee:
    all_coffees: List['Coffee'] = []

    def __init__(self, name: str):
        self._name = None
        self.name = name  # Trigger setter for validation

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self._name = value

    # relationship helpers
    def orders(self) -> List['Order']:
        from order import Order  # Import here to avoid circular dependency
        return [order for order in Order.all if order.coffee_name == self.name] 

    def customers(self) -> List['Customer']:
        seen = []
        for order in self.orders():
            if order.customer not in seen:
                seen.append(order.customer)
        return seen

        # aggregate methods
    def number_of_orders(self) -> int:
        return len(self.orders())   

    def average_price(self) -> Optional[float]:
        orders = self.orders()
        if not orders:
            return None
        total = sum(order.price for order in orders)
        return total / len(orders)