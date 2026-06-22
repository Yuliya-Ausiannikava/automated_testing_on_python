def read_file(filename):
    """
    The function reads a file, counts lines, words, and letters,
    and appends the information to the end of the file.
    :param filename: file name
    :return: string content, count_lines, count_words, count_letters
    """
    with open(filename, 'r', encoding='utf-8') as my_file:
        content = my_file.readlines()
        print(content)
        count_lines = 0
        count_words = 0
        count_letters = 0
        for line in content:
            count_lines += 1
            for word in line.split():
                count_words += 1
                for letter in word:
                    if letter.isalpha():
                        count_letters += 1
    print(f'Number of lines: {count_lines}, word count: {count_words}, '
          f'number of letters: {count_letters}')

    with open(filename, 'a', encoding='utf-8') as f:
        f.write("\nIn total, this file contains:\n")
        f.write(f"Number of lines: {count_lines}\n")
        f.write(f"word count: {count_words}\n")
        f.write(f"number of letters: {count_letters}\n")

    return count_lines, count_words, count_letters


def write_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)


write_file('../hw_14/test_text.txt', 'Вирджиния Вулф «На маяк»''\nДжеймс Джойс «Улисс»'
           + '\nВладимир Набоков «Лолита»''\nУильям Фолкнер «Звук и ярость»'
           + '\nЛев Толстой «Война и мир»')


read_file('../hw_14/test_text.txt')
