# Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення у вигляді кортежа:
# периметр квадрата, площа квадрата та його діагональ.

from math import sqrt


def square(square_side: float):
    perimetr = square_side * 4
    area = square_side * 2
    diagonal = sqrt(2) * square_side
    return perimetr, area, diagonal


def is_valid_input(inputted_str):
    try:
        floated_input = float(inputted_str)
    except ValueError:
        result = False
    else:
        result = floated_input > 0
    return result


inputted_value = input("Enter square side: ")
if is_valid_input(inputted_value):
    print(f"Square parameters (perimetr, area, diagonal): {square(float(inputted_value))}")
else:
    print("Entered incorrect data!")
