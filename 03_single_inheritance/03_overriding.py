'''
Overriding : when we inherit from another class, we inherit its attributes, including all its callable
             we can choose to redefine an existing callable in the sub class, this is called overriding
'''

class Person:
    def say_hello(self):
        return 'hello'
    def say_bye(self):
        return 'Bye!'
    
class Ak(Person):
    def say_hello(self):
        return 'yo'
    
p1 = Person()
print(p1.say_hello())
print(p1.say_bye())

p2 = Ak()
print(p2.say_hello()) # uses override
print(p2.say_bye()) # inherits from Person class because say_bye is not implemented in Ak class

'''
Overriding Functionality : when we create any class we can override any method defined in its parent class
'''

print(dir(object))
class Person:
    def __init__(self, name): # overrides __init__ from object class
        self.name = name

    def __repr__(self) -> str: # overrides __repr__ from object class
        return f'{self.__class__.__name__}(name={self.name})'
    
class Student(Person):
    def __repr__(self) -> str: # overrides __repr__ from Person class
        return f'{self.__class__.__name__}(name={self.name})'

    # since __init__ is not implemented in Student class so it inherits __init__ from Person Class

obj1 = Student('Arpit')   
print(repr(obj1))
obj2 = Person('Ankit')
print(repr(obj2))


'''
Another Example
'''
class Shape:
    def __init__(self, name):
        self.name = name
        
    def info(self):
         return f'Shape.info called for Shape({self.name})'
    
    def extended_info(self):
        return f'Shape.extended_info called for Shape({self.name})', self.info()
    
class Polygon(Shape):
    def __init__(self, name):
        self.name = name  # we'll come back to this later in the context of using the super()
        
    def info(self):
        return f'Polygon.info called for Polygon({self.name})'
    
p = Polygon('Rhombus')
'''
in this case we will use extended_info from Shape class but when we call self.info()
then we will use Polygon class because self is an instance of Polygon so first
it is going to search there.
'''
print(p.extended_info())