'''
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''

from pprint import pprint

def make_grid(x,y):
    res = []
    for i in range(0, x):
        temp = []
        for j in range(0,y):
            temp.append(i*j)
        res.append(temp)
    return res

inp = input("Please enter the values of X and Y separated by a comma: ")
xy = inp.split(",")
x = int(xy[0])
y = int(xy[1])

pprint(make_grid(x,y))