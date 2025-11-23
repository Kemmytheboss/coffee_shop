# tests/test_bonus.py
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

# Clear orders between tests
def teardown_function(fn):
    Order.all.clear()

# ---------- Customer edge cases ----------
def test_most_aficionado_no_orders():
    latte = Coffee("Latte")
    assert Customer.most_aficionado(latte) is None


def test_multiple_customers_most_aficionado():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")

    alice.create_order(latte, 500)
    alice.create_order(latte, 500)
    bob.create_order(latte, 500)

    # Alice total: 1200, Bob total:800
    assert Customer.most_aficionado(latte) == alice


def test_coffee_average_price_no_orders():
    espresso = Coffee("Espresso")
    assert espresso.average_price() == 0


def test_coffee_customers_unique():
    alice = Customer("Alice")
    latte = Coffee("Latte")

    # Alice orders Latte twice
    alice.create_order(latte, 500)
    alice.create_order(latte, 500)

    customers = latte.customers()
    assert len(customers) == 1
    assert customers[0] == alice


def test_customer_coffees_unique():
    alice = Customer("Alice")
    latte = Coffee("Latte")
    mocha = Coffee("Mocha")

    alice.create_order(latte, 500)
    alice.create_order(latte, 500)
    alice.create_order(mocha, 400)

    coffees = alice.coffees()
    assert len(coffees) == 2
    assert latte in coffees
    assert mocha in coffees


def test_price_validation():
    alice = Customer("Alice")
    latte = Coffee("Latte")

    with pytest.raises(Exception):
        alice.create_order(latte, 50)  # too low

    with pytest.raises(Exception):
        alice.create_order(latte, 1200)  # too high

    with pytest.raises(Exception):
        alice.create_order(latte, "free")  # not a number
