"""
    [2, 7, 11, 15], 22 -> [1, 3]
"""

def sum_two(arr, target):
    arr.sort()
    print(arr)
    first_index = 0
    last_index = len(arr) - 1
    while first_index < last_index:
        res = arr[first_index] + arr[last_index]
        if res == target:
            return first_index, last_index
        elif res < target:
            first_index += 1
        else:
            last_index -= 1

print(sum_two([6, 3, 51, 213, 2, 12, 5245,23, 1, 2532352, 12, 4, 11], 4))
