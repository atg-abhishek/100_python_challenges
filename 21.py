'''
Question
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

'''
import math
ins = []
vert = 0
hori = 0
while(True):
    s = input()
    if not s:
        break
    ins.append(s)

for i in ins:
    temp = i.split(" ")
    direction = temp[0]
    steps = int(temp[1])
    if direction == "UP":
        vert += steps
    if direction == "DOWN":
        vert -= steps
    if direction == "LEFT":
        hori -= steps
    if direction == "RIGHT":
        hori += steps
print(int(math.sqrt(math.pow(hori,2) + math.pow(vert,2))))