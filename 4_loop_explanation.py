"""Loops explanation"""

"""While loop example"""

var: int = 6
while var:  # if true than while loop will go even forever
    print(f"{var = }")
    var -= 1


class IteratorExample:
    def __init__(self, lst: list = None):
        self.lst = lst
        if not lst:
            self.lst = [1, 2, 3, 4]

    def __iter__(self):
        self.index_ = -1
        return self

    def __next__(self):
        self.index_ += 1
        if self.index_ == len(self.lst):
            raise StopIteration
        return self.lst[self.index_]


test_example = IteratorExample(lst=[1, 2, 3, 4])

for number in test_example:
    print(number)

print("pass")
lst = list(test_example)

"""Break and continiue example"""

for num in [1, 2, 3, 4]:  # Use debugger with this example with breakpoint in this line
    if num == 1:
        continue
    print("after continue")
    for letter in "ABCD":
        if letter == "B":
            break
        print(f"{letter = }")
    print(f"{num = }")

for num in range(10):
    print(f"{num = }")
    # print("dupa")

lst = list(range(10))

lst1 = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(lst1)):
    print(lst1[i])

for item in enumerate(lst1):
    a = item[0]
    b = item[1]
    c, d = item
    print(item)

evens = []
for i in range(11):
    if (i % 2) == 0:
        evens.append(i)

print(f"{evens = }")

evens2 = [num22 if (num22 % 2) == 0 else "dupa" for num22 in range(11)]

dict_comp = {key: val for key, *val in zip(range(2), range(10, 0, -1), range(10, 0, -1))}

set_comp = {i for i in range(10)}
