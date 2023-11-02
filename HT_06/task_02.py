# Написати функцію <bank> , яка працює за наступною логікою: користувач робить вклад у розмірі <a> одиниць строком на
# <years> років під <percents> відсотків (кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми
# вкладу і в наступному році на них також нараховуються відсотки). Параметр <percents> є необов'язковим і має значення
# по замовчуванню <10> (10%). Функція повинна принтануть суму, яка буде на рахунку, а також її повернути (але округлену
# до копійок).

def bank(a: float, years: float, percents: float = 10):
    return a * ((1 + percents / 100) ** years)


def is_valid_input(inputted_str):
    try:
        floated_input = float(inputted_str)
    except ValueError:
        result = False
    else:
        result = floated_input > 0
    return result


a_str = input("Enter deposit start value: ")
years_str = input("Enter deposit years: ")
percents_str = input("Enter deposit percents: ")
if is_valid_input(a_str) and is_valid_input(years_str) and is_valid_input(percents_str):
    print(f"Final sum: {bank(float(a_str), float(years_str), float(percents_str))}")
    print(f"Final sum (with default percents): {bank(float(a_str), float(years_str))}")
else:
    print("Entered incorrect data!")
