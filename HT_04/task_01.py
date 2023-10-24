# Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
# Кожне введене значення спочатку пробує перевести в int. У разі помилки - пробує перевести в float, а якщо і там ловить
# помилку - пропонує ввести значення ще раз (зручніше на даному етапі навчання для цього використати цикл while)
# Виводить результат ділення першого на друге. Якщо при цьому виникає помилка - оброблює її і виводить відповідне
# повідомлення

input_needed = True
first_number, second_number = "", ""
while input_needed:
    print_text = ""
    first_number = input("Input first number: ")
    second_number = input("Input second number: ")

    try:
        int(first_number)
        int(second_number)
    except ValueError:
        try:
            float(first_number)
            float(second_number)
        except ValueError:
            print_text = "Entered incorrect type, try again"
        else:
            input_needed = False
            print_text = "At least one of entered values is float"
    else:
        input_needed = False
        print_text = "Both entered values are integer"
    print(print_text)

try:
    print(f"{first_number} / {second_number} = {float(first_number) / float(second_number)}")
except Exception as e:
    print(f"Error: {e}")
