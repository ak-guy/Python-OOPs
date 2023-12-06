'''
class methods always be bounded to class and never to an instance
'''
class MyClass:
    def hello():
        return 'hello'
    
    def say_hello(self):
        return f'Hello from {self}'
    
    @classmethod
    def cls_hello(cls):
        return f'Hello from {cls}'
    
obj = MyClass()
print(MyClass.hello) # return a function
print(obj.hello) # returns a bound method MyClass object (calling this function will throw exception as no self is passed)
print('\n')
print(MyClass.say_hello) # return a function
print(obj.say_hello) # returns a bound method MyClass object (wont throw exception)
print('\n')
print(MyClass.cls_hello) # returns a bound method of class MyClass
print(obj.cls_hello) # returns a bound method of class MyClass
print('\n')

'''
static methods is a way to define a function in a class
such that it will never be bound to either class or obj
'''
class Circle:
    @staticmethod
    def get_radius():
        return f'some dummy value'
    
obj = Circle()
print(Circle.get_radius) # returns a normal function (<function Circle.get_radius at 0x104b11d30>)
print(obj.get_radius) # return a normal function (<function Circle.get_radius at 0x104b11d30>)


'''
so we have three types of functions
1. functions bound to instance when called from instance (def f(self): )
2. functions bound to class no matter from where it is called (@classmethod)
3. functions bound to neither class nor instance (@staticmethod)
'''