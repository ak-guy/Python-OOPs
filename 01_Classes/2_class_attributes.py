'''
MyClass is a class but it is also an object of type 'type'
'''
class MyClass:
    language = 'Python'
    version = '3.9'

'''
to get attribute directly from a class we use getattr function
getattr(object_symbol, attribute_name, optional_default)
'''
print(getattr(MyClass, 'language')) # => prints Python with type str
print(MyClass.language)

if False:
    print(getattr(MyClass, 'x')) # will throw AttributeError if attribute_name does not exists
print(getattr(MyClass, 'x', 'Something')) # => prints Something with type str as we gave it as optional_default

'''
to set attribute directly from a class we use setattr function
setattr(object_symbol, attribute_name, attribute_value)
'''
setattr(MyClass, 'version', '3.10')
print(MyClass.version)

'''
if we were to set an attribute which does not exists then this time it wont
throw exception as python is dynamical language it can modify our classes at runtime 
'''
setattr(MyClass, 'x', 10)
print(MyClass.x)

'''
where is the state of a class stored => it is stored in dictionary
but please remember not all states will be stored in dictionary
for example you can see __name___ is not present when we print __dict__
'''
print(MyClass.__dict__)

'''
to delete attributes from a class we use delattr function
delattr(object_symbol, attribute_name)
'''
delattr(MyClass, 'x') # we can also use => del Myclass.x
print(MyClass.__dict__)

if False:
    delattr(MyClass, 'c') # if we try to delete an attribute that does not exists in class then we receive an AttributeError

'''
accessing the namespace directly =>
MyClass.version
getattr(MyClass, 'version')
MyClass.__dict__['version']
'''
print(type(MyClass.__dict__['version']))
print(MyClass.__dict__['version'])
if False:
    MyClass.__dict__['version'] = 'Java' # this will throw exception TypeError as __dict__ is read-only