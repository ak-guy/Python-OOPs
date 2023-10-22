#################
## CHALLENGE 3 ##
#################

# Requirements:
# - Define a new type called Contact, which should store a person's name, last name, phone, email, as well as an
# instance attribute called display_mode, which defaults to "masked"
# - Should be able to create instances using name and last name only
# - Two instances should be considered equal if any of the following conditions are met:
#     - name, last name, phone and email are the same, or
#     - phone or email are the same
# - The instance representation should return obfuscated name and last name attributes when display_mode is set to "masked"
# and the regular full representation including all attributes otherwise
# - The str() representation on the other hand should always return the first letter of the last name followed by the
# first letter of the first name
# - A user should be able to format a masked instance's string representation so as to reveal all the attributes

# Example Usage:
# c1 = Contact("Andy", "Bek")
# c2 = Contact("Andy", "Bek", "647-537-9271")
# c3 = Contact("Andrew", "Bek", "647-537-9271", "hey@andybek.com")
# c4 = Contact("Andy", "Bek", "647-537-9271", display_mode="show")

# c2 == c3
# True # because the phone number is the same

# c1
# Contact(name=An***, last_name=B**)

# str(c1)
# 'BA'

# "{c:unmasked}".format(c=c1)
# 'Contact(name=Andy, last_name=Bek, phone=None, email=None)'

# f"{c2:unmasked}"
# 'Contact(name=Andy, last_name=Bek, phone=647-537-9271, email=None)'

# format(c2, "unmasked")
# 'Contact(name=Andy, last_name=Bek, phone=647-537-9271, email=None)'

class Contact():

    def __init__(self, name, last_name, phone=None, email=None, display_mode = "masked"):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode

    def __repr__(self):
        if self.display_mode == 'masked':
            return f"Contact(name='{self._obfuscate(self.name)}', last_name='{self._obfuscate(self.last_name)}')"
        
        return f"Contact(name='{self.name}', last_name='{self.last_name}', phone='{self.phone}', email='{self.email}')"

    def __str__(self):
        first = self.name[0]
        last = self.last_name[0]
        return f"Belongs to {last} {first}"

    def __eq__(self, other):
        # if other is not an instance of Contact, we will return False
        if not isinstance(other, Contact):
            return False

        if (self.phone is not None and self.phone ==other.phone) or (self.email is not None and self.email == other.email):
            return True
        
        return (self.name == other.name and self.last_name == other.last_name)
    
    # it is better practise to define __hash__ if we are modifying __eq__ dunder
    def __hash__(self) -> int:
        return hash((self.name, self.last_name, self.phone, self.email))
    
    @staticmethod
    def _obfuscate(text):
        half_len = len(text) // 2
        return text[:half_len] + '*' * (half_len + 1)
    

c1 = Contact("Andy", "Bek")
c2 = Contact("Andy", "Bek", "647-537-9271")
c3 = Contact("Andrew", "Bek", "647-537-9271", "hey@andybek.com")
c4 = Contact("Andy", "Bek", "647-537-9271", display_mode="show")

c1
print(Contact._obfuscate('adffdsn'))
print(c2 == c3)
print(c4)