'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''

def createGenerator(n):
    for i in range(0,n+1):
        if i%7==0:
            yield i
n = int(input("Please enter the value for n : "))
mygen = createGenerator(n)
for i in mygen:
    print(i)