# Write a script to get the maximum and minimum value in a dictionary.

dict_1 = {'foo': '36', 'bar': [-3], 'dou': {"value": 77}, 'USD': 36, 'AUD': 19.2, 'name': 99.99}
number_values = [value for value in dict_1.values() if isinstance(value, (int, float))]
max_value = max(number_values)
min_value = min(number_values)
print(f"Max value: {max_value}")
print(f"Min value: {min_value}")
