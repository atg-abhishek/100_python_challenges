'''
Question 9
Level 2

Question:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

from pprint import pprint 

print("Please enter your input at the prompt, to stop type \q")
cont = True
inp = []
while (cont):
    temp = input("Please enter your input: ")
    if temp == "\q":
        cont = False
        break
    else:
        inp.append(temp)

for line in inp:
    pprint(line.upper())