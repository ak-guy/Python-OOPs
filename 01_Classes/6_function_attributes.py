class MyClass:
    def say_hello():
        print("Hello")

obj = MyClass()

print(MyClass.say_hello) # this returns a function
print(obj.say_hello) # this will return a bound method

MyClass.say_hello()
if False:
    obj.say_hello() # this raises TypeError exception
print('\n')
'''
method is an actual object type in python which is different from a function
method is like a function, it is callable, but unlike a function a method is
bound to some object and that parameter is passed as first parameter of the 
function that is getting called

when we type obj.say_hello(),
this means say_hello is method object and it is bounded to obj
so when obj.say_hello is called, the bound object obj is injected as the first
parameter to the method say_hello like MyClass.say_hello(obj)

so method are objects that combine instance of some class and function method,
like any object methods also have attributes
__self__ --> the instance, method is bound to
__func__ --> the original function (defined in class)

calling obj.method(args) --> method.__func__(method.__self__, args)
'''
print(obj.say_hello.__self__) # this will point to the object 'obj'
print(obj.say_hello.__func__) # this will point to the function in the class itself

'''
to ensure obj.say_hello() does not throw exception we need to use it as
an instance method, meaning a method which belongs to an instance, that
we can acheive by passing a parameter object in say_hello function
'''

class MyClass:
    def say_hello(object):
        print("Hello")

obj = MyClass()
print(obj.say_hello) # again a bound method or instance method
print(obj.say_hello()) # now this wont throw exception
print(MyClass.say_hello('Null'))

'''
Also another way to add arg will be
'''
class MyClass:
    language = 'Python'
    def say_hello(*args):
        print(f"Hello there, {args}")

print(MyClass.say_hello())
obj = MyClass()
print(obj.say_hello())

'''
when we pass in object as a parameter in a function then we can
use its attribute there
'''

class MyClass:
    language = 'Python'
    def say_hello(object):
        print(f"Hello there, {object.language}")

obj = MyClass()
print(obj.say_hello())
obj.language = 'Java'
print(obj.say_hello())


class Person:
    name = 'Default Name'

    def set_name(instance_obj, name): # usual convention is to replace instance_obj with self keyword
        instance_obj.name = name

    def reset_name(self):
        self.name = Person.name

p = Person()
p.set_name('Arpit')
print(p.__dict__)
p.reset_name()
print(p.__dict__)

p = Person()
Person.set_name(p, 'Ankit')
print(p.__dict__)
p.reset_name()
print(p.__dict__)

'''
creating an attribute in class at runtime
'''

class Person:
    name = 'Default Name'

    def set_name(instance_obj, name): # usual convention is to replace instance_obj with self keyword
        instance_obj.name = name

    def reset_name(self):
        self.name = Person.name

p = Person()

Person.do_work = lambda self: print(f'do_work is called from {self}')
print(Person.__dict__) # 'do_work': <function <lambda> at 0x7f8219c160e0>
print(p.do_work) # <bound method <lambda> of <__main__.Person object at 0x7ff01104fac0>>
p.do_work()

p.another_work = lambda *self: print(f'here another work is being created in an instance hence it wont be available in main class {self}')
print(p.another_work)
p.another_work()