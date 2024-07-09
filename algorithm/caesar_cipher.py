"""
amir ---shift4block---> eqmv

"""


from string import ascii_letters

def encode(string, shift=2):
    res = ''
    for letter in string:
        if letter not in ascii_letters: res += letter; continue
        res += ascii_letters[(ascii_letters.index(letter) + shift) % len(ascii_letters)]
    return res


def decode(string, shift):
    shift *= -1
    return encode(string, shift)

def brute_force(string, what_you_want):
    key = len(ascii_letters) * -1
    my_words = {}
    while key <= len(ascii_letters):
        dec = decode(string, key)
        my_words[key] = dec
        if dec == what_you_want:
            return dec
        key += 1
    return my_words


print(encode('amir', 4))
print(brute_force('eqmv', 'amirs'))
