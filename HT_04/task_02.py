# Create a custom exception class called NegativeValueError. Write a Python program that takes an integer as input and
# raises the NegativeValueError if the input is negative. Handle this custom exception with a try/except block and
# display an error message.

class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} is negative"


try:
    int_number = int(input("Input integer number: "))
    if int_number < 0:
        raise NegativeValueError(int_number)
except NegativeValueError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid integer.")
else:
    print(f"Entered not negative integer: {int_number}")
