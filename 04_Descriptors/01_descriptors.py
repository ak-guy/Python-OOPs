'''
Descriptors: Python descriptors are created to manage the attributes of different classes
             which use the object as reference. In descriptors we used three different 
             methods that are __getters__(), __setters__(), and __delete__().
             If any of those methods are defined for an object, it can be termed as a descriptor

             method that needs to be defined in Descriptor class
             1. __get__
             2. __set__
             3. __delete__
'''

from datetime import datetime
class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat()
    
class Logger:
    current_time = TimeUTC()
if False:
    Logger.current_time = 'x'
    print(Logger.current_time) # output -> x
print(Logger.current_time) # output -> 2024-01-01T17:53:28.569948

'''
example - 1
'''
from random import choice, seed

class Deck:
    @property
    def suit(self):
        return choice(('Spade', 'Heart', 'Diamond', 'Club'))
    
    @property
    def card(self):
        return choice(tuple('123456789KQJA') + (10, ))
    
d = Deck()
seed(0)
for i in range(10):
    print(d.suit, d.card)
print('\n')

'''
in previous example we simply used two different fuction to get some random choice out of input that we provided
much better way will be to pass it to some function that will do all that
'''
class Choice:
    def __init__(self, *choices):
        self.choices = choices

    def __get__(self, instance, owner_class):
        return choice(self.choices)
    
class Deck:
    suit = Choice('Spade', 'Heart', 'Diamond', 'Club')
    card = Choice(*'123456789KQJA', '10')

d = Deck()
seed(0)
for i in range(10):
    print(d.suit, d.card)