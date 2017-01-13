'''
Question:
Define a class named American which has a static method called printNationality.
'''

class American():
    def __init__(self, nationality="American"):
        self.nationality = nationality
    @staticmethod
    def printNationality(self):
        print(self.nationality)

a = American()
American.printNationality(a)