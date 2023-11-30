"""
Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки (включіть фантазію). Наприклад вона
може містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.
"""
from abc import abstractmethod
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_DIR = Path(BASE_DIR, "task_02_files", "library.db")


class Person:
    def __init__(self, name):
        self.name = name


class User:
    @staticmethod
    def add_book_in_use(database, user_id, book_title):
        database.update_usage(1, user_id, book_title)

    @staticmethod
    def return_book_from_use(database, user_id, book_title):
        database.update_usage(0, user_id, book_title)


class Member(Person, User):
    def __init__(self, name):
        super().__init__(name)

    @abstractmethod
    def get_info(self):
        pass


class Teacher(Member):
    def __init__(self, name, science_sphere):
        super().__init__(name)
        self.science_sphere = science_sphere

    def get_info(self):
        print(f"Користувач: {self.name} є вчителем предмета: {self.science_sphere}")


class Student(Member):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def get_info(self):
        print(f"Користувач: {self.name} є студентом групи: {self.group}")


class Author(Person):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language


class Book:
    def __init__(self, title, author: Author):
        self.author = author
        self.title = title


class Shelf:
    def __init__(self):
        self.books_on_shelf = []

    def put_book_on_shelf(self, book: Book):
        self.books_on_shelf.append(book)


class Library:
    def __init__(self, path):
        self.database = Database(path)

    def receive_book_from_user(self, user_id, book_title):
        Member.return_book_from_use(self.database, user_id, book_title)
        user = self.database.get_user_by_id(user_id)
        print(f"Повернуто користувачем: {user[0]} книгу: {book_title}")

    def give_book_to_user(self, user_id, book_title):
        Member.add_book_in_use(self.database, user_id, book_title)
        user = self.database.get_user_by_id(user_id)
        print(f"Видано користувачу: {user[0]} книгу: {book_title}")

    def get_all_available_books(self):
        print("В бібліотеці доступні книги:")
        for book_data in self.database.get_all_books():
            if book_data[4] == 0:
                print(f"Книга: {book_data[1]}, автор: {book_data[2]}")

    def add_new_student(self, name, group_name):
        self.database.add_user(name, 1, group_name, None)

    def add_new_teacher(self, name, science_sphere):
        self.database.add_user(name, 2, None, science_sphere)

    def show_all_members(self):
        for member_data in self.database.get_all_users():
            member = None
            if member_data[2] == "Студент":
                member = Student(member_data[1], member_data[3])
            if member_data[2] == "Вчитель":
                member = Teacher(member_data[1], member_data[4])
            member.get_info()

    def get_book_by_title(self, book_title) -> Book:
        data = self.database.get_book_by_title(book_title)
        author = Author(data[1], data[2])
        return Book(book_title, author)

    def get_user_by_id(self, user_id) -> Member:
        data = self.database.get_user_by_id(user_id)
        return Member(data[0])

    def get_teacher_by_id(self, user_id) -> Teacher:
        data = self.database.get_teacher_by_id(user_id)
        return Teacher(data[0], data[1])

    def add_book(self, book_title, author_name, language):
        self.database.add_book(book_title, author_name, language)
        author = Author(author_name, language)
        return Book(book_title, author)


