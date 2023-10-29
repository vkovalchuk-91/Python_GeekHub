# Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями. Створiть просту умовну конструкцiю (звiсно
# вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" та у випадку
# нервіності - виводити ще і різницю.
#     Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
#     x > y;       вiдповiдь - "х бiльше нiж у на z"
#     x < y;       вiдповiдь - "у бiльше нiж х на z"
#     x == y.      вiдповiдь - "х дорiвнює y"

def compare_values(x: float, y: float):
    if x > y:
        result = f"х бiльше нiж у на {x - y}"
    elif x < y:
        result = f"y бiльше нiж x на {y - x}"
    else:
        result = f"х дорiвнює y"
    return result


x_str = input("Введіть x: ")
y_str = input("Введіть y: ")
try:
    x_float = float(x_str)
    y_float = float(y_str)
except ValueError:
    print("Entered incorrect values")
else:
    print(compare_values(x_float, y_float))
