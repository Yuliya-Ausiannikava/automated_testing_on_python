"""
A decorator has been written that checks whether the function arguments are positive numbers
"""


def validate_arguments(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("The argument must be of type integer or float")
            if arg < 0:
                raise ValueError("The argument must be a positive number")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError("The argument value must be of type integer or float")
            if value < 0:
                raise ValueError(f"The argument {key} must be a positive number")
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def my_function(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


print(my_function(1, 3.5, arg3=10))
