'''
Question:
Define a class named American and its subclass NewYorker. 
'''

class American():
    def __init__(self, style="American"):
        self.style = style

class NewYorker(American):
    pass

a = NewYorker()
print(a.style)
