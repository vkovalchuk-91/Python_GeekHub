"""
Банкомат 2.0: переробіть программу з функціонального підходу програмування на використання класів. Додайте шанс 10%
отримати бонус на баланс при створенні нового користувача.
"""
from datetime import datetime
import sqlite3
from pathlib import Path
import random

BASE_DIR = Path(__file__).parent
DB_DIR = Path(BASE_DIR, "task_03_files", "ATM.db")
BONUS_RANDOMIZER_PERCENT = 10
BONUS_AMOUNT_PERCENT = 10


class ATM:
    def __init__(self, path):
        self.database = Database(path)

    def start(self):
        self.database.initialize_db()
        while True:
            action_code = input("Введіть дію:\n   1. Увійти в систему\n   2. Зареєструвати нового користувача\n   3. "
                                "Вихід\n")
            if action_code == "1":
                if self.get_login():
                    self.database.close_db()
                    return
            elif action_code == "2":
                self.register_new_user()
            elif action_code == "3":
                print("До побачення")
                self.database.close_db()
                return
            else:
                print("Неправильно введений код дії, спробуйте ще")

    def get_login(self):
        login = input("Введіть логін користувача: ")
        password = input("Введіть пароль користувача: ")

        if self.check_credentials(login, password):
            self.start_menu_actions(login)
            return True
        else:
            print("Неправильно введено логін/пароль")
            return False

    def check_credentials(self, login, password):
        if self.database.get_user_by_login_and_password(login, password) is None:
            return False
        return True

    def start_menu_actions(self, login):
        is_cash_collector = self.is_user_cash_collector(login)
        while True:
            if is_cash_collector:
                action_code = input(
                    "Введіть дію:\n   1. Продивитись баланс\n   2. Поповнити баланс\n   3. Зняти кошти\n   4. "
                    "Вихід\n   5. Продивитись баланс банкомату\n   6. Змінити баланс банкомату\n")
            else:
                action_code = input(
                    "Введіть дію:\n   1. Продивитись баланс\n   2. Поповнити баланс\n   3. Зняти кошти\n  "
                    " 4. Вихід\n")
            if action_code == "1":
                print(f"Поточний баланс користувача {login}: {self.get_user_balance_sum(login)}")
            elif action_code == "2":
                self.top_up_balance_action(login)
            elif action_code == "3":
                self.withdraw_money_action(login)
            elif action_code == "4":
                print("До побачення")
                return
            elif is_cash_collector and action_code == "5":
                self.print_atm_banknote_balance()
            elif is_cash_collector and action_code == "6":
                self.change_atm_balance_action()
            else:
                print("Неправильно введений код дії, спробуйте ще")

    def is_user_cash_collector(self, login):
        return self.database.get_is_cash_collector_by_login(login)[0]

    def get_user_balance_sum(self, login):
        balance_sql_response = self.database.get_user_balance_by_login(login)
        if balance_sql_response is None:
            balance = 0
            self.insert_initial_balance_sum(login, 0)
        else:
            balance = balance_sql_response[0]
        return balance

    def insert_initial_balance_sum(self, login, balance_sum):
        user_id = self.database.get_user_id_by_login(login)[0]
        self.database.insert_new_users_balance_sum(user_id, balance_sum)

    def top_up_balance_action(self, login):
        deposit_sum = input("Введіть суму на яку бажаєте поповнити баланс: ")
        if self.is_valid_sum(deposit_sum):
            deposit_sum_float = float(deposit_sum)
            if deposit_sum_float % 10 != 0:
                deposit_sum_float -= deposit_sum_float % 10
                print(f"Баланс поповнено на {deposit_sum_float} грн, повернуто здачею {float(deposit_sum) % 10} грн")
            else:
                print(f"Баланс поповнено на {deposit_sum} грн")
            if self.is_first_transaction_with_bonus(login):
                deposit_sum_with_bonus = round(deposit_sum_float * (1 + BONUS_AMOUNT_PERCENT / 100), 2)
                print(f"Додатково баланс поповнено на суму бонуса: {deposit_sum_with_bonus - deposit_sum_float} грн")
                deposit_sum_float = deposit_sum_with_bonus
            balance_before = self.get_user_balance_sum(login)
            balance_after = balance_before + deposit_sum_float
            self.add_transaction(login, deposit_sum_float, "top_up_balance")
            self.update_balance_sum(login, balance_after)
        else:
            print("Ви ввели некоректне значення суми поповнення балансу")

    @staticmethod
    def is_valid_sum(sum_string):
        try:
            sum_float = float(sum_string)
            if sum_float > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def withdraw_money_action(self, login):
        withdraw_sum = input("Введіть суму грошей, яку бажаєте зняти з рахунку: ")
        if self.is_valid_sum(withdraw_sum):
            if float(withdraw_sum) > self.get_atm_balance_sum():
                print("Недостатньо коштів в банкоматі для зняття даної суми")
            else:
                balance_before = self.get_user_balance_sum(login)
                balance_after = balance_before - float(withdraw_sum)
                if balance_after < 0:
                    print("На рахунку недостатньо коштів для зняття даної суми")
                else:
                    self.update_balance_sum(login, balance_after)
                    self.add_transaction(login, withdraw_sum, "withdraw_money")
                    print(f"З рахунку знято {withdraw_sum} грн")
        else:
            print("Ви ввели некоректне значення суми для зняття з рахунку")

    def update_balance_sum(self, login, balance_sum):
        user_id = self.database.get_user_id_by_login(login)[0]
        self.database.update_users_balance_sum(user_id, balance_sum)

    def add_transaction(self, login, operation_sum, operation_name):
        user_id = self.database.get_user_id_by_login(login)[0]
        operation_id = self.database.get_operation_id_by_operation_name(operation_name)[0]
        self.database.insert_transaction(user_id, operation_id, operation_sum)

    def get_atm_balance_sum(self):
        balance_data_sql_response = self.database.get_atm_balance()
        balance = 0
        if balance_data_sql_response is not None:
            for banknote_quantity in balance_data_sql_response:
                balance += banknote_quantity[0] * banknote_quantity[1]
        return balance

    def print_atm_banknote_balance(self):
        print("Залишок купюр в банкоматі:")
        for banknote_quantity in self.database.get_atm_balance():
            print(f"Банкнот номіналом {banknote_quantity[0]} грн - {banknote_quantity[1]} од.")
        print(f"Всього поточний залишок: {self.get_atm_balance_sum()} грн")

    def change_atm_balance_action(self):
        banknote_nominal = input(
            "Введіть номінал банкноти, кількість яких ви хочете змінити (доступні купюри 10, 20, 50, "
            "100, 200, 500, 1000 грн): ")
        if banknote_nominal in ("10", "20", "50", "100", "200", "500", "1000"):
            banknote_amount = input(f"Введіть кількість банкнот номіналом {banknote_nominal} грн, що буде в банкоматі "
                                    f"після  даної операції: ")
            if self.is_valid_amount(banknote_amount):
                self.database.update_atm_banknote_balance(banknote_nominal, banknote_amount)
            else:
                print("Ви ввели некоректне значення кількості банкнот банкомату")
        else:
            print("Введеного вами номіналу не існує")

    @staticmethod
    def is_valid_amount(amount_string):
        try:
            amount_int = int(amount_string)
            if amount_int >= 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def register_new_user(self):
        print("Зверніть увагу логін та пароль мають бути не менше 5 символів!")
        login = input("Введіть логін нового користувача: ")
        if self.check_login_existing(login):
            print("Помилка, введений логін вже існує")
            return

        password = input("Введіть пароль нового користувача: ")
        if self.check_registration_validation(login, password):
            print("Помилка, логін та пароль мають бути не менше 5 символів")
        else:
            self.database.insert_new_user_to_db(login, password)
            print("Користувача успішно зареєстровано")
            if self.receive_bonus():
                self.database.insert_registration_bonus(login)
                print("Вітаю, ви отримаєте бонус додаткових 10% при першому поповненні")

    def check_login_existing(self, login):
        if self.database.get_existing_login(login) is None:
            return False
        return True

    @staticmethod
    def check_registration_validation(login, password):
        if len(login) < 5 or len(password) < 5:
            return True
        return False

    @staticmethod
    def receive_bonus():
        return random.random() < BONUS_RANDOMIZER_PERCENT / 100

    def is_first_transaction_with_bonus(self, login):
        return (self.database.get_top_up_transactions_count_by_login(login)[0] == 0 and
                self.database.get_first_transaction_bonus(login)[0])


