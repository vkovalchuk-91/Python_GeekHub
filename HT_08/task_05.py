"""
Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних букв та цифр, які
зустрічаються в рядку більше ніж 1 раз. Рядок буде складатися лише з цифр та букв (великих і малих). Реалізуйте
обчислення за допомогою генератора.
    Example (input string -> result):
    "abcde" -> 0            # немає символів, що повторюються
    "aabbcde" -> 2          # 'a' та 'b'
    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
    "indivisibility" -> 1   # 'i' присутнє 6 разів
    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
    "aA11" -> 2             # 'a' і '1'
    "ABBA" -> 2             # 'A' і 'B' кожна двічі
"""


def get_repeatable_signs_number(input_string: str):
    result_dict = {}
    for i in input_string:
        if i.lower() in result_dict:
            result_dict[i.lower()] = result_dict[i.lower()] + 1
        else:
            result_dict[i.lower()] = 1
    generator = (1 for i in result_dict.values() if i > 1)
    return sum(generator)


print(get_repeatable_signs_number("abcde"))
print(get_repeatable_signs_number("aabbcde"))
print(get_repeatable_signs_number("aabBcde"))
print(get_repeatable_signs_number("indivisibility"))
print(get_repeatable_signs_number("Indivisibilities"))
print(get_repeatable_signs_number("aA11"))
print(get_repeatable_signs_number("ABBA"))
print(get_repeatable_signs_number("fffawfwa"))
