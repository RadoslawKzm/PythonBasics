from __future__ import annotations
from typing import Callable, Union, Iterator


def dummy() -> None:
    pass


def test(*, func: Callable, var: Union[list, tuple], var1: Iterator = (1, 2, 3)) -> Union[Callable, str]:
    var2: int = 0
    str1: str = "test"
    var3 = func or var
    return func or str1


test(func=dummy, var=[1])


class TestClass:
    def test_method(self, func: TestClass):
        pass
