students = [
    {'name': 'Oleg', 'age': 18},
    {'name': 'Anna', 'age': 19},
    {'name': 'Ivan', 'age': 20}]


def get_names(students):
    result = []

    for student in students:
        result.append(student['name'])

    return result


def count_older_than_18(students):
    count = 0

    for student in students:
        if student['age'] > 18:
            count += 1

    return count



def get_names_older_than_18(students):
    result = []

    for student in students:
        if student['age'] > 18:
            result.append(student['name'])

    return result


def find_oldest_student(students):
    max_age = 0
    max_name = ''

    for student in students:
        if student['age'] > max_age:
            max_age = student['age']
            max_name = student['name']

    return  max_name, max_age


print('Names:', get_names(students))
print('Older than 18 count:',count_older_than_18(students))
print('Names older than 18:', get_names_older_than_18(students))
print('Oldest student:',find_oldest_student(students))