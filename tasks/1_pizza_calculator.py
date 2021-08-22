"""Calculate pizza area to price ratio
input: price:float, d:int
output: area_cm per 1zl

should return ration cm2 for 1zl in cm2/zl
"""
from __future__ import annotations
from math import pi


def pizza_calculator(*, price: float, d: int):
    print(f"Provided {d}cm pizza for {price = }")
    area_cm = pi * (d / 2) ** 2
    print(f"You can buy: {area_cm / price:0.2f}cm2/1zl")


# fmt: off
from abc import ABC, abstractmethod
from typing import List


# fmt: on


class PizzaABC(ABC):
    @abstractmethod
    def __init__(self, *, price: float, d_cm: int, currency: str = None, toppings: List[str] = None):
        """Create pizza object"""

    @abstractmethod
    def get_ratio(self):
        """return self.area_cm / self.price"""

    @abstractmethod
    def __gt__(self, other: PizzaABC):
        """return True if self.get_ratio() > other.get_ratio() else False"""

    @abstractmethod
    def __ge__(self, other: PizzaABC):
        """return True if self.get_ratio() >= other.get_ratio() else False"""

    @abstractmethod
    def __lt__(self, other: PizzaABC):
        """return True if self.get_ratio() < other.get_ratio() else False"""

    @abstractmethod
    def __le__(self, other: PizzaABC):
        """return True if self.get_ratio() <= other.get_ratio() else False"""

    @abstractmethod
    def __eq__(self, other: PizzaABC):
        """return True if self.get_ratio() == other.get_ratio() else False"""

    @abstractmethod
    def __repr__(self):
        """fill out repr method"""

    @abstractmethod
    def __str__(self):
        """fill out str method"""


class Pizza(PizzaABC):
    def __init__(self, *, price: float, d_cm: int, name: str = None, currency: str = "zl", toppings: List[str] = None):
        self.price = price
        self.currency = currency
        self.diameter = d_cm
        self.name = name
        self.area_cm = pi * (self.diameter / 2) ** 2
        self.ratio = self.get_ratio()
        self.toppings = None
        if toppings:
            self.toppings: List[str] = [topping for topping in toppings]

    def get_ratio(self):
        return self.area_cm / self.price

    def __gt__(self, other: PizzaABC):
        return True if self.get_ratio() > other.get_ratio() else False

    def __ge__(self, other: PizzaABC):
        return True if self.get_ratio() >= other.get_ratio() else False

    def __lt__(self, other: PizzaABC):
        return True if self.get_ratio() < other.get_ratio() else False

    def __le__(self, other: PizzaABC):
        return True if self.get_ratio() <= other.get_ratio() else False

    def __eq__(self, other: PizzaABC):
        return True if self.get_ratio() == other.get_ratio() else False

    def __repr__(self):
        return f"{self.price=}, {self.currency=}, {self.diameter=}, {self.ratio=}, {self.toppings=}"

    def __str__(self):
        return (
            f"{self.name or 'Pizza'}: {self.diameter}cm bought for {self.price}{self.currency} \n"
            f"with toppings:{self.toppings} \n"
            f"overall ratio is {self.ratio:0.2f}cm2/1zl"
        )


if __name__ == "__main__":
    pizza_calculator(price=25, d=30)
    pizza_calculator(price=40, d=40)

    pizza1 = Pizza(price=25, d_cm=30)
    print(f"{pizza1.get_ratio():0.2f}cm2")
    pizza2 = Pizza(price=40, d_cm=50, name="Kaprikosa z czoskowym")
    print(f"{pizza2.get_ratio():0.2f}cm2")
    print(f"{pizza2 > pizza1 = }")
    print(f"{pizza2 < pizza1 = }")
    print(f"{pizza2 >= pizza1 = }")
    print(f"{pizza2 <= pizza1 = }")
    print(f"{pizza2 == pizza1 = }")
    print(pizza1)
    print(pizza2)
