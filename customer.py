from customer import Customer

class Customer:

    def __init___(self, name: str):
        self._name = None
        self.name = name  # Trigger setter for validation   

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or len(value) == 0 or len(value) > 50:
            raise ValueError("Customer name must be a non-empty string with a maximum of 50 characters.")
        self._name = value  

    # relationship helpers  
    def orders(self) -> list['Order']:
        from order import Order  # Import here to avoid circular dependency
        return [order for order in Order.all if order.customer == self]

    def coffees(self) -> list['Coffee']:
        seen = []
        for order in self.orders():
            if order.coffee not in seen:
                seen.append(order.coffee)
        return seen 

    def test_create_order(self, coffee, price):
        from order import Order  # Import here to avoid circular dependency
        order = Order(self, coffee.name, price)
        return order

    # class methods
    @classmethod
    def most_aficionado(cls, coffee: 'Coffee') -> 'Customer':
        from order import Order  # Import here to avoid circular dependency
        customer_order_count = {}
        for order in Order.all:
            if order.coffee_name == coffee.name:
                customer = order.customer
                if customer in customer_order_count:
                    customer_order_count[customer] += 1
                else:
                    customer_order_count[customer] = 1
        if not customer_order_count:
            return None
        most_aficionado = max(customer_order_count, key=customer_order_count.get)
        return most_aficionado
        