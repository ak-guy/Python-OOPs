'''
Example of Getter method
'''
from datetime import datetime
class TimeUTC:
    def __get__(self, instance, owner_class):
        print(f'__get__called from self= {self}, instance= {instance}, owner_class= {owner_class}')
        return datetime.utcnow().isoformat()
    
class Logger1:
    current_time = TimeUTC()

class Logger2:
    current_time = TimeUTC()

l1 = Logger1()
l1_1 = Logger1()
l2 = Logger2()
print(Logger1.current_time) # same self as l1.current_time and l1_1.current_time, instance=None
print(Logger2.current_time) # instance = None
print(l1.current_time)
print(l1_1.current_time)
print(l2.current_time)
print('\n')
'''
since we are able to distinguish from where our __get__ method was called (class/instance)
'''
class TimeUTC:
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return datetime.utcnow().isoformat()
    
class Logger:
    current_time = TimeUTC()

l1 = Logger()
print(Logger.current_time)
print(l1.current_time)
print('\n')
'''
above implemented method will be in accordance to @property decorator
'''
class Test:
    @property
    def current_time(self):
        return datetime.utcnow().isoformat()

t1 = Test()
print(Test.current_time)
print(t1.current_time)
print('\n')

'''
example to show how once we make class attribute an instance of descriptor class, we will reuse it while making 
different instances of main class
'''
class CountDown:
    def __init__(self, start):
        self.start = start + 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.start -= 1
        return self.start

class Rocket:
    countdown = CountDown(10)

# every instance of Rocket class is going to share same instance of descriptor
rocket1 = Rocket()
rocket2 = Rocket()

# now we will print countdown of rocket1 and rocket2
print(rocket1.countdown)
print(rocket2.countdown)
print(rocket1.countdown)
print(rocket2.countdown)
# as we can when we check for rocket2's countdown we are referencing to already decreased start value
print('\n')

'''
Example of Setter Method
'''

class IntegerValue:
    def __set__(self, instance, value):
        # print(f'__set__ called from self = {self}, instance = {instance}')
        self._value = value

    def __get__(self, instance, owner_class):
        if instance is None:
            # print(f'_get__ called from class')
            return self
        else:
            # print(f'__get__ called from self = {self}, instance = {instance}, owner_class = {owner_class}')
            return self._value
    
class Point2D:
    x = IntegerValue()
    y = IntegerValue()
    
p1 = Point2D()
p1.x = 1.2
p1.y = 1.4
print(p1.x, p1.y)

p2 = Point2D()
p2.x = 2.9
print(p2.x, p2.y)
print(p1.x, p1.y) # p1.x also got changed