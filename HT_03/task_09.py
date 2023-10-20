# Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку
# (границі включно). P.S. Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400.

start_year = int(input(f"Input start year: "))
end_year = int(input(f"Input end year: "))
for year in range(start_year, end_year + 1):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(year)
