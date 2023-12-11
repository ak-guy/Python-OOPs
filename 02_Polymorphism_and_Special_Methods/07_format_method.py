from datetime import date
class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def __repr__(self):
        print('__repr__ called...')
        return f'Person(name={self.name}, dob={self.dob.isoformat()})'
    
    def __str__(self):
        print('__str__ called...')
        return f'Person({self.name})'
    
    def __format__(self, date_format_spec):
        print(f'__format__ called with {repr(date_format_spec)}...')
        dob = format(self.dob, date_format_spec)
        return f'Person(name={self.name}, dob={dob})'
    
p = Person('Arpit',date(1999, 8, 27))
print(p.__format__('%d-%m-%Y'))