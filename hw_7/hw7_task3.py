"""
This code solves the third task from homework #7 "Time converter"
"""

time = input('Write what time it is on your watch now in format HH:MM - ')
hour = int(time[0:2])
minute = time[3:5]
if 1 <= hour <= 11:
    print(f"{hour}:{minute} a.m.")
elif 12 <= hour <= 23:
    print(f"{hour - 12}:{minute} p.m.")
elif hour == 00:
    print(f"12:{minute} p.m.")
