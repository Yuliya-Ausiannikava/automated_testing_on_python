# The function calculates the sum of all numbers up to a given value
def total(x):
    result = 0
    for i in range(0, x + 1):
        result += i
    return result


res = total(5)
print(res)
