'''
Define a custom exception class which takes a string message as attribute.
'''

class CustomException(Exception):
    """
        Custom exception class
        Attributes:
            msg -- string to be printed out
    """
    def __init__(self, msg):
        self.msg = msg

err = CustomException("hello")