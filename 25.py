'''
Question:
    Define a class, which have a class parameter and have a same instance parameter.
'''

class Animal():
    name = "Animal"
    def __init__(self,name=None):
        self.name = name

cat = Animal("Cat")
print(Animal.name + "  " + cat.name)
dog = Animal()
print(Animal.name + "  " + str(dog.name))
