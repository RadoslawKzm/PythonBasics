"""Crete object that accepts some iterable and will return first inserted object"""
from typing import Iterable
from collections import deque


class Fifo:
    def __init__(self, *, input_: Iterable[int]):
        self.deq = deque(input_)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.deq:
            raise StopIteration
        return self.deq.popleft()

    def insert(self, number: int):
        self.deq.append(number)

    def __iadd__(self, other):
        self.deq.append(other)
        return self


fifo = Fifo(input_=[1, 2, 3, 4, 5, 6, 7, 8])
gen = fifo.__iter__()
first = fifo.__next__()
second = fifo.__next__()
third = fifo.__next__()
fifo.insert(9)
fifo += 1

for member in fifo:
    print(f"{member}")
