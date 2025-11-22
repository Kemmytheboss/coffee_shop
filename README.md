START
print "Welcome to Coffee Shop"
load MENU


order_list = []


WHILE user wants to order:
display MENU
item = user selects menu item
quantity = ask user quantity


add {item, quantity} to order_list


ask user "Do you want another item? (yes/no)"
END WHILE


total = 0
FOR each order in order_list:
subtotal = order.item.price * order.quantity
total = total + subtotal
END FOR


print "Your total is: $", total


payment = ask user for money


IF payment < total:
print "Insufficient funds"
RESTART payment
ELSE
change = payment - total
print "Payment accepted"
print "Your change: $", change
END IF


print receipt with all items, total, payment, change
print "Thank you for your purchase!"
END