'''
Write a function to compute 5/0 and use try/except to catch the exceptions.
'''

try:
    print (5/0)
except ZeroDivisionError:
    print("Division by zero not allowed")
except Exception:
    print("caught a general exception")
finally:
    print("in final block for cleanup")
