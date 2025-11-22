#debug.py 
from customer import Customer
from coffee import MENU

# Create some test data
alice = customer("Alice")
bob = customer("Bob")
latte = coffee("Latte")
espresso = coffee("Espresso")

# Create some test orders
alice.test_create_order(latte, 250)
alice.test_create_order(espresso, 200)
bob.test_create_order(espresso, 200)
bob.test_create_order(latte, 250)

# print hekppful debug information
print("All orders:", __import__('order').Order.all())
print("Latte orders:", latte.orders())
print("Latte customers:", latte.customers())
print("Latte num_orders:", latte.number_of_orders())
print("Latte average_price:", latte.average_price())
print("Alice total_spent:", alice.total_spent())
print("Most aficionado for Latte:", Customer.most_aficionado(latte))
print("Most popular coffee:", coffee.most_popular())