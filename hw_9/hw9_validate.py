"""
This is the code to complete the "Validate" task.
"""


def solution(number):
    """
    This function checks the validity of credit card numbers.
    :param number: int or str
    :return: boolean
    """

    # We are running checks on the correctness of the entered data
    if not number:
        return False

    if isinstance(number, int):
        numb_str = str(number)
    elif isinstance(number, str):
        numb_str = number
    else:
        return False

    if not numb_str.isdigit():
        if numb_str.startswith('-'):
            return False
        return False

    # Luhn's algorithm
    card_numb = list(map(int, numb_str))
    for i in reversed(range(len(card_numb))):
        if (len(card_numb) - i) % 2 == 0:
            dob = card_numb[i] * 2
            if dob > 9:
                card_numb[i] = dob - 9
            else:
                card_numb[i] = dob

    return sum(card_numb) % 10 == 0


assert solution(4561261212345464) is False
assert solution(4111111111111111) is True
assert solution(4222222222222) is True
assert solution(-42222222222222) is False
assert solution('') is False
assert solution('abcde') is False
