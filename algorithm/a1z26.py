"""
    amir -> [97, 109, 105, 104]
"""

def encode(string):
    return [ord(character) for character in string]

def decode(list_of_codes):
    return ''.join([chr(code) for code in list_of_codes])


print(encode('amir'))
print(decode([97, 109, 105, 114]))
