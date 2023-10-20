# Write a script that will run through a list of tuples and replace the last value for each tuple. The list of tuples
# can be hardcoded. The "replacement" value is entered by user. The number of elements in the tuples must be different.

tuple_list = [(1, 5, True), ("aaa", 2), (0,)]
counter = 0
for current_tuple in tuple_list:
    replacing_value = input(f"Input value for replacing in {counter + 1} tuple: ")
    tuple_list[counter] = current_tuple[:len(current_tuple) - 1] + tuple(replacing_value)
    counter += 1
print(f'List with replaced elements: {tuple_list}')
