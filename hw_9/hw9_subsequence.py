"""
This is the code to complete the "Sequence" task.
"""


def solution(sequence):

    def check_increasing(arr):
        """
        This function checks if the numbers are increasing.
        arg list: list of numbers
        return: boolean
        """

        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True

    # Checking a list after excluding one element
    for item in range(len(sequence) - 1):
        if sequence[item] >= sequence[item + 1]:
            rm_item = sequence[:item] + sequence[item + 1:]
            rm_next = sequence[:item + 1] + sequence[item + 2:]

            # Checking for increment after deleting an element
            if check_increasing(rm_next) or check_increasing(rm_item):
                return True
            return False
    return True


assert solution([1, 2, 3]) is True
assert solution([1, 2, 1, 2]) is False
assert solution([1, 3, 2, 1]) is False
assert solution([1, 2, 3, 4, 5, 3, 5, 6]) is False
assert solution([40, 50, 60, 10, 20, 30]) is False
