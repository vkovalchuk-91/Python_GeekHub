# Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких
# операцiя, яку зробити! Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом -
# типу 1 + 2). Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями на
# предмет помилок!

def calculate(first_arg: float, operator: str, second_arg: float):
    if operator == "+":
        result = first_arg + second_arg
    elif operator == "+":
        result = first_arg - second_arg
    elif operator == "*":
        result = first_arg * second_arg
    elif operator == "/":
        result = first_arg / second_arg if second_arg != 0 else "Zero division"
    elif operator == "%":
        result = first_arg % second_arg if second_arg != 0 else "Zero division"
    elif operator == "//":
        result = first_arg // second_arg if second_arg != 0 else "Zero division"
    elif operator == "**":
        result = first_arg ** second_arg
    else:
        result = "Incorrect operator"
    return result


print(calculate(2, "+", 10))
