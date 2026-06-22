def string(s, x):
    """
    The function converts a string
    :param s: str
    :param x: int
    :return: str
    """
    if x == 1:
        return s[:1]
    return s[:x] + s[x - 2::-1]


MY_STRING = 'abcdefghijklmnopqrstuvwxyz'
assert string(MY_STRING, 1) == 'a'
assert string(MY_STRING, 2) == 'aba'
