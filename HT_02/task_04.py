# Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end
# script must print out result of concatenating all <number> strings.

inputted_number = int(input("Input number of concatenating strings: "))
concatenated_string = ""
for i in range(inputted_number):
    concatenated_string += input(f"Input string {i + 1} :")
print(f"Concatenated string: {concatenated_string}")
