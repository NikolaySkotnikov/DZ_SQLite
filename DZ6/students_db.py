import sqlite3


def connection_db(func):
    def wrapper(self, *args, **kwargs):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        result = func(self, *args, **kwargs)
        self.connection.close()
        return result
    return wrapper


class StudentDataBase:
    def __init__(self, db_name='students.db'):
        self.db_name = db_name
        self.create_table()

    @connection_db
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                surname TEXT,
                age INTEGER,
                group_student TEXT)''')

    @connection_db
    def add_student(self, name, surname, age, groups):
        self.cursor.executescript(f'''
            INSERT INTO students (name, surname, age, group_student)
            VALUES ('{name}', '{surname}', {age}, '{groups}')''')

    @connection_db
    def show_students(self):
        self.cursor.execute('''
            SELECT * FROM students''')
        students = self.cursor.fetchall()
        for student in students:
            print(student)
