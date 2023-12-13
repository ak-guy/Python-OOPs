'''
Delegating to parent: often when overriding methods, we need to delegate back to parent class
                      calling a method ( super().method_name(*args) ) 
                      using this we will call the method from parent class but it will be
                      bound to the instance it is called from

                      delegation works its way up the inheritance hierarchy until it finds what it needs
'''

class Person:
    def sing(self):
        return f'la la la'
    
class OtherStudent(Person):
    pass

class Student(OtherStudent):
    def sing(self):
        return super().sing() + ' la la la'
    
s = Student()
print(s.sing()) # la la la la la la

'''
Delegation and Method Binding : when we call a method from an instance it is bounded to that instance
                                but when we delegate from an instance to parent method then that method
                                is bound to the instance from which it was called
'''
class Person:
    def sing(self):
        print(f"in Person class : {self}")

class Student(Person):
    def sing(self):
        print(f"in Student class : {self}")
        return super().sing()
    
s = Student()
print(s.sing()) # in Student class : <__main__.Student object at 0x104c62cd0>   ||    in Person class : <__main__.Student object at 0x104c62cd0>

'''
Another Example
'''

class Person:
    def wake_up(self):
        print(f'Person wakes up')

    def do_work(self):
        print(f'Person works')

    def sleep(self):
        print(f'Person sleeps')

    def do_routine(self):
        self.wake_up()
        self.do_work()
        self.sleep()


class Student(Person):
    def do_work(self):
        print(f'Student works')

    def do_routine(self):
        super().do_routine() # see the difference in s.do_routine() this behavior is because when we call super().do_routine() we are secretly passing instance of Student so when it searches for do_work() it is able to find in Student class
        print(f'Done !!!')

p = Person()
print(p.do_routine())

s = Student()
print(s.do_routine())