"""
This is the code to complete the "Number opposite" task.
"""


def solution(n, f_number):

    """
    This function, given n and first_number, finds the number
    that is written in the radially opposite position from first_number.
    :arg n: integer n
    :arg f_number: integer f_number
    :return: integer opposite position from first_number
    """
    if n >= 0 and n % 2 == 0:
        return (f_number + n // 2) % n
    else:
        return print("Error. n must be even and positive")


assert solution(10, 6) == 1
assert solution(10, 2) == 7
assert solution(10, 4) == 9
