"""
Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, продумайте
механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
"""
import requests
from datetime import datetime, timedelta


def get_exchange_rate(date, currency_code):
    url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"
    try:
        response = requests.get(url)
        data = response.json()
        currencies = data['exchangeRate']

        for response_currency in currencies:
            if response_currency['currency'] == currency_code:
                print(
                    f"Курс {currency_code} до UAH на {date}: Купівля - {response_currency['purchaseRateNB']}, "
                    f"Продаж - {response_currency['saleRateNB']}")
                return
        print(f"Курс для {currency_code} на {date} не знайдено.")
    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту: {e}")


def is_valid_date(date):
    try:
        datetime.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        return False


def is_valid_currency(currency_code):
    return currency_code in ("USD", "EUR", "CHF", "GBP", "PLZ", "SEK", "XAU", "CAD")


input_date = input("Введіть дату (або початкову дату і кінцеву дату через пробіл) у форматі DD.MM.YYYY: ").split()
currency = input("Введіть код валюти (наприклад, USD, EUR, CHF, GBP, PLZ, SEK, XAU, CAD): ").upper()
if len(input_date) == 1:
    if is_valid_date(input_date[0]):
        if is_valid_currency(currency):
            input_date = datetime.strptime(input_date[0], "%d.%m.%Y").strftime("%d.%m.%Y")
            get_exchange_rate(input_date, currency)
        else:
            print("Невірний код валюти (Доступні: USD, EUR, CHF, GBP, PLZ, SEK, XAU, CAD).")
    else:
        print("Невірний формат дати. Введіть у форматі DD.MM.YYYY.")
elif len(input_date) == 2:
    start_date, end_date = input_date
    try:
        if is_valid_date(input_date[0]):
            if is_valid_currency(currency):
                start_date = datetime.strptime(input_date[0], "%d.%m.%Y").strftime("%d.%m.%Y")
            else:
                print("Невірний код валюти (Доступні: USD, EUR, CHF, GBP, PLZ, SEK, XAU, CAD).")
        else:
            print("Невірний формат початкової дати. Введіть у форматі DD.MM.YYYY.")
        if is_valid_date(input_date[1]):
            if is_valid_currency(currency):
                end_date = datetime.strptime(input_date[1], "%d.%m.%Y").strftime("%d.%m.%Y")
            else:
                print("Невірний код валюти (Доступні: USD, EUR, CHF, GBP, PLZ, SEK, XAU, CAD).")
        else:
            print("Невірний формат кінцевої дати. Введіть у форматі DD.MM.YYYY.")
        delta = datetime.strptime(end_date, "%d.%m.%Y") - datetime.strptime(start_date, "%d.%m.%Y")
        for i in range(delta.days + 1):
            current_date = (datetime.strptime(start_date, "%d.%m.%Y") + timedelta(days=i)).strftime("%d.%m.%Y")
            get_exchange_rate(current_date, currency)
    except ValueError:
        print("Невірний формат дат. Введіть у форматі DD.MM.YYYY.")
else:
    print("Невірний формат введених даних. Введіть або одну дату, або початкову і кінцеву дати.")
