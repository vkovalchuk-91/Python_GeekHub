"""
Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких файлів. Якщо в попередньому завданні ви добре
    продумали структуру програми то у вас не виникне проблем швидко адаптувати її до нових вимог.
    - на старті додати можливість залогінитися або створити новго користувача (при створенні новго користувача,
    перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
    - в таблиці (базі) з користувачами має бути створений унікальний користувач-інкасатор, який матиме розширені
    можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
    - банкомат має власний баланс
    - кількість купюр в банкоматі обмежена. Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
    - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
    - користувач через банкомат може покласти на рахунок лише сумму кратну мінімальному номіналу що підтримує банкомат.
    В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5). Але це не має впливати на
    баланс/кількість купюр банкомату, лише збільшуєтсья баланс користувача (моделюємо наявність двох незалежних касет в
    банкоматі - одна на прийом, інша на видачу)
    - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
    - при неможливості виконання якоїсь операції - вивести повідомлення з причиною (не вірний логін/пароль, недостатньо
    коштів на раунку, неможливо видати суму наявними купюрами тощо.)
"""
from datetime import datetime
import sqlite3
from pathlib import Path
BASE_DIR = Path(__file__).parent
DB_DIR = Path(BASE_DIR, "task_01_files", "ATM.db")


def start():
    connection = sqlite3.connect(DB_DIR)
    initialize_db(connection)
    while True:
        action_code = input("Введіть дію:\n   1. Увійти в систему\n   2. Зареєструвати нового користувача\n   3. "
                            "Вихід\n")
        if action_code == "1":
            if get_login(connection):
                connection.close()
                return
        elif action_code == "2":
            register_new_user(connection)
        elif action_code == "3":
            print("До побачення")
            connection.close()
            return
        else:
            print("Неправильно введений код дії, спробуйте ще")


def get_login(connection):
    login = input("Введіть логін користувача: ")
    password = input("Введіть пароль користувача: ")

    if check_credentials(login, password, connection):
        start_menu_actions(login, connection)
        return True
    else:
        print("Неправильно введено логін/пароль")
        return False


def check_credentials(login, password, connection):
    cursor = connection.cursor()
    cursor.execute('''
        SELECT * 
        FROM users
        WHERE login=? AND password=?
    ''', (login, password))
    user = cursor.fetchone()

    if user is None:
        return False
    return True


def register_new_user(connection):
    print("Зверніть увагу логін та пароль мають бути не менше 5 символів!")
    login = input("Введіть логін нового користувача: ")
    if check_login_existing(login, connection):
        print("Помилка, введений логін вже існує")
        return

    password = input("Введіть пароль нового користувача: ")
    if check_registration_validation(login, password):
        print("Помилка, логін та пароль мають бути не менше 5 символів")
    else:
        insert_new_user_to_db(login, password, connection)
        print("Користувача успішно зареєстровано")


def check_login_existing(login, connection):
    cursor = connection.cursor()
    cursor.execute('''
        SELECT login 
        FROM users
        WHERE login=?
    ''', (login,))
    user = cursor.fetchone()

    if user is None:
        return False
    return True


def check_registration_validation(login, password):
    if len(login) < 5 or len(password) < 5:
        return True
    return False


def insert_new_user_to_db(login, password, connection):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO users (login, password, is_cash_collector) 
        VALUES (?, ?, 0) 
    ''', (login, password))
    connection.commit()


def start_menu_actions(login, connection):
    while True:
        action_code = input("Введіть дію:\n   1. Продивитись баланс\n   2. Поповнити баланс\n   3. Зняти кошти\n   4. "
                            "Вихід\n")
        if action_code == "1":
            print(f"Поточний баланс користувача {login}: {get_balance_sum(login, connection)}")
        elif action_code == "2":
            top_up_balance_action(login, connection)
        elif action_code == "3":
            withdraw_money_action(login, connection)
        elif action_code == "4":
            print("До побачення")
            return
        else:
            print("Неправильно введений код дії, спробуйте ще")


def get_balance_sum(login, connection):
    cursor = connection.cursor()
    cursor.execute('''
        SELECT ub.user_balance 
        FROM user_balance ub
        JOIN users u ON ub.user_id=u.user_id
        WHERE u.login=?
    ''', (login,))
    result = cursor.fetchone()
    if result is None:
        balance = 0
        insert_initial_balance_sum(login, 0, connection)
    else:
        balance = result[0]
    return balance


def insert_initial_balance_sum(login, balance_sum, connection):
    cursor = connection.cursor()
    cursor.execute('''
        SELECT user_id 
        FROM users
        WHERE login=?
    ''', (login,))
    user_id = cursor.fetchone()[0]

    cursor.execute('''
        INSERT INTO user_balance (user_id, user_balance, last_update) 
        VALUES (?, ?, ?) 
    ''', (user_id, balance_sum, datetime.now()))
    connection.commit()


def update_balance_sum(login, balance_sum, connection):
    cursor = connection.cursor()
    cursor.execute('''
        SELECT user_id 
        FROM users
        WHERE login=?
    ''', (login,))
    user_id = cursor.fetchone()[0]

    cursor.execute('''
        UPDATE user_balance
        SET user_balance=?, last_update=?
        WHERE user_id=?
    ''', (balance_sum, datetime.now(), user_id))
    connection.commit()


def top_up_balance_action(login, connection):
    deposit_sum = input("Введіть суму на яку бажаєте поповнити баланс: ")
    if is_valid_sum(deposit_sum):
        balance_before = get_balance_sum(login, connection)
        balance_after = balance_before + float(deposit_sum)
        add_transaction(login, deposit_sum, "top_up_balance", connection)
        update_balance_sum(login, balance_after, connection)
        print(f"Баланс поповнено на {deposit_sum} грн")
    else:
        print("Ви ввели некоректне значення суми поповнення балансу")


def withdraw_money_action(login, connection):
    withdraw_sum = input("Введіть суму грошей, яку бажаєте зняти з рахунку: ")
    if is_valid_sum(withdraw_sum):
        balance_before = get_balance_sum(login, connection)
        balance_after = balance_before - float(withdraw_sum)
        if balance_after < 0:
            print("На рахунку недостатньо коштів для зняття даної суми")
        else:
            update_balance_sum(login, balance_after, connection)
            add_transaction(login, withdraw_sum, "withdraw_money", connection)
            print(f"З рахунку знято {withdraw_sum} грн")
    else:
        print("Ви ввели некоректне значення суми для зняття з рахунку")


def is_valid_sum(sum_string):
    try:
        sum_float = float(sum_string)
        if sum_float > 0:
            return True
        else:
            return False
    except Exception:
        return False


def add_transaction(login, operation_sum, operation_name, connection):
    cursor = connection.cursor()
    cursor.execute('''
        SELECT user_id 
        FROM users
        WHERE login=?
    ''', (login,))
    user_id = cursor.fetchone()[0]

    cursor.execute('''
        SELECT operation_id 
        FROM operations
        WHERE operation_name=?
    ''', (operation_name,))
    operation_id = cursor.fetchone()[0]

    cursor.execute('''
        INSERT INTO transactions (user_id, operation_id, transaction_amount) 
        VALUES (?, ?, ?) 
    ''', (user_id, operation_id, operation_sum))
    connection.commit()


def initialize_db(connection):
    cursor = connection.cursor()
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
        (banknote_nominal INTEGER PRIMARY KEY AUTOINCREMENT,
        banknote_amount INTEGER)
    """)


start()
