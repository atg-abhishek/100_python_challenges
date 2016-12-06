'''
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''

from pprint import pprint

num = int(input("Please enter the number for which the factorial is to be calculated: "))
res = 1
for i in range(2,num+1):
    res *= i
pprint(res)