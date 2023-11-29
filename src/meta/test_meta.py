import unittest
from parameterized import parameterized
from meta.covid_seating import getMaxAdditionalDinersCount, seats_available_between

class CovidSeatingTestCase(unittest.TestCase):
    @parameterized.expand([
        ('10-1-2', (10, 1, 2, [2,6]), 3),
        ('3-1-2', (3, 1, 2, [0,2]), 0),
        ('6-2-2' ,(6, 2, 2, [0,5]), 0),
        ('3-1-0' ,(3, 1, 0, []), 2),
        ('6-1-0' ,(6, 1, 0, []), 3),
        ('15-2-3' ,(15, 2, 3, [11, 6, 14]), 1),
        ('16-2-3' ,(16, 2, 3, [6, 9, 15]), 2),
    ])
    def test_getMaxAdditionalDinersCount(self, _, args, expected):
        self.assertEqual(getMaxAdditionalDinersCount(*args),  expected)

    @parameterized.expand([
        ('0_4_1', (0,4,1), 1),
        ('N3_1_1', (-3,1,1), 1),
        ('N3_3_2', (-3,3,2), 1),
        ('2_11_2', (2,11,2), 2)
    ])
    def test_seats_available_between(self, _, args, expected):
        self.assertEqual(seats_available_between(*args), expected)
