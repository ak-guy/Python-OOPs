'''
some operator's dunder methods

'+' -> __add__
'-' -> __sub__
'*' -> __mul__
'/' -> __truediv__
'//' -> __floordiv__
'%' -> __mod__
'**' -> __pow__

'+=' -> __iadd__f
'-=' -> __isub__
'*=' -> __imul__
'/=' -> __itruediv__
'//=' -> __ifloordiv__
'%=' -> __imod__
'**=' -> __ipow__

'''

'''
***********************  IMPORTANT  **************************
important info about in-place operator (+=, -=, and so on)

l1 = [1,2]
l1 = l1 + [3,4]

now id of l1 ([1,2,3,4]) wont be same as prev l1 ([1,2])
but,

l1 = [1,2]
l1 += [3,4]
now id of l1 ([1,2,3,4]) will be same as prev l1 ([1,2])
but this wont work with tuple as they immutable

l1 = (1,2)
l1 += (3,4)
id(new_l1) != id(old_l1)

'''

from numbers import Real
from math import sqrt
class Vector:
    def __init__(self, *components) -> None:
        if len(components) < 1:
            raise ValueError("Cannot create empty vector")
        for component in components:
            if not isinstance(component, Real):
                raise ValueError(f"Vector component should be real, {component} is invalid.")

        self._components = tuple(components)
    
    def __len__(self):
        return len(self._components)
    
    @property
    def components(self):
        return self._components
    
    def __repr__(self) -> str:
        return f'Vector{self.components}'
    
    def validate_type_and_dimension(self, v):
        return isinstance(v, Vector) and len(self) == len(v)
    
    def __add__(self, other):
        '''
        adding two vectors
        '''
        if not self.validate_type_and_dimension(other):
            raise ValueError(f"Cannot add {self} and {other}")
        components = (a+b for a,b in zip(self.components, other.components))
        return Vector(*components)
    
    def __sub__(self, other):
        '''
        substracting two vectors
        '''
        if not self.validate_type_and_dimension(other):
            return NotImplemented # a way of raising TypeError
        components = (a-b for a,b in zip(self.components, other.components))
        return Vector(*components)
    
    def __mul__(self, other):
        '''
        dot product of two vectors and scalar product of vector and integer
        '''
        if isinstance(other, Real):
            components = (new*other for new in self.components)
            return Vector(*components)
        if isinstance(other, Vector):
            components = (a*b for a,b in zip(self.components, other.components))
            return sum(components)
        
        return NotImplemented

    def __rmul__(self, other):
        '''
        using __rmul__ method python flips the operand if we try to call 10 * Vector(1,2,3)
        '''
        return self * other
    
    def __iadd__(self, other):
        '''
        in-place addition of two vector
        '''
        if self.validate_type_and_dimension(other):
            components = (a+b for a,b in zip(self.components, other.components))
            self._components = tuple(components) # modifying self's component and not creating a new obj
            return self
        return NotImplemented

    def __abs__(self):
        return sqrt(sum(x ** 2 for x in self.components))
        
v1 = Vector(1,2,3)
v2 = Vector(3,6,7)
print(id(v1))
v3 = 10
v1 += v2
print(id(v1), v1)
print(abs(v1))