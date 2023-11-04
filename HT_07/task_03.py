"""
На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні,
   так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для
   кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
"""


class ValidationException(Exception):
    pass


def validate_login_password(username, password):
    if len(username) < 3:
        raise ValidationException("Username must be no less than 3 characters")
    if len(username) > 50:
        raise ValidationException("Username must be no more than 50 characters")
    if len(password) < 8:
        raise ValidationException("Password must be at least 8 characters long")
    if not any(char.isdigit() for char in password):
        raise ValidationException("Password must contain at least one digit")
    if username == password:
        raise ValidationException("Username must be not equal to password")
    return True


users = [("VasyaaaaaaVasyaaaaaaVasyaaaaaaVasyaaaaaaVasyaaaaaa", "Pupkin79"),
         ("VasyaaaaaaVasyaaaaaaVasyaaaaaaVasyaaaaaaVasyaaaaaa1", "Pupkin79"),
         ("Vasyaaaaaa", "Pupkin79"), ("Vasyaaaaaa", "Vasyaaaaaa"), ("Vasya", "Pupkin"), ("Vasya", "Pupkin77"),
         ("Va", "Pupkin77"), ("Vas", "1234567"), ("Vas", "12345678")]
for user in users:
    print(f"Name: {user[0]}")
    print(f"Password: {user[1]}")

    try:
        if validate_login_password(user[0], user[1]):
            print("Status: OK")
    except ValidationException as e:
        print("Status: " + e.__str__())
    print("-----")
