class MyClass:
    def __init__(self, language, name=None) -> None:
        self._language = language
        self._name = name

    @property
    def language(self):
        print(f'getter called... getting attribute -> _language')
        return self._language
    
    @language.setter
    def set_language(self, language):
        print(f'setter called... setting _language as  "{language}"')
        self._name = 'Arpit' # setting _name as 'Arpit' whenever we set language
        self._language = language

    @language.deleter
    def del_language(self):
        print('deleter called...')
        del self._language

print(*property.__dict__, sep=' , ')

new_class = MyClass('English', 'Arpit')
print(new_class.language)
new_class.set_language = 'Maths'
print(new_class.language)