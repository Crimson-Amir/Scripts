"""
    [1, 2, 3, 4, 5, 6, 7], 3 -> 2
"""

def search_linear(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index

print(search_linear([1, 2, 3, 4, 5, 6, 7], 3))