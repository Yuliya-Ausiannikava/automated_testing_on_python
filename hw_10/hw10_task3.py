"""
This is the code to complete the "Counting the number of letters" task.
"""


def solution(text):
    """
    This function counts the number of each character in a string.
    :param text: string
    :return: string
    """

    letter = []
    count = 1

    for i, char in enumerate(text):
        if i < (len(text) - 1) and char == text[i + 1]:
            count += 1
        else:
            letter.append(char)
            if count > 1:
                letter.append(str(count))
            count = 1

    return ''.join(letter)


assert solution("cccbba") == "c3b2a"
assert solution("abeehhhhhccced") == "abe2h5c3ed"
assert solution("aaabbceedd") == "a3b2ce2d2"
assert solution("abcde") == "abcde"
assert solution("aaabbdefffff") == "a3b2def5"
