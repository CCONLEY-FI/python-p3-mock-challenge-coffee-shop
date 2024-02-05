from statistics import mean
# Deliverables
# Write the following methods in the classes in the files provided. Feel free to
# build out any helper methods if needed.
# Customer
# - `Customer __init__(self, name)`
#   - Customer is initialized with a name
# - `Customer property name`
#   - Returns customer's name
#   - Names must be of type `str`
#   - Names must be between 1 and 15 characters, inclusive
#   - Should **be able** to change after the customer is instantiated
# - `Customer orders()`
#   - Returns a list of all orders for that customer
#   - Orders must be of type `Order`
# - `Customer coffees()`
#   - Returns a **unique** list of all coffees a customer has ordered
#   - Coffees must be of type `Coffee`
# - `Customer create_order(coffee, price)`
#   - Receives a **coffee object** and a **price number** as arguments
#   - Creates and returns a new Order instance and associates it with that
#     customer and the coffee object provided.
# - `Customer classmethod most_aficionado(coffee)`
#   - Receives a **coffee object** argument
#   - Returns the `Customer` instance that has spent the most money on the coffee
#     instance provided as argument.
#   - Returns `None` if there are no customers for the coffee instance provided.
#   - _hint: will need a way to remember all `Customer` objects_
# Coffee
# - `Coffee __init__(self, name)`
#   - Coffee is initialized with a name
# - `Coffee property name`
#   - Returns the coffee's name
#   - Names must be of type `str`
#   - Names length must be greater or equal to 3 characters
#   - Should **not be able** to change after the coffee is instantiated
#   - _hint: `hasattr()`_
# - `Coffee orders()`
#   - Returns a list of all orders for that coffee
#   - Orders must be of type `Order`
# - `Coffee customers()`
#   - Returns a **unique** list of all customers who have ordered a particular
#     coffee.
#   - Customers must be of type `Customer`
# - `Coffee num_orders()`
#   - Returns the total number of times a coffee has been ordered
#   - Returns `0` if the coffee has never been ordered
# - `Coffee average_price()`
#   - Returns the average price for a coffee based on its orders
#   - Returns `0` if the coffee has never been ordered
#   - Reminder: you can calculate the average by adding up all the orders prices
#     and dividing by the number of orders
# Order
# - `Order __init__(self, customer, coffee, price)`
#   - Order is initialized with a `Customer` instance, a `Coffee` instance, and a
#     price
# - `Order property price`
#   - Returns the price for the order
#   - Prices must be of type `float`
#   - Price must be a number between 1.0 and 10.0, inclusive
#   - Should **not be able** to change after the order is instantiated
#   - _hint: `hasattr()`_
# - `Order property customer`
#   - Returns the customer object for that order
#   - Must be of type `Customer`
# - `Order property coffee`
#   - Returns the coffee object for that order
#   - Must be of type `Coffee`


class Customer:
    all_customers = []

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = []
        Customer.all_customers.append(self)
        self.most_aficionado = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return self._orders

    def create_order(self, coffee, price):
        if not isinstance(price, (int, float)) or not 1.0 <= price <= 10.0:
            raise ValueError("Price must be a number between 1.0 and 10.0.")
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order

    def coffees(self):
        orders = self.orders()
        return list({order.coffee for order in orders})
    
    @staticmethod
    def most_aficionado(coffee):
        max_spent = 0
        most_aficionado_customer = None
        for customer in Customer.all_customers:
            orders = customer.orders()
            total_spent = sum(order.price for order in orders if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                most_aficionado_customer = customer
        return most_aficionado_customer

class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string of at least 3 characters.")
        self.__name = name
        self._orders = []

    @property
    def name(self):
        return self.__name

    def orders(self):
        return self._orders

    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError("Only instances of Order can be added.")
        self._orders.append(order)

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        if not self.orders():
            return 0
        return sum(order.price for order in self.orders()) / len(self.orders())


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, (int, float)) or not 1.0 <= price <= 10.0:
            raise ValueError("Price must be a number between 1.0 and 10.0.")
        self.__price = price
        self.customer = customer
        self.coffee = coffee

        coffee.add_order(self)
        customer._orders.append(self)
        Order.all.append(self)

    @property
    def price(self):
        return self.__price

