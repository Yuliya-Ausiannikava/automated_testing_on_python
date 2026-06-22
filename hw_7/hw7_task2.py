"""
This code solves the second task from homework #7 "Level Up"
"""

XP = float(input('Write the number of experience points before killing the monster?:'))
reward = float(input('How much experience did you get as a reward for killing a monster?:'))
THERESHOLD = 15
total = XP + reward
if total >= THERESHOLD:
    print(True)
if total < THERESHOLD:
    print(False)
