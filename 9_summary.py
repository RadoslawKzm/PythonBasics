"""How to do generator
1. What is generator
2. Memory management in generator
3. Implement simple generator with yield
4. Pros of generators: low memory consumption
5. Cons of generators: Not as fast as allocated variable
"""
from random import randint


def simple_generator(*, how_many: int):
    current_state = 0
    while current_state < how_many:
        current_state += 1
        yield randint(0, 9)


for item in simple_generator(how_many=20):
    print(f"{item = }")
    print("pass")

gen_comp = (randint(0, 9) for _ in range(20))

sim_gen = [item for item in simple_generator(how_many=20)]
gen = [item for item in gen_comp]


class Gen:
    def __init__(self):
        self.something = True

    def __iter__(self):
        pass

    def __next__(self):
        # end clause
        if self.something:
            raise StopIteration
        pass


"""How to do context manager
1. What is this f
2. What is with
3. Exception handling inside

"""

with open("0_data_types.py", "r") as f:
    for line in f:
        print(f"{line = }")


class Context:
    def __init__(self, *, suppress: bool = False):
        self.suppress = suppress

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if any((exc_type, exc_val, exc_tb)):
            return self.suppress
        print("do something after function")


# How to do decorator

def decorator(func):
    print("inside decorator")

    def wrapper(*args, **kwargs):
        print("do something b4 function call")
        result = func(*args, **kwargs)
        print("do something after function call")
        return result

    return wrapper


@decorator
def dummy_func(*, dupa: str):
    print("inside dummy")
    print(f"{dupa = }")


# dummy_func = decorator(dummy_func)

dummy_func(dupa="test")


# decorator with parameters
def parametrized(param):
    print(f"parametrized param = {param}")
    param += 1

    def decorator2(func):
        print("inside decorator")
        print(f"decorator param = {param}")

        def wrapper2(*args, **kwargs):
            print(f"wrapper param = {param}")
            print("do something b4 function call")
            result = func(*args, **kwargs)
            print("do something after function call")
            return result

        return wrapper2

    return decorator2


@parametrized(5)
def dummy2(t1, t2="test"):
    print(f"{t1 = }")
    print(f"{t2 = }")
    return t2

dummy2(1, t2="test2")
