"""
Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів. Після запуска програми на екран виводиться в лівій
   половині - колір автомобільного, а в правій - пішохідного світлофора. Кожну 1 секунду виводиться поточні кольори.
   Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах (пішоходам
   зелений тільки коли автомобілям червоний).
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
"""
import time


def colors_generator(red_time_for_car: int, yellow_time_for_car: int, green_time_for_car: int):
    one_iteration_color_list = (["Red        Green" for _ in range(red_time_for_car)] +
                                ["Yellow     Red" for _ in range(yellow_time_for_car)] +
                                ["Green      Red" for _ in range(green_time_for_car)] +
                                ["Yellow     Red" for _ in range(yellow_time_for_car)])
    i = 0
    while i < len(one_iteration_color_list):
        yield one_iteration_color_list[i]
        i += 1
        if i == len(one_iteration_color_list):
            i = 0


for colors in colors_generator(4, 2, 3):
    print(colors)
    time.sleep(1)
