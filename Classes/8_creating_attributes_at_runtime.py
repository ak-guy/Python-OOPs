'''

'''
class Person:
    name = 'Default Name'

    def set_name(instance_obj, name): # usual convention is to replace instance_obj with self keyword
        instance_obj.name = name

    def reset_name(self):
        self.name = Person.name

p = Person()
p.version = '3.11'

def f(obj):
    print('Hey')
# we cannot use this way if want to use object instance's namespace, this is because p.another_work will belongs to an object
p.another_work = lambda *obj: print(f'stored at >> {obj}')
print(p.another_work)
p.another_work()

'''
how can we create and bind a method to an instance at runtime
this can be acheived by defining a method that binds the function to the instance

MethodType(function, object_name)
'''

from types import MethodType

class Person:
    name = 'Default Name'

    def set_name(instance_obj, name): # usual convention is to replace instance_obj with self keyword
        instance_obj.name = name

    def reset_name(self):
        self.name = Person.name

p = Person()
p.another_work = MethodType(lambda self: print(f'Hey {self.name}'), p)
print(p.another_work())

'''
another example
'''
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person('Arpit')
p2 = Person('Ankit')

def say_hello(obj):
    print(f'Hey there, {obj.name}')

say_hello(p1)
say_hello(p2)

p1.say_hello = MethodType(say_hello, p1) # this way we can bind a method say_hello to an object p1
print(p1.__dict__.get('say_hello', None))
print(Person.__dict__.get('say_hello', None))
p1.say_hello()