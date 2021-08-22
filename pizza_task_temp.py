"""We want to create pizzas
input: name_of_pizza, diameter, toppings, price, costs
functionalities:
- create pizza object with given parameters.
- compare pizzas which one is more area for value cm2/zl
- calculate overall gross income
- calculate overall costs
- calculate overall net income
"""


class Pizza:
    def __init__(self, *, name_of_pizza: str, diameter: int, toppings: list, price: float, costs: float):
        self.name_of_pizza = name_of_pizza
        self.diameter = diameter
        self.topping = toppings
        self.price = price
        self.costs = costs


margherita = Pizza(diameter=30, toppings=["cheese"], costs=10, name_of_pizza="Margherita", price=25.56)
capriciosa = Pizza(diameter=30, toppings=["cheese", "ham", "fungi"], costs=12, name_of_pizza="Capriciosa", price=28)
pepperoni = Pizza(diameter=30, toppings=["cheese", "salami"], costs=13.2, name_of_pizza="Pepperoni", price=32.15)
quatro_fromagio = Pizza(
    diameter=30, toppings=["cheese", "blue", "parmigiano"], costs=20, name_of_pizza="Quatro Fromagio", price=45
)
