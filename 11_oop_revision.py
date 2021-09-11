import math


class Rational:
    def __init__(self, number: float):
        self.number = number

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
        return self.calculate()

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




tst = Rational(1.0008)
print(f"{str(tst) = }")

tst = Rational(1.5)
print(f"{str(tst) = }")

bool(tst == 2)

var = tst + 2
tst += 2

print("pass")
