from students_db import StudentDataBase


if __name__ == '__main__':
    while True:
        db = StudentDataBase()
        command = input('1. Показать всех студентов\n'
                        '2. Добавить студента\n'
                        '3. Выход\n')

        match command:
            case '1':
                db.show_students()
            case '2':
                name = input('Введите Имя студента: ')
                surname = input('Введите Фамилию студента: ')
                age = int(input('Введите возраст студента: '))
                group = input('Введите группу студента: ')
                db.add_student(name, surname, age, group)
            case '3':
                break
