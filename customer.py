class Customer:
    def __init__(self, name):
        if type(name) == str and len(name) >= 1 and len(name) <= 15:
            self.name = name
        else:
            raise Exception("Name must be between 1 and 15 characters.")
        self.orders_list = []

    def get_orders(self):
        return self.orders_list

    def get_coffees(self):
        coffees = []
        for order in self.orders_list:
            if order.coffee not in coffees:
                coffees.append(order.coffee)
        return coffees

    def make_order(self, coffee, price):
        from order import Order 

        new_order = Order(self, coffee, price)
        self.orders_list.append(new_order)

        coffee.orders_list.append(new_order)

        return new_order

    @classmethod
    def most_loyal_customer(cls, coffee):
        customers = coffee.get_customers()

        if len(customers) == 0:
            return None

        highest = 0
        best_customer = None
        for customer in customers:
            total = 0
            for order in customer.get_orders():
                if order.coffee == coffee:
                    total += order.price
            if total > highest:
                highest = total
                best_customer = customer

        return best_customer
