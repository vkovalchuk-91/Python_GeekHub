"""
Створити клас Person, в якому буде присутнім метод __init__ який буде приймати якісь аргументи, які зберігатиме в
відповідні змінні.
- Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
- Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession (його не має інсувати під
час ініціалізації).
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.profession = None

    def print_name(self):
        return self.name

    def show_age(self):
        return self.age

    def show_all_information(self):
        return self.name, self.age, self.profession


vasya = Person("Vasya", 25)
petya = Person("Petya", 20)
vasya.profession = "Hacker"
petya.profession = "Security"

print(f"Person name: {vasya.name}")
print(f"Person age: {vasya.age}")
print(f"All information (name, age, profession): {vasya.show_all_information()}")
print("--------------")
print(f"Person name: {petya.name}")
print(f"Person age: {petya.age}")
print(f"All information (name, age, profession): {petya.show_all_information()}")
