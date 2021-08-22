CONSTANT = 1  # constant variables declared at top of file with capital letters
var = 1  # normal variable with lower case letters
long_var = 1  # snake case for multiple part variables
input_ = 1  # single trailing underscore for avoiding collisions with built-in functions


class SomeClass:  # Camel case for class naming
    _private = 1  # leading underscore means developer meant variable should be "private"
    __name_tangling = 1  # will add '_' + 'SomeClass' to our variable name. This process is called name tangling

    def __str__(self):  # "DUNDER" > double underscore. Those are magic methods used in python
        pass


obj = SomeClass()
