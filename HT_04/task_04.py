# Write a Python program that demonstrates exception chaining. Create a custom exception class called CustomError and
# another called SpecificError. In your program (could contain any logic you want), raise a SpecificError, and then
# catch it in a try/except block, re-raise it as a CustomError with the original exception as the cause. Display both
# the custom error message and the original exception message.

class CustomError(Exception):
    def __str__(self):
        return "CustomError"


class SpecificError(Exception):
    def __str__(self):
        return "SpecificError"


try:
    try:
        if True:
            raise SpecificError()
    except SpecificError as specific_error:
        print(f"Error message printed from {specific_error} catching block")
        raise CustomError from specific_error
except CustomError as custom_error:
    print(f"Error message printed from {custom_error} catching block")
