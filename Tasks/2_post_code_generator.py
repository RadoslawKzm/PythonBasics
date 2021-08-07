"""Create function that generates XX-XXX postal code
input:
min = "84-000", max = "86-000"
output:
list containing ['84-000', '84-001', ..., '85-999', '86-000']
"""

from typing import List


def post_gen(*, min_: str, max_: str) -> List[str]:
    min_ = int(min_.replace("-", ""))
    max_ = int(max_.replace("-", ""))
    list_ = []
    for num in range(min_, max_ + 1):
        num = str(num)
        list_.append(f"{num[0:2]}-{num[2:]}")
    return list_


def post_gen_upgraded(*, min_: str, max_: str) -> List[str]:
    min_ = int(min_.replace("-", ""))
    max_ = int(max_.replace("-", ""))
    return [f"{str(num)[0:2]}-{str(num)[2:]}" for num in range(min_, max_ + 1)]


if __name__ == "__main__":
    print(post_gen(min_="84-000", max_="84-010"))
    print(post_gen_upgraded(min_="84-000", max_="84-010"))
