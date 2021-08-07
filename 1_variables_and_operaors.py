"""What is variable? What is operator?"""

"""Variables are containers for information like a package is for our things we buy from the internet"""
variable_1 = "some text"
print(variable_1)
our_print = print
our_print(variable_1)  # weird? everything in python is an object so we can allocate everything to a new variable

# fmt: off
import sys


# fmt: on


def example(msg: str):
    sys.stdout.write("Inside example function.\n")
    sys.stdout.write(f"{msg}\n")


print_backup = print
print = example
print("Nice example for you :)")
print = print_backup
print("\n")

# fmt: off
# Python3 style guide: python.org/dev/peps/pep-0008/
import webbrowser

# fmt:on
# webbrowser.open("https://python.org/dev/peps/pep-0008/")

"""Operators: we have arithmetic and others. Some examples above."""
print(f"{'Kazimierz' + 'Wielki' = }")
print(f"{'Jarek ' * 10 = }")
print(f"{2 ** 4 = }")
print(f"{20/16.3333 = :.4f}\n")

# inplace operators
a = 1
a += 1
b = 2
b = b + 2  # Equivalent of  b += 2
print(f"{a = }\n")

# membership testing operators:
set_1 = {1, 2, 3, 4, 5}
print(f"{1 in set_1 = }, {6 in set_1 = }\n")
print(f"{1 not in set_1 = }, {6 not in set_1 = }\n")

