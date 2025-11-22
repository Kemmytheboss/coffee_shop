from order import Order

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise Exception("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        coffee_orders = [order for order in Order.all if order.coffee == coffee]

        if not coffee_orders:
            return None

        spending = {}
        for order in coffee_orders:
            spending.setdefault(order.customer, 0)
            spending[order.customer] += order.price

        return max(spending, key=spending.get)
