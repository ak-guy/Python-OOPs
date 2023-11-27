'''
setting an attribute value to a callable
attribute value can be an object, other class, any callable, or anything
'''
class MyClass:
    language = 'Python'

    def say_hello():
        print(f"Hello from {MyClass.language}")

print(MyClass.__dict__)

'''
now we can call say_hello attribute by these ways
'''
MyClass.say_hello()
MyClass.__dict__['say_hello']()
getattr(MyClass, 'say_hello')()