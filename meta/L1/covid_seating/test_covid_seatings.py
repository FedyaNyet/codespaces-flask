import unittest
from parameterized import parameterized
from .covid_seating import getMaxAdditionalDinersCount

class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        ('10-1-2', (10, 1, 2, [2,6]), 3),
        ('3-1-2', (3, 1, 2, [0,2]), 0),
        ('6-2-2' ,(6, 2, 2, [0,5]), 0),
        ('3-1-0' ,(3, 1, 0, []), 2),
        ('6-1-0' ,(6, 1, 0, []), 3),
        ('15-2-3' ,(15, 2, 3, [11, 6, 14]), 1),
        ('16-2-3' ,(16, 2, 3, [6, 9, 15]), 2),
    ])
    def test_invalid_input(self, _, args, expected):
        self.assertEqual(getMaxAdditionalDinersCount(*args),  expected)
