from coffee import MENU
from customer import Customer
from order import Order

def teardown_function():
    Customer.customers.clear() 
    Order.all.clear()

def test_create_order():
    customer = Customer("Alice")
    order = Order(customer, "Latte")
    assert order.customer == customer
    assert order.coffee_name == "Latte"
    assert order in Order.all
    assert alice.orders() == [order]
    assert latte.orders() == [order]
    assert latte.number_of_orders() == 1
    assert latte.average_price() == 250
    assert aice.total_spent() == 250