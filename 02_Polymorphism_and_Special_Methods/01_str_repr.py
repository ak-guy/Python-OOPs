'''
__repr__ vs __str__ -> both are used for string representation of an object

__repr__ -> this is usually meant for developers
            they can make it so, that this string representation can be used to recreate the object
            usefull for debugging
            called when using repr() method 

__str__ -> this is usually meant for users
           if __str__ is not implemented then python looks for __repr__ instead
           and if neither is implemented then we will take __repr__ from parent class

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        print('__repr__ called')
        return f"Person(name='{self.name}, age=self.age')"
    
    def __str__(self):
        print('__str__ called')
        return self.name

obj = Person('Arpit', 24)
print(repr(obj))
print(obj)