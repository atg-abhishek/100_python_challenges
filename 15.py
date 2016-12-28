'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

a = int(input("Please enter the value of a : "))

res = a + (a*10 + a) + (a*100 + a*10 +a) + (a*1000 + a*100 + a*10 + a)
print(res)