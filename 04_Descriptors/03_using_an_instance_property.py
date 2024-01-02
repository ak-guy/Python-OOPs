'''
in this section we will try to solve the problem of same instance of descriptor being used by mutiple instances of owner class

class IntegerValue:
    def __init__(self):
        self.data = {} # we will storea key:value => instance : attribute_value

    def __set__(self, instance, value):
        self.data[instance] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self.data.get(instance)
'''

class IntegerValue:
    def __init__(self):
        self.data = {} # we will storea key:value => instance : attribute_value

    def __set__(self, instance, value):
        self.data[instance] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self.data.get(instance)
    
class Point2D:
    x = IntegerValue()
    y = IntegerValue()

p1 = Point2D()
p2 = Point2D()

p1.x = 10
p1.y = 20

p2.x = 11
p2.y = 21

print(Point2D.x.data)
print(p1.x)