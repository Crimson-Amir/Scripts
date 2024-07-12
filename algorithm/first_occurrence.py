"""
    [2, 2, 2, 5, 5, 5 ,7, 7, 8], 5 -> 3
"""

def occurrence_first(arr, target):
    minim = 0
    maxim = len(arr) - 1

    while minim <= maxim:
        mid = (minim + maxim) // 2

        if minim == maxim:
            return mid
        elif arr[mid] < target:
            minim = mid + 1
        else:
            maxim = mid
    return -1


def occurrence_last(arr, target):
    minim = 0
    maxim = len(arr) - 1

    while minim <= maxim:
        mid = (minim + maxim) // 2
        if (arr[mid] == target and mid == len(arr) - 1) or (arr[mid] == target and arr[mid + 1] > target):
            return mid
        elif arr[mid] <= target:
            minim = mid + 1
        else:
            maxim = mid - 1
    return -1

print(occurrence_last([2, 2, 2, 5, 5, 5 ,7, 7, 8], 5))