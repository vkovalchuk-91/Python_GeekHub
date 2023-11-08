"""
Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає
генератор, який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із
послідовності - ітерація починається знову.
   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   for elem in generator([1, 2, 3]):
       print(elem)
   1
   2
   3
   1
   2
   3
   1
   .......
"""

from typing import Iterable


def generator(iterable_object: Iterable):
    i = 0
    while i < len(list(iterable_object)):
        yield iterable_object[i]
        i += 1
        if i == len(list(iterable_object)):
            i = 0


for elem in generator([1, 2, 3]):
    print(elem)
