"""
Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль). Функція повинна приймати
три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за
замовчуванням - <False>).
Логіка наступна:
    якщо введено коректну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція вертає False
        якщо silent == False -породжується виключення LoginException (його також треба створити =))
"""


class LoginException(Exception):
    def __str__(self):
        return "Error: Wrong username or password"


def check_login(username, password, silent=False):
    users = [("user1", "password1"), ("user2", "password2"), ("user3", "password3"), ("user4", "password4"),
             ("user5", "password5")]
    for usr, pswrd in users:
        if username == usr and password == pswrd:
            return True

    if silent:
        return False
    else:
        raise LoginException()


try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    result = check_login(username, password)
    if result:
        print("Successful login")
    else:
        print("Unsuccessful login")
except LoginException as e:
    print(e)
