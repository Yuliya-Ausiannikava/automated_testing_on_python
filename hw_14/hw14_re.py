"""
Programs that work using regular expressions.
"""

import re


# Finds all dates in the text in the format "dd.mm.yyyy"
def find_date(file):
    for line in file:
        dt = re.findall(r'\d{2}.\d{2}.\d{4}', line)
        dt_str = ', '.join(dt)
        return print(dt_str)


with open('hw14_text.txt', 'r', encoding='utf-8') as text_file:
    find_date(text_file)
print('________________________________________________________________')


# Checks the correctness of passwords
def validate_password(password):
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$')
    if re.search(pattern, password):
        return print('Password is valid')
    else:
        return print('The password must be at least 8 characters long '
                     'and contain at least one uppercase letter, '
                     'one lowercase letter, and one number.')


validate_password("Afjkf7758")
print('________________________________________________________________')

# Corrects repetitions of words in the text
MESSAGE = ('Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. '
           'Смешно, не не правда ли? Не нужно портить хор хоровод.')
PATTERN = r'\b(\w+)\s+\1\b'
corrected_message = re.sub(PATTERN, r'\1', MESSAGE, flags=re.IGNORECASE)
print(corrected_message)
