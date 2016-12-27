'''
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

from pprint import pprint 

inp = input("Please enter a sentence: ")
letters = 0
digits = 0
for i in range(0, len(inp)):
    char = inp[i]
    if ord(char)>=ord('a') and ord(char)<=ord('z'):
        letters += 1
    if ord(char)>=ord('0') and ord(char)<=ord('9'):
        digits += 1
pprint("LETTERS " + str(letters))
pprint("DIGITS " + str(digits))