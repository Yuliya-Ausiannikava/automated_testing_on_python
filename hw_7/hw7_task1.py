"""
This code solves the second task from homework #7 "Time"
"""

n = int(input("Write how many minutes the motorcycle timer shows:"))
hour = (n // 60) % 24
minutes = n % 60

if hour < 10 and minutes < 10:
    S = f'0{hour}:0{minutes}'
    print(S)
    TOTAL = int(S[0]) + int(S[1]) + int(S[3]) + int(S[4])
    print(TOTAL)
elif minutes < 10 <= hour:
    S = f'{hour}:0{minutes}'
    print(S)
    TOTAL = int(S[0]) + int(S[1]) + int(S[3]) + int(S[4])
    print(TOTAL)
elif minutes >= 10 > hour:
    S = f'0{hour}:{minutes}'
    print(S)
    TOTAL = int(S[0]) + int(S[1]) + int(S[3]) + int(S[4])
    print(TOTAL)
elif hour >= 10 and minutes >= 10:
    S = f'{hour}:{minutes}'
    print(S)
    TOTAL = int(S[0]) + int(S[1]) + int(S[3]) + int(S[4])
    print(TOTAL)
