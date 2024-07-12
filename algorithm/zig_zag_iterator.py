"""
    [1, 3, 5, 7, 9], [2, 4, 6, 8, 10] -> 1,2,3,4,5,6,7,8,9,10
"""

count = 0
def zig_zag_iterator(first_list, second_list):
    global count
    final_list = [number for get_touple in zip(first_list, second_list) for number in get_touple]
    for number in final_list: yield number

a = zig_zag_iterator([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

