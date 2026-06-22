"""
This code solves the second task from homework #8 "Infinity loop"
"""

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

if a == b:
    print(False)
else:
    while a != b:
        a += 1
        b -= 1
        if a == b:
            print(False)
            break
        if a > b:
            print(True)
            break
