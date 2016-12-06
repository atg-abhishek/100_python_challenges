'''
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

from pprint import pprint 
import operator

inp = input("Please enter words separated by whitepaces: ")
lst = inp.split(" ")
unique_words = set(lst)
unique_words_list = [word for word in unique_words]
lexical_ordered = sorted(unique_words_list, key=operator.itemgetter(0))

pprint(" ".join(lexical_ordered))