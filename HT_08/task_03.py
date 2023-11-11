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


def my_range(*args: int):
    start = 0
    step = 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError(f"my_range() accepts at most 3 arguments, got {len(args)}")

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

print("my_range(7)")
for i in my_range(7):
    print(i)

print("-----------")

print("my_range(3, 7)")
for i in my_range(3, 7):
    print(i)

print("-----------")

print("my_range(1, 10, 2)")
for i in my_range(1, 10, 2):
    print(i)

print("-----------")

print("my_range(1, -10, -2)")
for i in my_range(1, -10, -2):
    print(i)

print("-----------")

print("my_range(1, 10, -2)")
for i in my_range(1, 10, -2):
    print(i)
