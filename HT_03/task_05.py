# Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.

dict_1 = {'foo': '36', 'bar': 'jones', 'dou': 'jones', 'USD': 36, 'AUD': 19.2, 'name': 'Tom'}
print(f'Original dictionary: {dict_1}')
unique_dict = {}
for key, value in dict_1.items():
    if value not in unique_dict.values():
        unique_dict[key] = value
print(f"Dictionary without duplicated values: {unique_dict}")
