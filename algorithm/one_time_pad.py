"""
    One Time Pad cipher
"""

import random

def encrypt(text):
    keys = []
    cipher = []
    character_unicode = [ord(unicode) for unicode in text]
    for character in character_unicode:
        random_key = random.randint(1, 300)
        character_cipher = character + random_key
        cipher.append(character_cipher)
        keys.append(random_key)
    return keys, cipher


def decrypt(cipher, keys):
    text = ''
    for code, key in zip(cipher, keys):
        text += chr(code - key)
    return text

k, c = encrypt('amir')
print(k, c)
print(decrypt(c, k))




