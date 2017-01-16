'''
7.2

Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 
'''

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width

a = Rectangle(5,2)
print(a.area())