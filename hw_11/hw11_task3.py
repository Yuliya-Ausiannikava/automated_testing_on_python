"""
A decorator has been created that converts the types of function arguments.
"""


def typed(type_):
    def wrapper(func):
        def inner(*args):
            convert = []
            for arg in args:
                if not isinstance(arg, type_):
                    arg = type_(arg)
                convert.append(arg)
            return func(*convert)
        return inner
    return wrapper


@typed(str)
def my_func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


print(my_func(3, '5', 1))
