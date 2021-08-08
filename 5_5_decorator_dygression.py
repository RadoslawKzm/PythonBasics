from time import time


def decorator(func):
    print("w decoratorze")

    def wrapper(*args, **kwargs):
        tstart = time()
        output = func(*args, **kwargs)
        print(f"Elapsed time: {time() - tstart}")

    return wrapper


print("pass")


@decorator
def example(test, dupa=None):
    print("w examplu")


decorator(example)

example(1, dupa=5)
