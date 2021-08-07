"""There are numerous datatypes in python, those included and those that need import.
Here we will discuss built-in datatypes in Python
"""

"""Strings, we all like them. It is always nice to see good content in a pair of nice quotes :D"""
string_1: str = "Hello world"
string_2: str = "Some random message"
print(f"{string_1 = }, some separator message, {string_2 = }\n")

"""Integers, numbers without floating points"""

# int: Integer data type, consists numbers from -2,147,483,647 to 2,147,483,647
first_int: int = 0
second_int: int = 10
third_int: int = -100

# But what would happen if we go beyond 2,147,483,647?
beyond_int: int = 2_147_483_649
# python converts int to internal long int. For us it is still int but inside one bit more on the left was added


"""Float, numbers with floating point and bad precession when going far from 0"""
# float: there are 2^64 possible floating numbers it gives 18446744073709551616
first_float: float = 21.37
second_float: float = 0.100_200_300_400_500_600_700_800_900_100_200_300_400_500_600_700_2
third_float: float = 0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_1
fourth_float: float = second_float - third_float
print(f"{fourth_float = }\n")
"""
Here we can see loosing precision. Some would say it is not meaningful. Sure for our example and many more it is not.
But what if you are a scientist or even better work in bank?
Did you heard story about hacker that stole 1 penny from each transaction :D?
"""


"""So one important digression, Decimal datatype. When we care about rounding precision :)"""

# fmt: off
import decimal

# fmt: on

decimal_1: decimal.Decimal = decimal.Decimal("0.100_200_300_400_500_600_700_800_900_100_200_300_400_500_600_700_2")
decimal_2: decimal.Decimal = decimal.Decimal("0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_1")
decimal_3: decimal.Decimal = decimal_1 - decimal_2
print(f"{decimal_3 = }")
"""What? But you told us we won't loose precision using decimal. What is going on.
Well, you don't loose precision with decimal but for precision you configure :D
Here we didn't configure any precision so we used default 28 places but our examples have 49 places"""

decimal.getcontext().prec = 50
decimal_4: decimal.Decimal = decimal.Decimal("0.100_200_300_400_500_600_700_800_900_100_200_300_400_500_600_700_2")
decimal_5: decimal.Decimal = decimal.Decimal("0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_1")
decimal_6: decimal.Decimal = decimal_4 - decimal_5
print(f"{decimal_6 = }")
print(f"{(decimal_6 + decimal_5) == decimal_4 = }\n")
