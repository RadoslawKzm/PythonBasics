"""We want to create pizzas
input: name_of_pizza, diameter, toppings, price, costs
functionalities:
- create pizza object with given parameters.
- compare pizzas which one is more area for value cm2/zl
- calculate overall gross income
- calculate overall costs
- calculate overall net income
"""
from __future__ import annotations

from math import pi


class AreaRatioStrategy:
    def __gt__(self, other: Pizza) -> bool:
        # if self.ratio > other.ratio:
        #     return True
        # return False
        return True if self.ratio > other.ratio else False

    def __ge__(self, other: Pizza) -> bool:
        return True if self.ratio >= other.ratio else False

    def __lt__(self, other: Pizza) -> bool:
        return True if self.ratio < other.ratio else False

    def __le__(self, other: Pizza) -> bool:
        return True if self.ratio <= other.ratio else False

    def __eq__(self, other: Pizza) -> bool:
        return True if self.ratio == other.ratio else False


class PriceStrategy:
    def __gt__(self, other: Pizza) -> bool:
        # if self.ratio > other.ratio:
        #     return True
        # return False
        return True if self.price > other.price else False

    def __ge__(self, other: Pizza) -> bool:
        return True if self.price >= other.price else False

    def __lt__(self, other: Pizza) -> bool:
        return True if self.price < other.price else False

    def __le__(self, other: Pizza) -> bool:
        return True if self.price <= other.price else False

    def __eq__(self, other: Pizza) -> bool:
        return True if self.price == other.price else False


class Pizza(PriceStrategy):
    avail_strategies = {"price": PriceStrategy, "area_price_ratio": AreaRatioStrategy}

    def __init__(self, *, name: str, diameter: int, toppings: list, price: float, costs: float):
        self.name = name
        self.diameter = diameter
        self.topping = toppings
        self.price = price
        self.costs = costs

        self.area = pi * (self.diameter / 2) ** 2
        self.ratio = self.area / self.price


margherita = Pizza(diameter=30, toppings=["cheese"], costs=10, name="Margherita", price=25.56)
capriciosa = Pizza(diameter=30, toppings=["cheese", "ham", "fungi"], costs=12, name="Capriciosa", price=28)
pepperoni = Pizza(diameter=30, toppings=["cheese", "salami"], costs=13.2, name="Pepperoni", price=32.15)
quatro_fromagio = Pizza(
    diameter=30, toppings=["cheese", "blue", "parmigiano"], costs=20, name="Quatro Fromagio", price=45
)

print(f"{margherita > capriciosa = }")
