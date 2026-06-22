"""
A decorator is created that checks if the result of a function is a number
"""


def res_number(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            print("Error. The result of a function can only be a number.")
            raise ValueError(...)
        return result
    return wrapper


@res_number
def my_func(arg1, arg2):
    return arg1 + arg2


print(my_func('10', '2.5'))