# failed tests
# class Customer:
#     all_customers = []

#     def __init__(self, name):
#         if not isinstance(name, str) or not (1 <= len(name) <= 15):
#             raise ValueError("Name must be a string between 1 and 15 characters.")
#         self.name = name
#         self.orders = []
#         Customer.all_customers.append(self)

#     def create_order(self, coffee, price):
#         if not isinstance(price, (int, float)) or not 1.0 <= price <= 10.0:
#             raise ValueError("Price must be a number between 1.0 and 10.0.")
#         new_order = Order(self, coffee, price)
#         self.orders.append(new_order)
#         return new_order

#     def coffees(self):
#         return list({order.coffee for order in self.orders})

#     @staticmethod
#     def most_aficionado(coffee):
#         max_spent = 0
#         most_aficionado_customer = None
#         for customer in Customer.all_customers:
#             total_spent = sum(order.price for order in customer.orders if order.coffee == coffee)
#             if total_spent > max_spent:
#                 max_spent = total_spent
#                 most_aficionado_customer = customer
#         return most_aficionado_customer


# class Coffee:
#     def __init__(self, name):
#         if not isinstance(name, str) or len(name) < 3:
#             raise ValueError("Coffee name must be a string of at least 3 characters.")
#         self.name = name
#         self.orders = []

#     def add_order(self, order):
#         if not isinstance(order, Order):
#             raise TypeError("Only instances of Order can be added.")
#         self.orders.append(order)

#     def customers(self):
#         return list({order.customer for order in self.orders})

#     def num_orders(self):
#         return len(self.orders)

#     def average_price(self):
#         if not self.orders:
#             return 0
#         return sum(order.price for order in self.orders) / len(self.orders)


# class Order:
#     all_orders = []

#     def __init__(self, customer, coffee, price):
#         if not isinstance(price, (int, float)) or not 1.0 <= price <= 10.0:
#             raise ValueError("Price must be a number between 1.0 and 10.0.")
#         self.price = price
#         self.customer = customer
#         self.coffee = coffee
#         coffee.add_order(self)
#         customer.orders.append(self)
#         Order.all_orders.append(self)

# class Customer:
#     _all_customers = []

#     def __init__(self, name: str):
#         if not isinstance(name, str) or not (1 <= len(name) <= 15):
#             raise ValueError(
#                 "Name must be a string between 1 and 15 characters.")
#         self.__name = name
#         self.__orders = []
#         Customer._all_customers.append(self)

#     @property
#     def name(self) -> str:
#         return self.__name

#     @name.setter
#     def name(self, value: str) -> None:
#         if not isinstance(value, str) or not (1 <= len(value) <= 15):
#             raise ValueError(
#                 "Name must be a string between 1 and 15 characters.")
#         self.__name = value

#     def orders(self) -> list:
#         return self.__orders.copy()

#     def coffees(self) -> list:
#         return list({order.coffee for order in self.__orders})

#     def create_order(self, coffee, price):
#         if not isinstance(price, (int, float)) or not 1.0 <= price <= 10.0:
#             raise ValueError("Price must be a number between 1.0 and 10.0.")
#         new_order = Order(self, coffee, float(price))
#         self.__orders.append(new_order)
#         return new_order

#     @classmethod
#     def most_aficionado(cls, coffee):
#         return max(cls._all_customers, key=lambda customer: sum(order.price for order in customer.orders() if order.coffee == coffee), default=None)

# class Coffee:
#     def __init__(self, name: str):
#         if not isinstance(name, str) or len(name) < 3:
#             raise ValueError(
#                 "Coffee name must be a string of at least 3 characters.")
#         self.__name = name
#         self.__orders = []

