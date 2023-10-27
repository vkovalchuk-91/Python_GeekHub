# Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат (напр. інпут від
# юзера, результат математичної операції тощо). Також створiть четверту ф-цiю, яка всередині викликає 3 попереднi,
# обробляє їх результат та також повертає результат своєї роботи. Таким чином ми будемо викликати одну (четверту)
# функцiю, а вона в своєму тiлi - ще 3.

def read_value():
    return input("Input value: ")


def is_number(value):
    try:
        float(value)
    except ValueError:
        result = False
    else:
        result = True
    return result


def transform_to_number(value):
    return float(value)


def read_float():
    str_value = read_value()
    return f"Введене число = {transform_to_number(str_value)}" if is_number(str_value) else "Введено не число!"


print(read_float())
