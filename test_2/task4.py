def arr_number(arr):
    """
    The function adds one to a number and returns a list
    :param arr: list of numbers
    :return: list of numbers
    """
    result = arr[::-1]
    for i in range(len(result)):  # pylint: disable=consider-using-enumerate
        if result[i] == 9:
            result[i] = 0
        else:
            result[i] += 1
            return result[::-1]
    return [1] + result[::-1]


array = arr_number([1, 2, 3])
array1 = arr_number([9, 9, 9])
print(array)
print(array1)
