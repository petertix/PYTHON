# demo.py
import pdb

'''
    Example: How to set a break point in the code
'''

def add(a, b):
    return a + b

def func():
    pdb.set_trace()  # -- added breakpoint
    age = 26
    print("Hello Peter!!")
    print("Hello World!!")
    result = add("buggy", age)
    print('One extra print')
    return result

func()