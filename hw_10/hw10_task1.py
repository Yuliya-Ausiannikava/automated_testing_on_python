"""
This is the code to complete the "Strings with a given character" task.
"""


def solution(text):
    """
    This function removes the previous character from the string when it finds "#"
    :param text: string text
    :return: string text_list
    """

    text_list = []
    for el in text:
        if el != "#":
            text_list.append(el)
        elif el == "#":
            if len(text_list) > 0:
                text_list.pop()
    return "".join(text_list)


assert solution("a#bc#d") == "bd"
assert solution("abc#d##c") == "ac"
assert solution("abc##d######") == ""
assert solution("#######") == ""
assert solution("") == ""
