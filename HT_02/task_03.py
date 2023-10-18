# Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.

inputted_number = int(input("Input number of positive integers: "))
print(f"Sum of first {inputted_number} integers = {sum(range(1, inputted_number + 1))}")
