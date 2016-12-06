'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

from pprint import pprint

class Hello:
    def __init__(self):
        self.greeting = ""
    def getString(self):
        self.greeting = input("Please enter a greeting: ")
    
    def printString(self):
        pprint(self.greeting.upper())

def test():
    h = Hello()
    h.getString()
    h.printString()

test()