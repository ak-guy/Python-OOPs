'''
an object can be made callable by implementing __call__ method
'''

class Person:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"__call__ method called from Person('{self.name}')")

p = Person('Arpit')
p()
print(type(p))

'''
this shows that not only methods can be called, but any callables can be called

and we can check if anything is callable or not by -> callable(variable_name) -> returns Bool
'''
from functools import partial

def dummy_func(a,b,c):
    return a,b,c
partial_func = partial(dummy_func, 10,20)
print(type(dummy_func))
print(type(partial_func))
print(partial_func)
print(partial_func(30))
print('\n')

class CustomPartial:
    def __init__(self, function,*args):
        self._function = function
        self._args = args

    def __call__(self, *args):
        return self._function(*self._args, *args)
    
partial_func = CustomPartial(dummy_func, 10,20)
print(partial_func)
print(partial_func(30))

