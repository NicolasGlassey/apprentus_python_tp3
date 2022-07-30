import unittest

from fraction import FractionError
from fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_getters_numerator_nominal_case_success(self):
        """given"""
        expected_numerator = 10;
        expected_denominator = 2;
        fraction = Fraction(10, 2)

        """when"""

        """then"""
        self.assertEqual(expected_numerator, fraction.get_numerator())
        self.assertEqual(expected_denominator, fraction.get_denominator())

if __name__ == '__main__':
    unittest.main()
