"""
    [1, 2, 3, 4, 5, 6, 7], 3 -> 2
"""

def search_binary(arr, target):
    minim = 0
    maxim = len(arr) - 1

    while minim <= maxim:
        mid = (minim + maxim) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            minim = mid + 1
        else:
            maxim = mid - 1
    return -1


print(search_binary([1, 2, 3, 4, 5, 6, 7], 5))