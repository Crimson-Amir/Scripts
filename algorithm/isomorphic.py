"""
    soo , daa -> True
    soo , dea -> False
"""

def isomorph(string_1, string_2):
    if len(string_1) != len(string_2): raise KeyError('Strings must be same!')

    _morphs = {}
    for letter_1, letter_2 in zip(string_1, string_2):
        if letter_1 not in _morphs:
            _morphs[letter_1] = letter_2
            continue

        if _morphs[letter_1] == letter_2: continue
        return False
    return True


print(isomorph('missaki', 'nabbbea'))