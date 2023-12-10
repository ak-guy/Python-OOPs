import unittest
from timezone import TimeZone
from datetime import datetime, timedelta

def run_test(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

class TestTimeZone(unittest.TestCase):
    def test_create_timezone(self):
        tz = TimeZone('IST', 5, 30)
        self.assertEqual('IST', tz._name)
        self.assertEqual(timedelta(hours=5, minutes=30), tz.offset)

    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)

    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)
        
        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )
        for test_tz in test_timezones:
            self.assertNotEqual(tz, test_tz)


run_test(TestTimeZone)