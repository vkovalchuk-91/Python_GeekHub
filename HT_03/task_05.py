# Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.

dict_1 = {'foo': '36', 'bar': 'jones', 'dou': 'jones', 'USD': 36, 'AUD': 19.2, 'name': 'Tom'}
dict_1 = {key: value for key, value in dict_1.items() if list(dict_1.values()).count(value) == 1}
print(f"Dictionary without values duplicates: {dict_1}")
