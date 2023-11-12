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


def my_range(start: int = 0, stop: int = None, step: int = 1):
    if stop is None:
        stop = start
        start = 0

    i = start
    if step > 0:
        while i < stop:
            yield i
            i += step
    else:
        while i > stop:
            yield i
            i += step


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
