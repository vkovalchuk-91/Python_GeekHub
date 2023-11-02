# Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто функція приймає два
# аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна -
# навпаки - пересуваємо елементи з початку списку в його кінець).
#    Наприклад:
#    fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#    fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]

def shift_values(value_list: list, shift: int):
    result = []
    if shift >= 0:
        for i in range(-shift, 0):
            result.append(value_list[i])
        for i in range(len(value_list) - shift):
            result.append(value_list[i])
    else:
        for i in range(- shift, len(value_list)):
            result.append(value_list[i])
        for i in range(-shift):
            result.append(value_list[i])
    return result


print(f"fnc([1, 2, 3, 4, 5], shift=1): {shift_values([1, 2, 3, 4, 5], shift=1)}")
print(f"fnc([1, 2, 3, 4, 5], shift=-2): {shift_values([1, 2, 3, 4, 5], shift=-2)}")
print(f"fnc([1, 2, 3, 4, 5, 6, 7, 8, 9], shift=5): {shift_values([1, 2, 3, 4, 5, 6, 7, 8, 9], shift=5)}")
print(f"fnc([1, 2, 3, 4, 5, 6, 7, 8, 9], shift=-4): {shift_values([1, 2, 3, 4, 5, 6, 7, 8, 9], shift=-4)}")
