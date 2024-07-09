"""
[1, 2, 3, 4, 5, 6, 7, 8]
min 5 = [5, 6, 7, 8]
max 5 = [1, 2, 3, 4, 5]
min max 5 = [5]
"""


def limit(_list, min_number=None, max_number=None):
    min_func =  lambda x : True if min_number is None else (x >= min_number)
    max_func = lambda x : True if max_number is None else (x <= max_number)

    return [number for number in _list if min_func(number) and max_func(number)]

print(limit([1, 2, 3, 4, 5, 6, 7, 8], 2, 6))