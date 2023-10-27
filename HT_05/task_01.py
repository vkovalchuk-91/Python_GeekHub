# Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде повертати пору року, якiй
# цей мiсяць належить (зима, весна, лiто або осiнь). У випадку некоректного введеного значення - виводити відповідне
# повідомлення.

def season(month: int):
    if month in [1, 2, 12]:
        result = "зима"
    elif month in [3, 4, 5]:
        result = "весна"
    elif month in [6, 7, 8]:
        result = "літо"
    elif month in [9, 10, 11]:
        result = "осінь"
    else:
        result = "некоректно введені дані"
    return result


print(f"1 місяць це {season(1)}")
print(f"2 місяць це {season(2)}")
print(f"3 місяць це {season(3)}")
print(f"4 місяць це {season(4)}")
print(f"5 місяць це {season(5)}")
print(f"6 місяць це {season(6)}")
print(f"7 місяць це {season(7)}")
print(f"8 місяць це {season(8)}")
print(f"9 місяць це {season(9)}")
print(f"10 місяць це {season(10)}")
print(f"11 місяць це {season(11)}")
print(f"12 місяць це {season(12)}")
print(f"При введенні 55 - {season(55)}")
