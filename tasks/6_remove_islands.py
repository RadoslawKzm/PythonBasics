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
from typing import List, Tuple

input_ = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]


def is_xy_valid(*, x: int, y: int, token: int, matrix: List[list]) -> bool:
    max_y: int = len(matrix) - 1
    if not (0 <= y <= max_y):
        return False
    max_x: int = len(matrix[y]) - 1
    if not (0 <= x <= max_x):  # check for out of borders point
        return False
    if matrix[y][x] != token:  # this is for different tokens to look for instead of example 1
        return False
    return True


def check_point(
        *,
        points: set,
        set_of_results: set,
        point: Tuple[int, int],
        token,
        matrix: List[list],
        prev: Tuple[int, int] = frozenset([(-1, -1)]),
):
    x, y = point
    if not is_xy_valid(x=x, y=y, token=token, matrix=matrix):
        return None
    set_of_results.add((x, y))
    for new_xy in {(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)}.difference({prev}):
        check_point(points=points, set_of_results=set_of_results, point=new_xy, prev=point, matrix=matrix, token=token)


def remove_islands(*, matrix: List[List], token):
    set_of_results: set = set()

    t1: list = [(i, 0) for i in range(len(matrix[0]))]
    t2: list = [(i, len(matrix) - 1) for i in range(len(matrix[0]))]
    t3: list = [(0, i) for i in range(len(matrix[0]))]
    t4: list = [(len(matrix) - 1, i) for i in range(len(matrix[0]))]
    points: set = {(x, y) for iterable in [t1, t2, t3, t4] for x, y in iterable if matrix[y][x] == token}
    # for iterable in [t1, t2, t3, t4]:
    #     for x,y in iterable:
    #         if matrix[y][x] == token:
    #             points.add((x,y))
    for point in points:
        check_point(points=points, set_of_results=set_of_results, point=point, matrix=matrix, token=token)
    return set_of_results


output = remove_islands(matrix=input_, token=1)
