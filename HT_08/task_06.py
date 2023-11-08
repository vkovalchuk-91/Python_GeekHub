"""
Напишіть функцію,яка прймає рядок з декількох слів і повертає довжину найкоротшого слова. Реалізуйте обчислення за
допомогою генератора.
"""


def get_shortest_word_length(input_string: str):
    result_list = input_string.split()
    if len(result_list) == 0:
        result = 0
    else:
        generator = (len(i) for i in result_list)
        result = min(generator)
    return result


print(get_shortest_word_length("sfgn fgnsr srthrst"))
print(get_shortest_word_length("aabt b cde"))
print(get_shortest_word_length("a a b B c d e"))
print(get_shortest_word_length("indivisibility ttttttttt"))
print(get_shortest_word_length("Indivisibilities t"))
print(get_shortest_word_length(""))
print(get_shortest_word_length("ABBA tttt"))
print(get_shortest_word_length("fffawfwa"))
