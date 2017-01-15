'''
Question:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

'''
import math
class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi*self.radius*self.radius

a = Circle(5)
print(a.area())