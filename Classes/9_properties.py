'''
sometimes assigning a value directly to an instance attribute does not make sense
like suppose we have to add additional validation before we assign any value to
instance attribute then we cannot do that with obj.attribute = value

so what we do is we make sure that developer has to use getattribute and
setattribute to modify any instance's attribute

we can use property class in this case to ensure that we use get_attribute and set_attr
when dealing with attributes

dummy_attribute_name = property(fget=get_instance_property_value, fset=set_instance_property_value, fdel=delete_instance_property)
'''

class MyClass:
    def __init__(self, language, name=None) -> None:
        self._language = language
        self._name = name

    def get_language(self):
        return self._language
    
    def set_language(self, language):
        self._name = 'Arpit' # setting _name as 'Arpit' whenever we set language
        self._language = language

    language = property(fget=get_language, fset=set_language)

obj = MyClass('Python')
print(obj.__dict__) # {'_language': 'Python', '_name': None}
obj.language = 'Java' # here we are language instead of _language because we used property class and assigned it to language
print(obj.language, obj._name)