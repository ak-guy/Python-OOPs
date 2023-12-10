from timezone import TimeZone
from helper import generateTransactionIds
import random
import numbers
from datetime import datetime
from collections import namedtuple

Confirmation = namedtuple('Confirmation', 'account_number, transaction_code, transaction_id, time_utc, time')

class Accounts:
    transaction_counter = generateTransactionIds(100)
    _MIR = 0.05 # monthly interest rate 5%
    _TRANSACTION_CODES = {
        'Deposit': 'D',
        'Withdraw': 'W',
        'Interest': 'I',
        'Rejected': 'X'
    }

    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)
        self.timezone = timezone

        self._balance = float(initial_balance)
    
    @property
    def timezone(self):
        return self._timezone
    
    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Timezone must be valid TimeZone object')
        self._timezone = value
    
    # read-only
    @property
    def account_number(self):
        return self._account_number
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self,value):
        self._first_name = Accounts.validateName(value, 'First Name')
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self,value):
        self._last_name = Accounts.validateName(value, 'Last Name')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    # making balance read-only
    @property
    def initial_balance(self):
        return self._balance
        
    @staticmethod
    def validateName(value, field_title):
        if not isinstance(value,str) or len(str(value.strip())) == 0 or value is None:
            raise ValueError(f"{field_title} must be a non-empty and valid string")
        return str(value).strip()
        
    @classmethod
    def getInterestRate(cls):
        return cls._MIR
    
    @classmethod
    def setInterestRate(cls, value):
        if not isinstance(value,numbers.Real):
            raise ValueError('Interest Rate must be real value')
        if value < 0:
            raise ValueError('Interest Rate cannot be negative')
        cls._MIR = value 

    @staticmethod
    def validate_amount(value, min_val=None):
        if not isinstance(value, numbers.Real):
            raise ValueError('Amount should be real')
        
        if min_val is not None and value < min_val:
            raise ValueError(f'Amount must be atleast {min_val}')
        
        return value

    
    # dummy-A100-20190325224918-101
    def generate_confirmation_code(self, transaction_code):
        modified_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}-{self.account_number}-{modified_time}-{next(Accounts.transaction_counter)}'
    
    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
        parts = confirmation_code.split('-')
        if len(parts) != 4:
            raise ValueError('Invalid Confirmation code')
        transaction_code, account_number, raw_time_utc, transaction_id = parts
        try:
            time_utc = datetime.strptime(raw_time_utc, '%Y%m%d%H%M%S')
        except ValueError as e:
            raise ValueError('Date Time format is incorrect') from e
        
        if preferred_time_zone is None:
            preferred_time_zone = TimeZone('UTC', 0, 0)
        
        if not isinstance(preferred_time_zone, TimeZone):
            raise ValueError('Invalid time zone defined')
        
        preffered_time = time_utc + preferred_time_zone.offset
        preffered_time_str = f"{preffered_time.strftime('%Y%m%d%H%M%S')} ({preferred_time_zone.name})"
        return Confirmation(account_number, transaction_id, transaction_code, raw_time_utc, preffered_time_str)
    
    def deposit(self, value):
        value = Accounts.validate_amount(value, 0.01)
        
        conf_code = self.generate_confirmation_code(Accounts._TRANSACTION_CODES['Deposit'])
        self._balance += value
        return conf_code

    def withdraw(self, value):
        value = Accounts.validate_amount(value, 0.01)
        
        withdraw_accepted = False
        if self._balance - value < 0:
            transaction_code = Accounts._TRANSACTION_CODES['Rejected']
        else:
            withdraw_accepted = True
            transaction_code = Accounts._TRANSACTION_CODES['Withdraw']

        conf_code = self.generate_confirmation_code(transaction_code)
        if withdraw_accepted:
            self._balance -= value
        
        return conf_code

    def addInterest(self):
        conf_code = self.generate_confirmation_code(Accounts._TRANSACTION_CODES['Interest'])
        self._balance *= (1 + Accounts.getInterestRate())
        return conf_code

if __name__ == '__main__':
    account_no = ''.join(str(random.randint(0,9)) for i in range(0,6))
    a = Accounts('A100', 'Eric', 'Idle', timezone=TimeZone('MST', -7, 0), initial_balance=100)
    print(a._balance)
    print(a.deposit(150.02))
    print(a._balance)
    print(a.withdraw(0.02))
    print(a._balance)
    Accounts.setInterestRate(0.01)
    print(a.getInterestRate())
    print(a.addInterest())
    print(a._balance)
    print(a.withdraw(1000))