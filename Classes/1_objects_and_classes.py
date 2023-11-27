'''
an object is an container that 
contains data => state / attributes
contains functionality => behavior / methods
'''

'''
class is like a template used to create objects
objects created from that class are called instances with type class_name
'''

'''
if class is an object, and objects are created from classes, how are classes created?
 => class are created from the type metaclass 
'''

'''
everything in python is an object
class is also an object with type => type
instances is also an object with type => class_name
'''
class Person:
    pass

obj = Person()
print(isinstance(obj, Person)) # True

# we created an empty class but by default it will contain few attributes and methods
print(obj.__dir__()) # will list all attributes and methods
