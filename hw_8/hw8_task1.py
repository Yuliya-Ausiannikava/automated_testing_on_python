"""
This code solves the second task from homework #7 "Bulls and cows"
"""

import random

while True:
    NUMBER = str(random.randint(1000, 9999))
    if len(set(NUMBER)) == 4:
        break

while True:
    GUESS = str(input('The number has been chosen. Try to guess it: '))
    if len(set(GUESS)) != 4 or not GUESS.isdigit() or len(GUESS) != 4:
        print('Please, enter a 4-digit number without repeating digits:')
        continue

    BULLS = 0
    COWS = 0
    for i, char in enumerate(GUESS):
        if char == NUMBER[i]:
            BULLS += 1
        elif char in NUMBER and char != NUMBER[i]:
            COWS += 1

    print(f'Bulles: {BULLS},cows: {COWS}')

    if BULLS == 4:
        print('You win!')
        break
