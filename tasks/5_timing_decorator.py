"""Write a decorator that calculates execution time of given function"""
import time
from typing import Callable


def dec(func: Callable):
    def wrapper(*args, **kwargs):
        tstart = time.time()
        retval = func()
        print(f"Elapsed time: {time.time() - tstart:0.2f}s")

    return wrapper


@dec
def test_func():
    time.sleep(2)


test_func()
