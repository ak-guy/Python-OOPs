'''
to create a read only property we need to create a property with only
get accessor defined
'''
import math
class Circle:
    def __init__(self, r):
        self._r = r

    @property
    def area(self):
        return math.pi * self._r * self._r
    
c = Circle(10)
if False:
    c.area = 10 # will throw AttributeError Exception
print(c.area)


'''
Application : Caching Computed Properties
'''
