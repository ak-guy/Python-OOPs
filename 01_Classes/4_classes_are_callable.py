'''
when we create a class using the 'class' keyword
python automatically adds behaviors to the class
including, it makes the class callable which returns an object
which is an instance of that class having type 'class_name'
'''

'''
when we call a class, a class instance object is created
which has its own namespace, meaning it will be distict
from the namespace of the class that was used to create
the object.

This object has some attributes python automatically implements for us
__dict__ => object's local namespace
__class__ => tells us which class was used to instantiate the object 
'''

class MyClass:
    __class__ = str
    language = 'Python'

    def say_hello():
        print(f"Hello from {MyClass.language}")

p1 = MyClass
p2 = MyClass()
print(MyClass.__dict__)
print(p1.__dict__) # this will contain same namespace as that of MyClass because it is not an instance of MyClass
print(p2.__dict__) # this will be empty

print(type(p2)) # type will specify correct type of object
print(p2.__class__) # __class__ can be modified so we can make it any type

print(isinstance(p2, MyClass))
print(isinstance(p2, str)) # since we made changes to __class__ attribute it affected at metaclass level hence now p2 is also an instance of str