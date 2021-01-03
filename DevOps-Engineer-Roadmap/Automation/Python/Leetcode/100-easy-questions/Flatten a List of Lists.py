def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

nested_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
print('Original List', nested_list)
print('Transformed Flat List', flatten_list(nested_list))


regular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]
flat_list = [item for sublist in regular_list for item in sublist]
print('Original list', regular_list)
print('Transformed list', flat_list)


import itertools

regular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
flat_list = list(itertools.chain(*regular_list))

print('Original list', regular_list)
print('Transformed list', flat_list)


regular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]

flat_list = sum(regular_list, [])

print('Original list', regular_list)
print('Transformed list', flat_list)
