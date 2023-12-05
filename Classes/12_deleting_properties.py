'''
generally it is used to perform some cleanups upon property deletion
it does not remove property from the class it just removes it from 
instance namespace
and it just calls the deleter method
'''

class MyClass:
    def __init__(self, language, name=None) -> None:
        self._language = language
        self._name = name

    @property
    def language(self):
        print(f'getter called... getting attribute -> _language')
        return self._language

    @language.setter
    def language(self, language):
        print(f'setter called... setting _language as  "{language}"')
        self._name = 'Arpit' # setting _name as 'Arpit' whenever we set language
        self._language = language

    @language.deleter
    def language(self):
        print('deleter called...')
        del self._language

obj = MyClass('English', 'Arpit')
print(obj.__dict__) # {'_language': 'English', '_name': 'Arpit'}
print(MyClass.__dict__) # {'__module__': '__main__', '__init__': <function MyClass.__init__ at 0x100920af0>, 'language': <property object at 0x10092b4f0>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
del obj.language
print(obj.__dict__) # {'_name': 'Arpit'}
print(MyClass.__dict__) # same as before