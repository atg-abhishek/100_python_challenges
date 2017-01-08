'''
Question:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
'''

def map_it(li):
    res = map(lambda x: x*x, li)
    return list(res)
print(map_it([1,2,3,4,5,6,7,8,9,10]))