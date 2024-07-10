"""
    [1, 3, 5, 7] 3 : 4
    [1, 3, 5, 7] 4 : 3
"""

def search(arr: list, number):
    arr.sort()
    print(f'I sort you array: {arr}')
    if number in arr: return arr.index(number)
    shoud_be_add = 1
    for index, arr_number in enumerate(arr):
        if (number > arr_number) and (index + 1 == len(arr)): return f'shoud br in index {index + 1}'
        if (number > arr_number) and (number < arr[index + shoud_be_add]): return f'shoud br in index {index + 1}'

# print(search([1, 3, 5, 7], 12))


def another_way(arr: list, number):
    minimum = 0
    maximum = len(arr) - 1
    avg = maximum // 2

    while minimum <= maximum:
        if number > arr[avg]:
            avg += 1
            minimum = avg
        else:
            avg -= 1
            maximum = avg

    return minimum


print(another_way([1, 3, 5, 7], 3))
