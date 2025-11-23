from order import Order

class Customer:
    all = [] # Class-level list to store all Customer instances

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):# Validate that name is a string of length 1-15
            raise TypeError("Customer name must be a string")
        value = value.strip() #removes any blank spaces from strings and prevents them from being counted as chracters
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be 1-15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        highest_customer = None
        highest_amount = 0
        for customer in cls.all:
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > highest_amount:
                highest_amount = total
                highest_customer = customer
        return highest_customer