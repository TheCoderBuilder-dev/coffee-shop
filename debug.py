from customer import Customer
from coffee import Coffee

latte = Coffee("Latte")
mocha = Coffee("Mocha")

brian = Customer("Brian")
alice = Customer("Alice")
mike = Customer("Mike")

brian.make_order(latte, 3.5)
brian.make_order(mocha, 4.0)
alice.make_order(mocha, 5.0)
mike.make_order(latte, 2.5)
mike.make_order(latte, 3.0)

print("Most loyal customer for Latte:", Customer.most_loyal_customer(latte).name)
print("Most loyal customer for Mocha:", Customer.most_loyal_customer(mocha).name)
print("Coffees Brian has ordered:", [c.name for c in brian.get_coffees()])
