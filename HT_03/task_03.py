# Write a script to concatenate following dictionaries to create a new one.
#     dict_1 = {'foo': 'bar', 'bar': 'buz'}
#     dict_2 = {'dou': 'jones', 'USD': 36}
#     dict_3 = {'AUD': 19.2, 'name': 'Tom'}

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}
united_dict = dict_1.copy()
united_dict.update(dict_2)
united_dict.update(dict_3)
print(f"United dictionary: {united_dict}")
