"""
This code solves the second task from homework #8 "Statues"
"""

size_1 = [3, 1, 8, 5, 10]
size_2 = []

for i in range(0, max(size_1)):
    i += 1
    if i not in size_1:
        size_2.append(i)
print(len(size_2))
