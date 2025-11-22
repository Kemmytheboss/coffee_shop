# order.py
from typing import List


class Order:
    """
    Order ties together a Customer, a Coffee and a price.
    All Order instances are recorded in Order._all
    """
    _all: List["Order"] = []

    def __init__(self, customer, coffee, price):
        # validations (delegated to properties)
        self._customer = None
        self._coffee = None
        self._price = None

        self.customer = customer
        self.coffee = coffee
        self.price = price

        # register order (single source of truth)
        Order._all.append(self)

    # ---------- customer property ----------
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        # lazy import to avoid circular imports at module load
        from customer import Customer  # type: ignore
        if not isinstance(value, Customer):
            raise TypeError("customer must be a Customer instance")
        self._customer = value

    # ---------- coffee property ----------
    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee  # type: ignore
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        self._coffee = value

    # ---------- price property ----------
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # accept int/float but store as float
        if not isinstance(value, (int, float)):
            raise TypeError("price must be a number")
        value = float(value)
        if not (150 <= value <= 1000):
            raise ValueError("price must be between 1.0 and 10.0")
        self._price = value

    # ---------- class utility ----------
    @classmethod
    def all(cls):
        return list(cls._all)

    def __repr__(self):
        return f"<Order customer={self.customer.name!r} coffee={self.coffee.name!r} price={self.price:.2f}>"
