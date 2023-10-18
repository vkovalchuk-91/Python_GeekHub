# Write a script which accepts two sequences of comma-separated colors from user. Then print out a set containing all
# the colors from color_list_1 which are not present in color_list_2.

color_list_1 = input("Input first sequence of comma-separated colors: ").split(",")
color_list_2 = input("Input second sequence of comma-separated colors: ").split(",")

print(
    f'All the colors from color_list_1 which are not present in color_list_2: {set(color_list_1) - set(color_list_2)}')
