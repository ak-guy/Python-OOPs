import unittest
from accounts import Accounts
from timezone import TimeZone
from datetime import datetime, timedelta

def run_test(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

class TestAccounts(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone('TZ', 1, 30)
        self.balance = 100.00

    def test_create_account(self):
        a = Accounts(self.account_number, self.first_name, self.last_name, self.tz, self.balance)
        self.assertEqual(self.account_number, a._account_number)
        self.assertEqual(self.first_name, a.first_name)
        self.assertEqual(self.last_name, a.last_name)
        self.assertEqual(self.first_name + ' ' + self.last_name, a.full_name)
        self.assertEqual(self.tz, a.timezone)
        self.assertEqual(self.balance, a._balance)

    def test_create_account_black_first_name(self):
        with self.assertRaises(ValueError): # catching ValueError
            a = Accounts(self.account_number, "", self.last_name, self.tz, self.balance)

    def test_account_deposit_ok(self):
        a = Accounts(self.account_number, self.first_name, self.last_name, self.tz, self.balance)
        conf_code = a.deposit(100)
        self.assertEqual(200, a._balance)
        self.assertIn('D-', conf_code)


run_test(TestAccounts)