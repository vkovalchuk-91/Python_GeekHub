# Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову, яка буде виводити поточне значення, якщо
# остача від ділення на 17 дорівнює 0.

inputted_value = int(input(f"Input limiting value: "))
for i in range(inputted_value + 1):
    if i % 17 == 0:
        print(i)
