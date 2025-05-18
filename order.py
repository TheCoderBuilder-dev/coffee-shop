# order.py

class Order:
    def __init__(self, customer, coffee, price):
 
        if customer is None:
            raise Exception("You must give a customer.")
        
        if coffee is None:
            raise Exception("You must give a coffee.")

        if type(price) != float and type(price) != int:
            raise Exception("Price must be a number.")
        
        if price < 1.0 or price > 10.0:
            raise Exception("Price must be between 1.0 and 10.0.")


        self.customer = customer
        self.coffee = coffee
        self.price = price