class Database:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)

    def get_user_by_id(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT username
            FROM users
            WHERE user_id=?
        ''', (user_id,))
        return cursor.fetchone()

    def get_teacher_by_id(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT username, science_sphere
            FROM users
            WHERE user_id=? and role_id=2
        ''', (user_id,))
        return cursor.fetchone()

    def get_book_by_title(self, book_title):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT book_title, author_name, language
            FROM books
            WHERE book_title=?
        ''', (book_title,))
        return cursor.fetchone()

    def add_user(self, username, role_id, group_name, science_sphere):
        cursor = self.connection.cursor()
        cursor.execute('''
                    INSERT INTO users (username, role_id, group_name, science_sphere) 
                    VALUES (?, ?, ?, ?) 
                ''', (username, role_id, group_name, science_sphere))
        self.connection.commit()

    def add_book(self, book_title, author_name, language):
        cursor = self.connection.cursor()
        cursor.execute('''
                    INSERT INTO books (book_title, author_name, language, is_in_use) 
                    VALUES (?, ?, ?, 0) 
                ''', (book_title, author_name, language))
        self.connection.commit()

    def get_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute('''
                    SELECT u.user_id, u.username, r.role_name, u.group_name, u.science_sphere
                    FROM users u
                    Join roles r ON u.role_id=r.role_id
                ''')
        return cursor.fetchall()

    def get_all_books(self):
        cursor = self.connection.cursor()
        cursor.execute('''
                    SELECT *
                    FROM books
                ''')
        return cursor.fetchall()

    def update_usage(self, is_in_use, user_id, book_title):
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE books
            SET is_in_use=?, user_id=?
            WHERE book_title=? 
        ''', (is_in_use, user_id, book_title))
        self.connection.commit()

    def initialize_db(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS roles
            (role_id INTEGER PRIMARY KEY AUTOINCREMENT,
            role_name TEXT UNIQUE)
                """)

        cursor.execute('''
            INSERT OR IGNORE INTO roles (role_name)
            VALUES ('Студент')
                ''')

        cursor.execute('''
            INSERT OR IGNORE INTO roles (role_name)
            VALUES ('Вчитель')
                        ''')

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users
            (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            role_id INTEGER,
            group_name TEXT,
            science_sphere TEXT,
            FOREIGN KEY (role_id) REFERENCES roles(role_id))
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books
            (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_title TEXT UNIQUE,
            author_name TEXT,
            language TEXT,
            is_in_use INTEGER,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(user_id))
                """)
        self.connection.commit()

    def close_db(self):
        self.connection.close()


class UserInterface:
    def __init__(self, path):
        self.library = Library(path)

    def start(self):
        self.library.database.initialize_db()

        while True:
            action_code = input("Введіть дію:\n   "
                                "1. Показати всі доступні в бібліотеці книги\n   "
                                "2. Показати всіх користувачів бібліотеки\n   "
                                "3. Додати нового користувача бібліотеки\n   "
                                "4. Додати нову книгу в бібліотеку\n   "
                                "5. Видати книгу користувачу\n   "
                                "6. Прийняти повернуту книгу у користувача\n   "
                                "7. Вихід\n")
            if action_code == "1":
                self.library.get_all_available_books()
            elif action_code == "2":
                self.library.show_all_members()
            elif action_code == "3":
                self.add_new_user()
            elif action_code == "4":
                self.add_new_book()
            elif action_code == "5":
                self.give_book_to_user()
            elif action_code == "6":
                self.receive_book_from_user()
            elif action_code == "7":
                print("До побачення")
                self.library.database.close_db()
                return
            else:
                print("Неправильно введений код дії, спробуйте ще")

    def add_new_user(self):
        while True:
            action_code = input("Введіть дію:\n   "
                                "1. Додати нового користувача вчителя\n   "
                                "2. Додати нового користувача студента\n   "
                                "3. Назад в головне меню\n")
            if action_code == "1":
                name = input("Введіть ім'я вчителя: ")
                science_sphere = input("Введіть предмет викладання вчителя: ")
                self.library.add_new_teacher(name, science_sphere)
                return
            elif action_code == "2":
                name = input("Введіть ім'я студента: ")
                group = input("Введіть групу студента: ")
                self.library.add_new_student(name, group)
                return
            elif action_code == "3":
                return
            else:
                print("Неправильно введений код дії, спробуйте ще")

    def add_new_book(self):
        author_name = input("Введіть ім'я автора: ")
        title = input("Введіть назву книги: ")
        language = input("Введіть мову книги: ")
        self.library.add_book(title, author_name, language)

    def give_book_to_user(self):
        title = input("Введіть назву книги: ")
        book = self.library.get_book_by_title(title)
        if book is None:
            print("Книги з даною назвою не існує")
            return
        user_id = input("Введіть ID користувача: ")
        member = self.library.get_user_by_id(user_id)
        if member is None:
            print("Користувача з таким ID не існує")
            return
        self.library.give_book_to_user(user_id, title)

    def receive_book_from_user(self):
        title = input("Введіть назву книги: ")
        book = self.library.get_book_by_title(title)
        if book is None:
            print("Книги з даною назвою не існує")
            return
        user_id = input("Введіть ID користувача: ")
        member = self.library.get_user_by_id(user_id)
        if member is None:
            print("Користувача з таким ID не існує")
            return
        self.library.receive_book_from_user(user_id, title)


UserInterface(DB_DIR).start()
