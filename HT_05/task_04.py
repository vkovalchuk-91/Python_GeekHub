# Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345"
# -> просто потицяв по клавi =)
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
# -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)

from functools import reduce


def crazy_function(input_string):
    if 30 <= len(input_string) <= 50:
        length = len(input_string)
        letters_number = reduce(lambda count, char: count + char.isalpha(), input_string, 0)
        digits_number = reduce(lambda count, char: count + char.isdigit(), input_string, 0)
        print(f"Length: {length}, Letters number: {letters_number}, Digits number: {digits_number}")
    elif len(input_string) < 30:
        numbers_list = ''.join(map(lambda char: char if char.isdigit() else ' ', input_string)).split()
        numbers_count = reduce(lambda count, number: count + int(number), numbers_list, 0)
        letters = ''.join(filter(lambda char: char.isalpha(), input_string))
        print(f"Sum of all numbers: {numbers_count}, Letters: {letters}")
    elif len(input_string) > 50:
        print("Фантазія відсутня")


crazy_function("f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345")
crazy_function("f98neroi4nr0c3n30irn03ien3jnp46ij7k 5j78p3kj546p4")
crazy_function("f98neroi4nr0 j7846p4 65jj345")
