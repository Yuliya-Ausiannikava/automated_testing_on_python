"""
This is the code to complete the "Candles" task.
"""


def solution(candle_number, make_new):
    """
    This function calculates how many new candles can be made from the remains of burnt ones.
    :param candle_number: integer candle number
    :param make_new: integer candle number
    :return: integer total
    """
    candle_residue = candle_number
    total = candle_number
    while candle_residue >= make_new:
        candle_residue = candle_residue - make_new
        total = total + 1
        candle_residue = candle_residue + 1
    return total


assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2
