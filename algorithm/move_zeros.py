"""
    [False, 2, 5, "a", 0, 42, 0, 32] -> [False, 2, 5, "a", 42, 32, 0, 0]
"""

def move(arr, character=0):
    result = []
    number_of_character = 0
    for index, ch in enumerate(arr):
        if ch == character and not isinstance(ch, bool):
            arr.pop(index)
            number_of_character += 1
            continue
        result.append(ch)
    result.extend([character] * number_of_character)
    return result


print(move([False, 2, 5, "a", 0, 42, 0, 32]))


