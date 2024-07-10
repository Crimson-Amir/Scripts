"""
    [1, 5, 2, 7, 5, 8, 1, 8] -> [1, 1, 2,5, 5, 7, 8, 8]
"""

def my_sort_situation(arr):
    new_list = []
    while arr:
        for index in arr:
            is_qualifield_for_add = True

            for other_numbers in arr:
                if index > other_numbers: is_qualifield_for_add = False

            if is_qualifield_for_add:
                new_list.append(index)
                arr.remove(index)

    return new_list

def bead_sort(arr):
    for _ in arr:
        for index, (upper_number, lower_number) in enumerate(zip(arr, arr[1:])):
            if upper_number > lower_number:
                arr[index] -= upper_number - lower_number
                arr[index + 1] += upper_number - lower_number
    return arr

print(bead_sort([1, 5, 2, 7, 5, 8, 1, 8]))