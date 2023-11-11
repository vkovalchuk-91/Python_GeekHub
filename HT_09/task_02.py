"""
Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів. Файл також додайте в репозиторій.
На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу. Кількість
символів в блоках - та, яка введена в другому параметрі. Придумайте самі, як обробляти помилку, наприклад, коли
кількість символів більша, ніж є в файлі або, наприклад, файл із двох символів і треба вивести по одному символу, то що
виводити на місці середнього блоку символів?). Не забудьте додати перевірку чи файл існує.
"""


def print_blocks(path: str, symbols_number: int):
    if symbols_number <= 0:
        raise Exception("Symbols number less or equal 0")
    try:
        with open(path) as text_file:
            content = text_file.read()
            if symbols_number > len(content):
                raise SymbolsNumber
            if symbols_number % 2 != len(content) % 2:
                raise MiddleSymbolsNumberException
            print("Beginning symbols: " + content[:symbols_number])
            start_index = int((len(content) - symbols_number) / 2)
            print("Middle symbols: " + content[start_index: start_index + symbols_number])
            print("Ending symbols: " + content[-symbols_number:])
    except FileNotFoundError:
        raise FileNotFoundError("File not exist")


class SymbolsNumber(Exception):
    def __str__(self):
        return "Symbols number more then file content length"


class MiddleSymbolsNumberException(Exception):
    def __str__(self):
        return "Impossible to print the middle of the file content, wrong number of symbols in the middle"


with open("task_02_files/task_02_test_01.txt") as file:
    print("For file content: " + file.read() + " (2 symbols number)")
print_blocks("task_02_files/task_02_test_01.txt", 2)

print("----------------------------------")

with open("task_02_files/task_02_test_02.txt") as file:
    print("For file content: " + file.read() + " (3 symbols number)")
print_blocks("task_02_files/task_02_test_02.txt", 3)
