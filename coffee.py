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