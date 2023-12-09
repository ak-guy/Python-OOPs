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

'''
Another way of doing it 
'''

from types import MethodType

class Person:
    def __init__(self, name) -> None:
        self.name = name

    def register_do_work(self, func):
        '''
        what this method will do is, it will create an attribute _do_work for object self and assign its functionality based on func
        '''
        setattr(self, '_do_work', MethodType(func, self))

    def do_work(self):
        do_work_method = getattr(self, '_do_work', None)

        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError('You must register do work first')
        
good_person = Person('Ankit')
bad_person = Person('Arpit')

if False:
    # this will raise AttributeError as _do_work does not belong to good_person obj
    good_person.do_work()

def take_math(self):
    print(f'{self.name} is going to take math class today')

print(good_person.__dict__)
good_person.register_do_work(take_math)
print(good_person.__dict__)


def take_english(self):
    print(f'{self.name} is going to take english class today')

print(bad_person.__dict__)
bad_person.register_do_work(take_english)
print(bad_person.__dict__)

persons = [good_person, bad_person]
for p in persons:
    p.do_work()