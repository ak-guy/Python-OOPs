'''
Slots : __slots__ is used to tell python that we will be using only certain pre-determined attributes
        python will then use a more compact data structure to store those attributes (not in dict)
        
        __slots__ are useful for better memory and speed but it comes at a cost of complexity and maintanence
'''
class Person:
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Arpit', 24)
if False:
    print(p.__dict__()) # this will attribute error because python now no longer has attribute __dict__, because we defined in slots that only 'name' and 'age' should exists
    p.style = 'Rambo' # this also will give attribute error as we cannot create new attributes
