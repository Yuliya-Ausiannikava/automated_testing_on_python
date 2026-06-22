"""
This code created a file with a list of students,
counted their number in each group and the average score for the group.
"""


with open('students.txt', 'w', encoding='utf-8') as file:
    file.write('name: Ivan, group number: 1, grade: 7\n')
    file.write('name: Irina, group number: 2, grade: 9\n')
    file.write('name: Mariya, group number: 2, grade: 7\n')
    file.write('name: Egor, group number: 3, grade: 8\n')
    file.write('name: Misha, group number: 1, grade: 10\n')
    file.write('name: Elena, group number: 3, grade: 7\n')
    file.write('name: Katya, group number: 2, grade: 5')

try:
    with open('students.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('File not found')


# Total number of students
def count_students_in_group(stud_file):
    count_student = 0
    for line in stud_file:
        if not line:
            continue
        count_student += 1
    return count_student


with open('students.txt', 'r', encoding='utf-8') as file:
    TOTAL_STUDENTS = count_students_in_group(file)


# Number of students in each group and average score for the group
def students_data(stud_file):
    count_students_in_group_1 = 0
    count_students_in_group_2 = 0
    count_students_in_group_3 = 0
    grade_students_1 = 0
    grade_students_2 = 0
    grade_students_3 = 0

    for line in stud_file:
        line = line.strip()
        format_line = line.split(', ')
        group_number = format_line[1].split(': ')[1]
        try:
            grade = int(format_line[2].split(': ')[1])
        except ValueError:
            print('Invalid grade. It is not a number.')
        if group_number == '1':
            count_students_in_group_1 += 1
            grade_students_1 += grade
        elif group_number == '2':
            count_students_in_group_2 += 1
            grade_students_2 += grade
        elif group_number == '3':
            count_students_in_group_3 += 1
            grade_students_3 += grade
    try:
        average_group_rating_1 = round(grade_students_1 / count_students_in_group_1, 1)
        average_group_rating_2 = round(grade_students_2 / count_students_in_group_2, 1)
        average_group_rating_3 = round(grade_students_3 / count_students_in_group_3, 1)
    except ZeroDivisionError:
        print('Division by zero is impossible.')

    return {
        "Group_1": {"count_in_group_1": count_students_in_group_1,
                    "average_rating_1": average_group_rating_1},
        "Group_2": {"count_in_group_2": count_students_in_group_2,
                    "average_rating_2": average_group_rating_2},
        "Group_3": {"count_in_group_3": count_students_in_group_3,
                    "average_rating_3": average_group_rating_3}
    }


with open('students.txt', 'r', encoding='utf-8') as file:
    students = students_data(file)


with open('students.txt', 'a', encoding='utf-8') as file:
    file.write('\nInformation about student groups:\n')
    file.write(f'Total number of students: {TOTAL_STUDENTS}\n')
    file.write(f'Total number of students in group 1: {students["Group_1"]["count_in_group_1"]}\n')
    file.write(f'Average rating in group 1: {students["Group_1"]["average_rating_1"]}\n')
    file.write(f'Total number of students in group 2: {students["Group_2"]["count_in_group_2"]}\n')
    file.write(f'Average rating in group 2: {students["Group_2"]["average_rating_2"]}\n')
    file.write(f'Total number of students in group 3: {students["Group_3"]["count_in_group_3"]}\n')
    file.write(f'Average rating in group 3: {students["Group_3"]["average_rating_3"]}\n')
