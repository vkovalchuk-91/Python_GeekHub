# Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(limit_number: float):
    if 0 <= limit_number < 1:
        return [0]
    if 1 <= limit_number < 2:
        return[0, 1, 1]
    else:
        i = 1
        result = [0, 1]
        while i <= limit_number:
            result.append(i)
            i = result[-1] + result[-2]
    return result


def is_valid_input(inputted_str):
    try:
        floated_input = float(inputted_str)
    except ValueError:
        result = False
    else:
        result = floated_input >= 0
    return result


limit_number_str = input("Enter limit number: ")
if is_valid_input(limit_number_str):
    print(f"Fibonacci numbers that aren't greater than {limit_number_str}: {fibonacci(float(limit_number_str))}")
else:
    print("Entered incorrect data!")

