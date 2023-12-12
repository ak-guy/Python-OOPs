'''
            _____ Shape _____
           |                 |
        Ellipse            Polygon
           |               |     |
        Circle      Rectangle    Triangle
                       |
                    Square
'''

class Shape:
    pass

class Ellipse(Shape):
    pass

class Circle(Ellipse):
    pass

class Polygon(Shape):
    pass

class Rectangle(Polygon):
    pass

class Square(Rectangle):
    pass

class Triangle(Polygon):
    pass

print(issubclass(Circle, Shape)) # True
print(issubclass(Shape, Circle)) # False
print(issubclass(Square, Shape)) # True
print(issubclass(Square, Polygon)) # True
print(issubclass(Circle, Polygon)) # False
print('\n')

s1 = Shape()
sq = Square()
el = Ellipse()
po = Polygon()
ci = Circle()
re = Rectangle()
tr = Triangle()

print(isinstance(s1, Shape)) # True
print(isinstance(sq, Polygon)) # True

'''
Note : type(obj) gives from which class that obj is created
       isinstance(obj, Class_Name) returns bool value if obj is of Class_Name it will return True even if Class_Name is Ancestor of type(obj)
'''
