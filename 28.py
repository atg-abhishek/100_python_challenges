'''
Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
Listed as Q3.5 on the link
'''

def res(li):
    return list(map(lambda x : x*x, filter(lambda x: x%2==0, li)))

print(res([1,2,3,4,5,6,7,8,9,10]))