# Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with
# those numbers.

inputted_numbers = input("Input comma-separated numbers for list and tuple generating: ")
generated_list = inputted_numbers.split(",")
generated_tuple = tuple(generated_list)
