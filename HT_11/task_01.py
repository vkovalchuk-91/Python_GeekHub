"""
Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з
2-ма числами, а саме додавання, віднімання, множення, ділення.
- Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повенен повернути результат виконання ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
    ...
"""


class Calc:
    """
    Клас для виконання математичних операцій та збереження результату.

    Attributes:
        last_result (float): Зберігає результат останньої виконаної операції.

    Methods:
        __init__(): Ініціалізує клас та встановлює last_result на None.

        add(first_number, second_number): Виконує операцію додавання та оновлює last_result.

        divide(first_number, second_number): Виконує операцію ділення та оновлює last_result.

        multiply(first_number, second_number): Виконує операцію множення та оновлює last_result.

        subtract(first_number, second_number): Виконує операцію віднімання та оновлює last_result.
    """
    def __init__(self):
        """
        Ініціалізує клас Calc та встановлює last_result на None.

        Example:
            calc_instance = Calc()
                """
        self.last_result = None
        print(f"last_result --> {self.last_result}")

    def add(self, first_number, second_number):
        """
        Виконує операцію додавання та оновлює last_result.

        Args:
            first_number (float): Перше число для додавання.
            second_number (float): Друге число для додавання.

        Example:
            calc_instance.add(2, 3)
        """
        print(f"{first_number} + {second_number}")
        print(f"last_result --> {self.last_result}")
        self.last_result = first_number + second_number

    def divide(self, first_number, second_number):
        """
        Виконує операцію ділення та оновлює last_result.

        Args:
            first_number (float): Ділене число.
            second_number (float): Дільник.

        Example:
            calc_instance.divide(6, 2)
        """
        print(f"{first_number} / {second_number}")
        print(f"last_result --> {self.last_result}")
        self.last_result = first_number / second_number

    def multiply(self, first_number, second_number):
        """
        Виконує операцію множення та оновлює last_result.

        Args:
            first_number (float): Перше число для множення.
            second_number (float): Друге число для множення.

        Example:
            calc_instance.multiply(4, 5)
        """
        print(f"{first_number} * {second_number}")
        print(f"last_result --> {self.last_result}")
        self.last_result = first_number * second_number

    def subtract(self, first_number, second_number):
        """
        Виконує операцію віднімання та оновлює last_result.

        Args:
            first_number (float): Перше число для віднімання.
            second_number (float): Друге число для віднімання.

        Example:
            calc_instance.subtract(8, 3)
        """
        print(f"{first_number} - {second_number}")
        print(f"last_result --> {self.last_result}")
        self.last_result = first_number - second_number


calculator = Calc()
calculator.add(1, 1)
calculator.multiply(2, 3)
calculator.multiply(3, 4)
