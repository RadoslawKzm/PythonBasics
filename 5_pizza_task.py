"""We want to creat pizzas
input: name_of_pizza, diameter, toppings, price, costs
functionalities:
- create pizza object with given parameters.
- calculate overall gross income
- calculate overall costs
- calculate overall net income
- compare pizzas which one is more area for value
"""


class Pizza:
    how_many_pizzas_done = 0

    def __init__(self, name: str, d: int, price: float, costs: float, toppings: list = None):
        self.name = name
        self.diameter = d
        self.price = price
        self.costs = costs
        self.toppings = toppings
        if not self.toppings:
            self.toppings = []
        self.update_counter()

    @classmethod
    def update_counter(cls):
        cls.how_many_pizzas_done += 1


pizza1 = Pizza()
pizza2 = Pizza()
pizza3 = Pizza()
