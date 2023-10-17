# Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.

inputted_number = int(input())
counter = 0
for i in range(1, inputted_number + 1):
    counter += i
print(counter)
