class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # getter - wyciaga wartosc pola
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


tst = Animal("dupa", 1)

# class First(h,j,k):
#     def test(self):
#         print("test")
#
#
# class Second(First, a, b, c):
#     def printer(self):
#         print("printer")
#
# tst2 = Second()


gen = range(10).__iter__()
gen.__next__()
gen.__next__()
gen.__next__()
for item in gen:
    print(f"{item = }")


class Animal:
    def __init__(self, name="Rex", age=2):
        self.__name = name
        self.__age = age


my_dog = Animal()
# print(my_dog.__name)
