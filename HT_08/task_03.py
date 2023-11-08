"""
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції. Тобто щоб її можна було використати у
вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
   https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (аналог range(1, -10, 5)). Подивіться як веде себе стандартний range
   в таких випадках.
"""


def my_range(first_param: int, second_param: int = None, third_param: int = None, /):
    if second_param is None and third_param is None:
        start, stop, step = 0, first_param, 1
    elif third_param is None:
        start, stop, step = first_param, second_param, 1
    else:
        if third_param == 0:
            raise ValueError("my_range() third_param must not be zero")
        start, stop, step = first_param, second_param, third_param

    i = start
    result_list = []
    if step > 0:
        while i < stop:
            result_list.append(i)
            i += step
    else:
        while i > stop:
            result_list.append(i)
            i += step
    return (element for element in result_list)


for i in my_range(1, -10, 5):
    print(i)
