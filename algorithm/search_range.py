"""
    [1, 2, 2, 8, 8, 8, 19], 8 -> [3, 5]
"""

def range_search(arr, range_number):
    list_of_index = []
    range_started = False

    for index, number in enumerate(arr):
        if number == range_number:
            range_started = True
            list_of_index.append(index)

        elif number != range_number and range_started: return list_of_index[0::len(list_of_index) - 1]


print(range_search([1, 2, 2, 8, 8, 8, 8, 8, 8, 8, 19], 8))