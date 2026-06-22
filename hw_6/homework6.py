"""
Этот файл содержит код, который выполняет все пункты домашней работы №6
"""

# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
S1 = 'www.my_site.com#about'
print(S1.replace('#', '/'))
print('=======================')

# Напишите программу, которая добавляет ‘ing’ к словам
A = 'run'
B = 'work'
C = 'sing'
D = 'ing'
print(A+D+',', B+D+',', C+D)
print('========================')

# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
NAME = 'Ivanou Ivan'
N1 = NAME.split()
# print(n1)
N2 = N1[::-1]
print(' '.join(N2))
print('========================')

# Напишите программу которая удаляет пробел в начале, в конце строки
NAME1 = ' My name is Yuliya '
print(NAME1.lstrip())
print(NAME1.rstrip())
print('========================')

# Исправьте "pARiS" >> "Paris"
CITY = 'pARiS'
print(CITY.capitalize())
print('========================')

# Перевести строку в список
STR1 = 'Robin Singh'
STR2 = 'I love arrays they are my favorite'
print(STR1.split())
print(STR2.split())
print('========================')

# Напечатайте текст: “Hello, Robin Singh! Welcome to airport”
LIST1 = ['Robin', 'Singh']
W = 'Welcome'
AIR = 'airport'
J1 = ' '.join(LIST1)
print(f'Hello {J1}! {W} to {AIR}')
print('========================')

# Сделать строку из списка
LIST2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
J2 = ' '.join(LIST2)
print(J2)
print('========================')

# Создайте список из 10 элементов и отредактировать
LIST3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LIST3[3] = 12
del LIST3[6]
print(LIST3)
