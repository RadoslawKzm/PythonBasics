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