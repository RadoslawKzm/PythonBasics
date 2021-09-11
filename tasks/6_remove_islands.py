"""
You are given input:
matrix =
[
    [1,0,0,0,0,0],
    [0,1,0,1,1,1],
    [0,0,1,0,1,0],
    [1,1,0,0,1,0],
    [1,0,1,1,0,0],
    [1,0,0,0,0,1]
]
expected output =
[
    [1,0,0,0,0,0],
    [0,0,0,1,1,1],
    [0,0,0,0,1,0],
    [1,1,0,0,1,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,1]
]
(0,0), (3,1), (4,1), (5,1), (4,2), (0,3), (1,3), (4,3), (0,4), (0,5), (5,5)

removed ones:
[
    [-,-,-,-,-,-],
    [-,X,-,-,-,-],
    [-,-,X,-,-,-],
    [-,-,-,-,-,-],
    [-,-,X,X,-,-],
    [-,-,-,-,-,-]
]
{(1,1), (2,2), (2,4), (3,4)}

Create an algorithm that will clear all islands not connected to a border.
"""
from typing import List

input_ = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]


def remove_islands(*, matrix: List[List], token):
    pass


output = remove_islands(matrix=input_, token=1)
