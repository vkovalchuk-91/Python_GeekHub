# Write a script to remove an empty elements from a list.
#     Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

test_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
test_list = [current_element for current_element in test_list if len(current_element) > 0]
print(f'List without empty elements: {test_list}')
