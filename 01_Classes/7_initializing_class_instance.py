'''
whenever we instantiate a class, by default python does two things in order,
first it will create an instance with empty namespace
second it will initialize the namespace of object based on __init__ (only if __init__ method is defined)
like this => obj.__init__('3.11')

so what __init__ does is it provides custom namespace for the class's instance
'''
class MyClass:
    # language is class attribute
    language = 'Python'

    def __init__(instance_obj, version):
        # version is instance attribute
        instance_obj.version = version
    
obj = MyClass('3.11')
print(obj.__dict__)