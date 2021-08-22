"""If conditionals explanation"""

if (x := 1) > 0:
    print(f"{x = }")

y = 1
if y > 0:
    print(f"{y = }")

# z = 1 > 0
if z := 1 > 0:
    print(f"{z = }")

lst = [1, 2, 3, 4, 5, 6]
if lst:
    print("list is present :)")
    print("do some list operation")


def tst(name: str = None):
    if not name:
        name = "John Doe"
    print(f"Your name is: {name}")


# tst()
# tst("dupa")


def tst2(lst1: list = [1, 2, 3, 4]):  # Anti Pattern example
    # if not lst1:
    #     lst1 = [1, 2, 3, 4]
    lst1.extend((5, 6, 7, 8))
    print(f"Your list is: {lst1}")
    return lst1


# var1 = tst2()
# var2 = tst2()


"""if else explanation"""

x = 1
if x > 0:
    print(f"{x = } is greater than 0")
else:
    print(f"{x = } is not greater than 0")

y = 0
if y > 0:
    print(f"{y = } is greater than 0")
elif y <= 0:
    print(f"{y = } is less or equal than 0")  # here it will stop
else:
    print(f"{y = } is not equal 0")

z = 0
if z > 0:
    print(f"{z = } is greater than 0")
if z < 0:
    print(f"{z = } is less than 0")  # will enter here
if z == 0:
    print(f"{z = } is equal 0")  # will enter here too


def if_example(a: int = 6):
    if a > 0:
        print(f"{a = } is greater from zero")

    if a < 7:
        print(f"{a = } is less then 7")

    if not (a % 2):
        print(f"{a = } is even")


if_example()


def elif_example(b: int = 6):
    if b > 0:
        print(f"{b = } is greater from zero")

    elif b < 7:
        print(f"{b = } is less then 7")

    elif not (b % 2):
        print(f"{b = } is even")


elif_example()


def if_example_upgraded(a: int = 6):
    if a > 0:
        print(f"{a = } is greater from zero")
        return None

    if a < 7:
        print(f"{a = } is less then 7")
        return None

    if not (a % 2):
        print(f"{a = } is even")
        return None


if_example_upgraded()


def junior_function(c: int = 6):
    if c > 0:
        if c < 10:
            if not (c % 2):
                print(f"{c = } greater than zero but less than 10 and is even")
            else:
                print(f"{c = } greater than zero but less than 10 and is not even")
        else:
            print(f"{c = } greater than zero and more than 10")
    else:
        print(f"{c = } greater less zero")


# junior_function()


def better_function(d: int = 6):
    if 0 < d < 10 and not (d % 2):
        print(f"{d = } is greater than 0")
        return None
    if d < 10 and not (d % 2):
        print(f"{d = } is less than 10")
        return None
    if not (d % 2):
        print(f"{d = } is even")
        return None
    return None


# better_function()

e = -1
if e > 0:
    print(f"{e = } is greater than 0")
else:
    print(f"{e = } is less than 0")


def some_function(f: int = 6):
    if f > 0:
        print(f"{f = } is greater than 0")
        return None
    print(f"{f = } is less than 0")
