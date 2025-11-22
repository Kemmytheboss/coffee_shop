from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

c1.create_order(latte, 5)
c1.create_order(mocha, 7)
c2.create_order(latte, 6)

print("Alice's Coffees:", [c.name for c in c1.coffees()])
print("Latte Orders:", latte.num_orders())
print("Latte Avg Price:", latte.average_price())
print("Most Aficionado for Latte:", Customer.most_aficionado(latte).name)
