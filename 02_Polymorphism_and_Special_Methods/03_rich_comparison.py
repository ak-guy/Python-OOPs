'''
Rich comparison method

'__lt__' -> less than
'__le__' -> less than equal to
'__gt__' -> greater than
'__ge__' -> greater than equal to
'__eq__' -> equal
'__ne__' -> not equal

note : if suppose __lt__ is not implemented than for a < b,
       python will search for __gt__ (in class methods) method b > a
       "Furthermore, if one comparison does not exist, Python will try to the reverse the operands and the operator 
       (and unlike the arithmetic operators, both operands can be of the same type)."
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'
        
    def __eq__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            other = Vector(*other)
        elif isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
v1 = Vector(1,1)
v2 = Vector(1,1)
print(v1 == (1,1,1))
print(v1 == v2)