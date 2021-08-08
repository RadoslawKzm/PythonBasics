"""We want to creat pizzas
input: name_of_pizza, diameter, toppings, price, costs
functionalities:
- create pizza object with given parameters.
- compare pizzas which one is more area for value
- calculate overall gross income
- calculate overall costs
- calculate overall net income
"""


class Pizza:
    how_many_pizzas_done = 0

    def __init__(self, *, name: str, d_cm: int, price_zl: float, costs_zl: float, toppings: list = None):
        self.name = name
        self.diameter_cm = d_cm
        self.price_zl = price_zl
        self.costs_zl = costs_zl
        self.toppings = toppings
        if not self.toppings:
            self.toppings = []
        self.update_counter()

    @classmethod
    def update_counter(cls):
        cls.how_many_pizzas_done += 1


pizza1 = Pizza(name="Kaprikosa", d_cm=32, price_zl=25, costs_zl=5, toppings=["ser", "szynka", "pieczarki"])
pizza2 = Pizza(name="Margerita", d_cm=40, price_zl=30, costs_zl=10, toppings=["ser"])
pizza3 = Pizza(name="Pepperoni", d_cm=50, price_zl=40, costs_zl=15, toppings=["ser", "salami"])
