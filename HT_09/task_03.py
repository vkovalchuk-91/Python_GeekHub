"""
Програма-банкомат.
   Використувуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та історію транзакцій (файл
      <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено цифри;
      знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання нового користувача -
      не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль). Якщо вони неправильні - вивести
      повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на
      ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій
"""

import csv
import json


def start():
    login = input("Введіть логін користувача: ")
    password = input("Введіть пароль користувача: ")
    if check_credentials(login, password):
        start_menu_actions(login)
    else:
        print("Неправильно введено логін/пароль")


def check_credentials(login, password):
    with open("task_03_files/users.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["login"] == login and row["password"] == password:
                return True
        return False


def start_menu_actions(login):
    while True:
        action_code = input("Введіть дію:\n   1. Продивитись баланс\n   2. Поповнити баланс\n   3. Зняти кошти\n   4. "
                            "Вихід\n")
        if action_code == "1":
            print(f"Поточний баланс користувача {login}: {get_balance_sum(login)}")
        elif action_code == "2":
            top_up_balance_action(login)
        elif action_code == "3":
            withdraw_money_action(login)
        elif action_code == "4":
            print("До побачення")
            return
        else:
            print("Неправильно введений код дії, спробуйте ще")


def get_balance_sum(login):
    try:
        with open("task_03_files/" + login + "_balance.txt", "r") as text_file:
            return float(text_file.read())
    except FileNotFoundError:
        raise FileNotFoundError("Файлу з записами балансу для даного користувача не знайдено")
    except ValueError:
        raise ValueError("Файл з записами балансу для даного користувача містить не цифрове значення")


def update_balance_sum(login, balance_sum):
    try:
        with open("task_03_files/" + login + "_balance.txt", "w") as text_file:
            text_file.write(str(balance_sum))
    except FileNotFoundError:
        raise FileNotFoundError("Файлу з записами балансу для даного користувача не знайдено")


def top_up_balance_action(login):
    deposit_sum = input("Введіть суму на яку бажаєте поповнити баланс: ")
    if is_valid_sum(deposit_sum):
        balance_before = get_balance_sum(login)
        balance_after = balance_before + float(deposit_sum)
        add_transaction(login, deposit_sum, "top_up_balance")
        update_balance_sum(login, balance_after)
        print(f"Баланс поповнено на {deposit_sum} грн")
    else:
        print("Ви ввели некоректне значення суми поповнення балансу")


def withdraw_money_action(login):
    withdraw_sum = input("Введіть суму грошей, яку бажаєте зняти з рахунку: ")
    if is_valid_sum(withdraw_sum):
        balance_before = get_balance_sum(login)
        balance_after = balance_before - float(withdraw_sum)
        if balance_after < 0:
            print("На рахунку недостатньо коштів для зняття даної суми")
        else:
            update_balance_sum(login, balance_after)
            add_transaction(login, withdraw_sum, "withdraw_money")
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


def add_transaction(login, operation_sum, operation_name):
    exist_data = read_exist_json_data(login)
    try:
        with open("task_03_files/" + login + "_transactions.json", "w") as json_file:
            new_row = [{"operation": operation_name, "sum": operation_sum}]
            transaction_list = exist_data + new_row
            json.dump(transaction_list, json_file)
    except FileNotFoundError:
        raise FileNotFoundError("Файлу з записами транзакцій для даного користувача не знайдено")


def read_exist_json_data(login):
    try:
        with open("task_03_files/" + login + "_transactions.json", "r") as json_file:
            return json.load(json_file)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        raise FileNotFoundError("Файлу з записами транзакцій для даного користувача не знайдено")


start()
