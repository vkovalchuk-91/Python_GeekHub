# Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких
# операцiя, яку зробити! Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом -
# типу 1 + 2). Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями на
# предмет помилок!

def calculate(first_arg: float, operator: str, second_arg: float):
    if operator == "+":
        result = first_arg + second_arg
    elif operator == "-":
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


x_str = input("Enter first operand: ")
operator_str = input("Enter operator (+, -, *, /, %, //, **): ")
y_str = input("Enter second operand: ")

if operator_str not in ["+", "-", "*", "/", "%", "//", "**"]:
    print("Entered incorrect operator sign")
else:
    try:
        x_float = float(x_str)
        y_float = float(y_str)
    except ValueError:
        print("Entered incorrect operands")
    else:
        print(calculate(x_float, operator_str, y_float))