#     @property
#     def name(self) -> str:
#         return self.__name

#     def orders(self) -> list:
#         return self.__orders.copy()

#     def customers(self) -> list:
#         return list({order.customer for order in self.__orders})

#     def num_orders(self) -> int:
#         return len(self.__orders)

#     def average_price(self) -> float:
#         if not self.__orders:
#             return 0
#         return sum(order.price for order in self.__orders) / len(self.__orders)

#     def add_order(self, order) -> None:
#         if not isinstance(order, Order):
#             raise TypeError("Only instances of Order can be added.")
#         self.__orders.append(order)


# class Order:
#     all = []

#     def __init__(self, customer: Customer, coffee: Coffee, price: float):
#         if not isinstance(price, (int, float)) or not 1.0 <= price <= 10.0:
#             raise ValueError("Price must be a number between 1.0 and 10.0.")
#         self.__price = float(price)
#         self.__customer = customer
#         self.__coffee = coffee
#         coffee.add_order(self)
#         customer._Customer__orders.append(self)
#         Order.all.append(self)

#     @property
#     def price(self) -> float:
#         return self.__price

#     @property
#     def customer(self) -> Customer:
#         return self.__customer

#     @property
#     def coffee(self) -> Coffee:
#         return self.__coffee



### first attempt, failed tests ###
# class Customer:
#     _all_customers = []  # This stores all instances of Customer

#     def __init__(self, name):
#         if not isinstance(name, str) or not (1 <= len(name) <= 15):
#             raise ValueError("Name must be a string between 1 and 15 characters.")
#         self._name = name
#         self._orders = []
#         Customer._all_customers.append(self)

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str) or not (1 <= len(value) <= 15):
#             raise ValueError("Name must be a string between 1 and 15 characters.")
#         self._name = value

#     @property
#     def orders(self):
#         return self._orders.copy()

#     @property
#     def coffees(self):
#         return list({order.coffee for order in self._orders})

#     def create_order(self, coffee, price):
#         if not isinstance(price, (int, float)) or not 1.0 <= price <= 10.0:
#             raise ValueError("Price must be a number between 1.0 and 10.0.")
#         new_order = Order(self, coffee, float(price))
#         self._orders.append(new_order)
#         return new_order

#     @classmethod
#     def most_aficionado(cls, coffee):
#         max_spent = 0
#         most_aficionado = None
#         for customer in cls._all_customers:
#             total_spent = sum(order.price for order in customer._orders if order.coffee == coffee)
#             if total_spent > max_spent:
#                 max_spent = total_spent
#                 most_aficionado = customer
#         return most_aficionado

# class Coffee:
#     def __init__(self, name):
#         if not isinstance(name, str) or len(name) < 3:
#             raise ValueError("Coffee name must be a string of at least 3 characters.")
#         self._name = name
#         self._orders = []

#     @property
#     def name(self):
#         return self._name

#     @property
#     def orders(self):
#         return self._orders.copy()

#     @property
#     def customers(self):
#         return list({order.customer for order in self._orders})

#     def num_orders(self):
#         return len(self._orders)

#     def average_price(self):
#         if not self._orders:
#             return 0
#         return sum(order.price for order in self._orders) / len(self._orders)

#     def add_order(self, order):
#         if not isinstance(order, Order):
#             raise TypeError("Only instances of Order can be added.")
#         self._orders.append(order)

# class Order:
#     all = []  # This stores all instances of Order

#     def __init__(self, customer, coffee, price):
#         if not isinstance(price, (int, float)) or not 1.0 <= price <= 10.0:
#             raise ValueError("Price must be a number between 1.0 and 10.0.")
#         self._price = float(price)
#         self._customer = customer
#         self._coffee = coffee

#         coffee.add_order(self)
#         customer._orders.append(self)
#         Order.all.append(self)

#     @property
#     def price(self):
#         return self._price

#     @property
#     def customer(self):
#         return self._customer

#     @property
#     def coffee(self):
#         return self._coffee