class Database:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)

    def get_user_by_login_and_password(self, login, password):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT * 
            FROM users
            WHERE login=? AND password=?
        ''', (login, password))
        return cursor.fetchone()

    def get_existing_login(self, login):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT login 
            FROM users
            WHERE login=?
        ''', (login,))
        return cursor.fetchone()

    def insert_new_user_to_db(self, login, password):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO users (login, password, is_cash_collector) 
            VALUES (?, ?, 0) 
        ''', (login, password))
        self.connection.commit()

    def get_is_cash_collector_by_login(self, login):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT is_cash_collector 
            FROM users
            WHERE login=?
        ''', (login,))
        return cursor.fetchone()

    def get_user_balance_by_login(self, login):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT ub.user_balance 
            FROM user_balance ub
            JOIN users u ON ub.user_id=u.user_id
            WHERE u.login=?
        ''', (login,))
        return cursor.fetchone()

    def get_user_id_by_login(self, login):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT user_id 
            FROM users
            WHERE login=?
        ''', (login,))
        return cursor.fetchone()

    def insert_new_users_balance_sum(self, user_id, balance_sum):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO user_balance (user_id, user_balance, last_update) 
            VALUES (?, ?, ?) 
        ''', (user_id, balance_sum, datetime.now()))
        self.connection.commit()

    def update_users_balance_sum(self, user_id, balance_sum):
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE user_balance
            SET user_balance=?, last_update=?
            WHERE user_id=?
        ''', (balance_sum, datetime.now(), user_id))
        self.connection.commit()

    def get_operation_id_by_operation_name(self, operation_name):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT operation_id 
            FROM operations
            WHERE operation_name=?
        ''', (operation_name,))
        return cursor.fetchone()

    def insert_transaction(self, user_id, operation_id, operation_sum):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO transactions (user_id, operation_id, transaction_amount) 
            VALUES (?, ?, ?) 
        ''', (user_id, operation_id, operation_sum))
        self.connection.commit()

    def get_atm_balance(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT *
            FROM atm_balance
        ''')
        return cursor.fetchall()

    def update_atm_banknote_balance(self, banknote_nominal, banknote_amount):
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE atm_balance
            SET banknote_amount=?
            WHERE banknote_nominal=?
        ''', (banknote_amount, banknote_nominal))
        self.connection.commit()

    def insert_registration_bonus(self, login):
        cursor = self.connection.cursor()
        cursor.execute('''
                    UPDATE users
                    SET first_transaction_bonus=?
                    WHERE login=?
                ''', (1, login))
        self.connection.commit()

    def initialize_db(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users
            (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE,
            password TEXT,
            is_cash_collector INTEGER)
        """)

        cursor.execute('''
            INSERT OR IGNORE INTO users (login, password, is_cash_collector) 
            VALUES ('admin', 'admin', 1) 
        ''')

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_balance
            (balance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            user_balance REAL,
            last_update DATETIME,
            FOREIGN KEY (user_id) REFERENCES users(user_id))
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS operations
            (operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation_name TEXT UNIQUE)
        """)

        cursor.execute('''
            INSERT OR IGNORE INTO operations (operation_name) 
            VALUES ('top_up_balance') 
        ''')

        cursor.execute('''
            INSERT OR IGNORE INTO operations (operation_name) 
            VALUES ('withdraw_money') 
        ''')

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions
            (transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            operation_id INTEGER,
            transaction_amount INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (operation_id) REFERENCES operations(operation_id))
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS atm_balance
            (banknote_nominal INTEGER PRIMARY KEY,
            banknote_amount INTEGER)
        """)

        cursor.execute('''
            INSERT OR IGNORE INTO atm_balance (banknote_nominal, banknote_amount) 
            VALUES (10, 20) 
        ''')

        cursor.execute('''
            INSERT OR IGNORE INTO atm_balance (banknote_nominal, banknote_amount) 
            VALUES (20, 20) 
        ''')

        cursor.execute('''
            INSERT OR IGNORE INTO atm_balance (banknote_nominal, banknote_amount) 
            VALUES (50, 20) 
        ''')

        cursor.execute('''
            INSERT OR IGNORE INTO atm_balance (banknote_nominal, banknote_amount) 
            VALUES (100, 20) 
        ''')

        cursor.execute('''
            INSERT OR IGNORE INTO atm_balance (banknote_nominal, banknote_amount) 
            VALUES (200, 20) 
        ''')

        cursor.execute('''
            INSERT OR IGNORE INTO atm_balance (banknote_nominal, banknote_amount) 
            VALUES (500, 20) 
        ''')

        cursor.execute('''
            INSERT OR IGNORE INTO atm_balance (banknote_nominal, banknote_amount) 
            VALUES (1000, 20) 
        ''')

    def close_db(self):
        self.connection.close()

    def get_top_up_transactions_count_by_login(self, login):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT count(*)
            FROM transactions t
            JOIN users u ON u.user_id=t.user_id AND u.login=? AND operation_id=1
        ''', (login,))
        return cursor.fetchone()

    def get_first_transaction_bonus(self, login):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT first_transaction_bonus 
            FROM users
            WHERE login=?
        ''', (login,))
        return cursor.fetchone()


ATM(DB_DIR).start()
