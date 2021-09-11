# 1,dupa,test
# 2,nazwa,nazwisko
# 3,andrzej,malczewski


file = open("0_data_types.py", "r")

txt = file.readline()

_ = file.__next__()
_ = file.__next__()
file.flush()
_ = file.__next__()
_ = file.__next__()
_ = file.__next__()

tst = file.__iter__()
file.close()

with open("0_data_types.py", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()


class FileWrapper:
    def __init__(self, *, suppress: bool = False):
        self.suppress = suppress

    def __enter__(self):
        return "DUPA"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if any((exc_type, exc_val, exc_tb)):
            print("Error present ")
            """False when you want to propagate exception stopping the program, True if you want to suppress"""
            return self.suppress
        print("doing something no matter if exception occured")


with FileWrapper(suppress=True) as var:
    print("inside context")
    raise KeyError("simulating error")

with FileWrapper(suppress=False) as var2:
    print("inside context")
    raise KeyError("simulating error")