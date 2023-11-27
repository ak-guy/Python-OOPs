class MyClass:
    language = 'Python'

obj = MyClass()
'''
MyClass.__dict__ => {'language': 'Python'}
obj.__dict__ => {}

when we type MyClass.language it will return Python
that is also true when we type obj.language but this is because
when interpretor executes obj.language it first search in obj.__dict__
if it does not find the result there it will then search in MyClass.__dict__
and then return the result, same theory applies in 'Inheritance'
'''
print(MyClass.language)
print(obj.language)

obj.language = 'Java' # now we are changing namespace(__dict__) of obj object and not 'MyClass' object
print(obj.language)

obj2 = MyClass()
print(type(MyClass.__dict__))
print(type(obj2.__dict__))
'''
since type of obj.__dict__ is dict it becomes mutable meaning we can do this obj.__dict__['language'] = 'C++'
'''
obj.__dict__['language'] = 'C++' # this will not throw exception but if we do this -> MyClass.__dict__['language'] = 'C++' then we get AttributeError exception because type of MyClass.__dict__ is 'mappingproxy' not 'dict'
print(obj.language)