# Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих
# чисел всередині цього діапазона. Не забудьте про перевірку на валідність введених даних та у випадку невідповідності -
# виведіть повідомлення.

import math


def prime_list(start: float, end: float):
    result = []
    for i in range(math.ceil(start), math.floor(end) + 1):
        if is_prime(i):
            result.append(i)
    return result


def is_prime(number: float):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def is_valid_input(inputted_str):
    try:
        floated_input = float(inputted_str)
    except ValueError:
        result = False
    else:
        result = floated_input >= 0
    return result


start_number_str = input("Enter start number: ")
end_number_str = input("Enter end number: ")
if is_valid_input(start_number_str) and is_valid_input(end_number_str):
    print(f"Simple numbers from {start_number_str} to {end_number_str}: "
          f"{prime_list(float(start_number_str),float(end_number_str))}")
else:
    print("Entered incorrect data!")
