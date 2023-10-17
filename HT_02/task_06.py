# Write a script to check whether a value from user input is contained in a group of values.
#     e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#          [1, 2, 'u', 'a', 4, True] --> 5 --> False

inputted_value = input()
values = [1, 2, 'u', 'a', 4, True]
try:
    inputted_value = int(inputted_value)
except ValueError:
    try:
        inputted_value = float(inputted_value)
    except ValueError:
        if inputted_value == "True":
            inputted_value = True
        elif inputted_value == "False":
            inputted_value = False
print(inputted_value in values)
