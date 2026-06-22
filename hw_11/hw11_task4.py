"""
Created a decorator for the caching function
"""


def cache(func):
    res_memories = {}

    def wrapper(*args):
        if args in res_memories:
            print("The result is already in the dictionary")
            return res_memories[args]
        else:
            print("I'm calculating")
            result = func(*args)
            res_memories[args] = result
            return result
    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
