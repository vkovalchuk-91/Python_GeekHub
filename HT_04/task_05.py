# Create a Python program that repeatedly prompts the user for a number until a valid integer is provided. Use a
# try/except block to handle any ValueError exceptions, and keep asking for input until a valid integer is entered.
# Display the final valid integer.

while True:
    number = input("Input integer: ")
    try:
        int_number = int(number)
    except ValueError:
        print("Entered incorrect value, try again")
    else:
        print(f"Entered {int_number}")
        break
