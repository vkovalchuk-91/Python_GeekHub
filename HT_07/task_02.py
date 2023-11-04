"""
Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
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


try:
    if validate_login_password("VasyaaaaaaVasyaaaaaaVasyaaaaaaVasyaaaaaaVasyaaaaaa", "Pupkin79"):
        print("Valid login/password")
except ValidationException as e:
    print(e)
