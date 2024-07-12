"""
    [1, 5, 2, 8, 5, 2, 30, 3, -1, 2] -> remove -1
"""


def remove(arr):
    minimum_number = 0
    for number in arr:
        if number < minimum_number: minimum_number = number
    arr.remove(minimum_number)
    return arr

print(remove([1, 5, 2, 8, 5, 2, 30, 3, -1, 2]))
