# Write a script to concatenate all elements in a list into a string and print it. List must be include both strings
# and integers and must be hardcoded.

values = [1, 2, 'u', 'a', 4, True]
print("Concatenated value of all list elements: " + "".join([str(i) for i in values]))
