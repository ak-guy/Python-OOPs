class Account:
    apr = 3.0
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = 'Generic Account'
        
    def calc_interest(self):
        return f'Calc interest on "{self.account_type}" with APR = {type(self).apr}'
        
        
class Savings(Account):
    apr = 5.0    
    def __init__(self, account_number, balance):
        super().__init__(account_number,balance)
        self.account_type = 'Savings Account' 

s = Savings(1231254, 243)
print(s.calc_interest()) # Calc interest on "Savings Account" with APR = 5.0