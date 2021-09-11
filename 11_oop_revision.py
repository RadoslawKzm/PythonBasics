import math


class Rational:
    instances = []

    @classmethod
    def max(cls):
        return max(instance.number for instance in cls.instances)

    def __init__(self, number: float):
        self.number = number
        self.update_instances(self)

    @classmethod
    def update_instances(cls, self):
        cls.instances.append(self)

    @staticmethod
    def static(num_1: int, num_2: int):
        print(num_1 + num_2)

    def calculate(self) -> str:
        lst = str(self.number).split('.')
        len_second = len(lst[1])
        licznik = int(lst[1])
        mianownik = 10 ** len_second
        gcd = math.gcd(licznik, mianownik)
        licznik /= gcd
        mianownik /= gcd
        nowy_licznik = int(lst[0]) * mianownik + licznik
        return f"{int(nowy_licznik)}/{int(mianownik)}"

    def __str__(self) -> str:
        return self.calculate()

    def __repr__(self):
        return f"Rational class with args: {self.number = }, {self.instances = }"

    def __eq__(self, other) -> bool:
        return self.number == other

    def __lt__(self, other):
        return self.number < other

    def __le__(self, other):
        return self.number <= other

    def __gt__(self, other):
        return self.number > other

    def __ge__(self, other):
        return self.number >= other

    def __add__(self, other):
        new_obj = Rational(number=self.number + other)
        return str(new_obj)

    def __iadd__(self, other):
        self.number += other
        return self.calculate()

    def write_to_file(self, filename: str):
        with open(filename, "w") as f:
            f.write(f"{self.number = }")


tst = Rational(1.0008)
# print(f"{str(tst) = }")

tst2 = Rational(1.5)
# print(f"{str(tst) = }")
#
# tst.write_to_file("test.txt")
#
print("pass")


class Calculator:
    @staticmethod
    def add(first, second):
        return first + second

    @staticmethod
    def sub(first, second):
        return first - second
