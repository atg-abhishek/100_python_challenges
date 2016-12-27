'''
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

from pprint import pprint 
import re

inp = input("Please enter a sentence : ")
lower = 0
upper = 0
for c in inp:
    if c.islower():
        lower+= 1 
    if c.isupper():
        upper += 1
pprint("UPPER CASE : " + str(upper))
pprint("LOWER CASE : " + str(lower))
