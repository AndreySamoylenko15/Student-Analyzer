import json

students = [
    {'name': 'Oleg', 'age': 18},
    {'name': 'Anna', 'age': 19},
    {'name': 'Ivan', 'age': 20}
]
def show_students():
    with open('students.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for student in data:
        print(student['name'], student['age'])



def add_student():
    with open('students.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    data.append({'name': name , 'age': age})

    with open('students.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def count_students():
    with open('students.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return len(data)


def find_oldest_student():
    with open('students.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    max_age = 0
    max_name = ''
    for student in data:
        if student['age'] > max_age:
            max_age = student['age']
            max_name = student['name']
    return max_name, max_age


choice=''


while choice!= '0':
    print('1 - Show students')
    print('2 - Add student')
    print('3 - Count students')
    print('4 - Find oldest student')
    print('0 - Exit')

    choice = input('Choose option: ')


    if choice == '1':
        show_students()
    elif choice == '2':
        add_student()
    elif choice == '0':
        print('Goodbye')
    elif choice == '3':
        print('Students count:', count_students())
    elif choice == '4':
        print('Oldest student:', find_oldest_student())
    else:
        print('Invalid choice')
