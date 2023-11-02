# Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів у ньомy і виводить
# результат. Елементами списку можуть бути дані будь-яких типів.
#     Наприклад:
#     1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"

def count_elements(value_list: list):
    bool_list = []
    other_list = []
    for value in value_list:
        if isinstance(value, bool):
            bool_list.append(value)
        else:
            other_list.append(value)

    other_str = get_str_from_list(other_list)
    bool_str = get_str_from_list(bool_list)

    result_list = [value for value in [other_str, bool_str] if value]
    return ", ".join(result_list)


def get_str_from_list(analysing_list):
    count_list = []
    for item in analysing_list:
        if item not in count_list:
            count_list.append(item)
    return ", ".join([f"{item} -> {analysing_list.count(item)}" for item in count_list])


print(f"[ 1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ]:      {count_elements([1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]])}")
print(f"[ 1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ]:      {count_elements([1, 1, True, 'foo', [1, 2], 5, [2, 4], True, 'foo', 1, [1, 2]])}")
print(f"[ 1, 1, 'foo', [1, 2], 'foo', 1, [1, 2] ]:      {count_elements([1, 1, 'foo', [1, 2], 'foo', 1, [1, 2]])}")
