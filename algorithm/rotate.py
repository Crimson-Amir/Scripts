"""
    hello, 2 -> llohe
"""

def rotate(text, rotate_number=2):
    ready_text = ['*'] * len(text)
    for index, character in enumerate(text):
        ready_text[(index + rotate_number) % len(ready_text)] = character
    return ''.join(ready_text)

def simple_way(text, rotate_number=2):
    ready_text = text + text
    return ready_text[rotate_number:rotate_number+len(text)]

print(rotate('hello', 3))
print(simple_way('hello', 2))











