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
if z <= 0:
    print(f"{z = } is less or equal than 0")  # will enter here
if z == 0:
    print(f"{z = } is not equal 0")  # will enter here too


def if_example(a: int = 6):
    if a > 0:
        print(f"{a = } is greater from zero")

    if a < 7:
        print(f"{a = } is less then 7")

    if not (a % 2):
        print(f"{a = } is even")


if_example()
