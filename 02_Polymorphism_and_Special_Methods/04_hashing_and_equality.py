'''
>>> if we have to implement __hash__ then we should implement __eq__ also,

>>> if only __eq__ is implemented then __hash__ is set to None unless __hash__ is implemented

>>> we need to make class hashable if we want to use its object as a key in some dictionary 
    because key can only be some immutable obj, and for an obj to be immutable it should be hashable
'''

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f'Person({self.name})'
    
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name
    

p1 = Person('Arpit')
p2 = Person('Arpit')
p3 = Person('Ankit')
print(hash(p1) == hash(p2))
print(hash(p2) == hash(p3))
print(hash(p1))