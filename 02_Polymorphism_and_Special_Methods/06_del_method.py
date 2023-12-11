'''
__del__ method : 
                 >>> it is a class finalizer, __del__ method is called right before
                     the object is destroyed by Garbage Collector, so GC determines 
                     when this dunder method should be called
                 >>> So we dont control when it gets called (PS: calling del(obj) does not call __del__)
                 >>> it is called only when all the references of the obj are gone
                 >>> exception occured in implementation of __del__ method is not raised but silenced by python
                 >>> so we use context manager to clean up resources

'''
import ctypes
from sys import getrefcount

def ref_count(memory_address):
    '''
    getting reference count using this method wont add 1 to return value because here we only pass address of an obj rather than obj itself
    '''
    return ctypes.c_long.from_address(memory_address)

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name={self.name})"
    
    def __del__(self):
        print(f"__del__ method called for Person(name={self.name})")

obj = Person("Arpit")
x = 1
print(ref_count(id(obj)))
print(ref_count(id(x)))
print(getrefcount(x))
print(getrefcount(obj))