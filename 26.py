'''
Question:
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
'''

def try_filter(li):
    res = filter(lambda x: x%2==0,li)
    for r in res:
        print(r)

try_filter([1,2,3,4,5,6,7,8,9,10])