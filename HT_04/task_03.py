# Create a Python script that takes an age as input. If the age is less than 18 or greater than 120, raise a custom
# exception called InvalidAgeError. Handle the InvalidAgeError by displaying an appropriate error message.

class InvalidAgeError(Exception):
    def __str__(self):
        return "Age must be from 18 to 120"


try:
    age = int(input("Input age: "))
    if age < 18 or age > 120:
        raise InvalidAgeError()
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid age value.")
else:
    print(f"Entered age: {age}")
