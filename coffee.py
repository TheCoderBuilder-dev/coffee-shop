class Coffee:
    def __init__(self, name):
        if type(name) == str and len(name) >= 3:
            self.name = name
        else:
            raise Exception("Coffee name must be 3 or more characters.")

        self.orders_list = []

    def get_orders(self):
        return self.orders_list

    def get_customers(self):
        customers = []
        for order in self.orders_list:
            if order.customer not in customers:
                customers.append(order.customer)
        return customers

    def count_orders(self):
        return len(self.orders_list)

    def get_average_price(self):
        if len(self.orders_list) == 0:
            return 0

        total = 0
        for order in self.orders_list:
            total += order.price

        average = total / len(self.orders_list)
        return average
