"""There are numerous datatypes in python, those included and those that need import.
Here we will discuss built-in datatypes in Python
"""

"""Strings, we all like them. It is always nice to see good content in a pair of nice quotes :D"""
string_1: str = "Hello world"
string_2: str = "Some random message"
print(f"{string_1 = }, some separator message, {string_2 = }\n")

backup_print = print
print = 2
import sys
def new_print(word:str):
    sys.stdout.write(f"{word}\n")

new_print("test dupa")


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

"""None type. There is python specific design pattern that states if somewhere returns nothing should return None"""
none_1 = None

"""Booleans. They are simple, just True or False or maybe not :D?"""
bool_1: bool = True
bool_2: bool = False
print(f"{bool_1 = }, {bool_2 = }")
# We can test something if it is true or false
print(f"1 is True: {bool(1)}")
print(f"'some string' is True: {bool('some string')}")
print(f"[1,2,3,4] is True: {bool([1, 2, 3, 4])}")
print(f"None is True: {bool(None)}\n")

"""We can check any data type using built-in function type(data)"""
print(f"{type(first_int) = }, {type(first_float) = }, {type(string_1) = }, {type(decimal_1) = }, {type(none_1) = }")
print(f"{int.mro() = }, {float.mro() = }, {str.mro() = }, {decimal.Decimal.mro() = }, {bool.mro() = }\n")

"""
More advanced containers for data, previously we had more basic types.
"""

"""Tuples, something like lists but immutable. RULE OF THUMB > DO NOT PUT mutable inside immutables."""
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = ("one", "two", "three", "four", "five")
tuple_3 = ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])  # SOOOOOO BAD, don't do it.
print(f"{tuple_1[0] = }, {tuple_1[1] = }, {tuple_1[2] = }, {tuple_1[3] = }, {tuple_1[4] = }")
print(f"{tuple_2[0] = }, {tuple_2[1] = }, {tuple_2[2] = }, {tuple_2[3] = }, {tuple_2[4] = } \n")

"""Lists: indexable data container where index can be also a form of data"""
list_1 = [1, 2, 3, 4, 5]
list_2 = ["one", "two", "three", "four", "five"]
list_3 = list_1 + list_2
print(f"{list_1 = }, \n{list_2 = }, \n{list_3 = }\n")
print(f"{list_1[0] = }, {list_1[1] = }, {list_1[2] = }, {list_1[3] = }, {list_1[4] = }")
print(f"{list_2[0] = }, {list_2[1] = }, {list_2[2] = }, {list_2[3] = }, {list_2[4] = } \n")

"""Dictionaries, hash tables in python. Providing 0[1] lookup time"""
dictionary_1 = {1: 1, 2: 2, 3: 3, 4: 4}
dictionary_2 = {"one": 1, "two": 2, "three": 3, "four": 4}
dictionary_3 = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(f"{dictionary_1 = }")
print(f"{dictionary_2 = }")
print(f"{dictionary_3 = }")
print(f"{dictionary_1[1] = } \n{dictionary_2['two']= } \n{dictionary_3['key3'] = }\n")

"""Sets, dictionaries where value is a pointer to a key. Sets same as dict keys don't allow same values"""
set_1 = {1, 2, 3, 4, 1, 2, 3, 4}
print(f"{set_1 = }")

"""Deque: double ended queue. Best for making queues and stacks"""
# fmt: off
from collections import deque

# fmt: on

deq = deque(range(10))
deq.append(11)
deq.appendleft(-1)
deq_pop_left = deq.popleft()
deq_pop = deq.pop()

lst = list(range(10))
lst.append(11)
lst_pop = lst.pop()

# FIFO queue ( first in - first out)
deq1 = deque(range(10))
deq1.append(int(input("podaj liczbe")))
while deq1:
    print(deq1.popleft())

# FILO queue ( first in - last out)
deq2 = deque(range(10))
deq2.append(20)
while deq2:
    print(deq2.pop())


# lst = list(range(1_000_000_0))
# st = set(range(1_000_000_0))
#
# print("starting")
# import time
# t_start = time.time()
# print(f"{999_999_999_999_999 in lst}")
# print(f"elapsed time: {time.time() - t_start:0.4f}")
#
# t_start = time.time()
# print(f"{999_999_999_999_999 in st}")
# print(f"elapsed time: {time.time() - t_start:0.4f}")
