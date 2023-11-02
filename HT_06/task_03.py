# Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число
# просте і False - якщо ні.

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


number_str = input("Enter deposit start value: ")
if is_valid_input(number_str):
    if is_prime(float(number_str)):
        print("Number is simple")
    else:
        print("Number is not simple")
else:
    print("Entered incorrect data!")
