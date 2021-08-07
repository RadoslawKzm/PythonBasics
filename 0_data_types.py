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

