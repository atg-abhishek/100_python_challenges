'''
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

from pprint import pprint 
import operator
def lexical_ordering(li):
    return sorted(li, key=operator.itemgetter(0))

inp = input("Please enter the words separated by commas: ")
lst = inp.split(",")
pprint(lexical_ordering(lst))
