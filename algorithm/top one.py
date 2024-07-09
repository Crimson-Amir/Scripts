"""
    [1, 1, 2, 3, 4, 2] -> [1, 2]
"""


def top_one(arr):
    top_ones = {}
    for number in arr:
        top_ones[number] = arr.count(number)

    max_value = 0
    ret = {}
    counts = 1
    for number, count in top_ones.items():
        if count > max_value:
            ret[f'biggest{counts}'] = {number: count}
            max_value = count
        elif count == max_value:
            counts += 1
            ret[f'biggest{counts}'] = {number: count}

    return ret

print(top_one([1, 1, 2, 3, 4, 2]))
