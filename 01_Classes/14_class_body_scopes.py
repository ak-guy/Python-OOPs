'''
Example 1
'''
class Account:
    COMP_FREQ = 12
    APR = 0.02 # 2%
    APY = (1 + APR/COMP_FREQ) ** COMP_FREQ - 1

    def __init__(self, balance):
        self._balance = balance
    
    def monthly_interest_1(self):
        return f'This is monthly interest {self.APY}'
    
    @classmethod
    def monthly_interest_2(cls):
        return f'This is monthly interest {cls.APY}'
    
    @staticmethod
    def monthly_interest_3():
        return f'This is monthly interest {Account.APY}'
    
    def monthly_interest_4(self): # this will throw exception as APY is not defined as this variable is not defined in function's scope or any enclosing scopes
        return f'This is monthly interest {APY}'
    
'''
Example 2
'''
name = 'Arpit'
class Name:
    name = 'Ankit'
    list_1 = [name] * 3 # here name scope lies in Name class level
    list_2 = [name for i in range(3)] # since this is list comprehension name scope lies at module level

    @classmethod
    def say_hello(cls):
        return f'{name} says hello'
    
print(Name.list_1)
print(Name.list_2)
