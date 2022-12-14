import unittest

from fraction import Fraction
from fraction import NullDenominatorException
from fraction import ParameterIsNotAFractionException


class TestFraction(unittest.TestCase):
    def test_all_getters_case_success(self):
        """given"""
        expected_numerator = 10
        expected_denominator = 2
        fraction = Fraction(expected_numerator, expected_denominator)

        """when"""
        """event will be called directly in assert"""

        """then"""
        self.assertEqual(expected_numerator, fraction.get_numerator())
        self.assertEqual(expected_denominator, fraction.get_denominator())

    def test_all_getters_default_value_success(self):
        """given"""
        expected_numerator = 1
        expected_denominator = 1
        fraction = Fraction()

        """when"""
        """events will be called directly in assert"""

        """then"""
        self.assertEqual(expected_numerator, fraction.get_numerator())
        self.assertEqual(expected_denominator, fraction.get_denominator())

    def test_constructor_zero_value_denominator_throwException(self):
        """given"""
        expected_numerator = 1
        expected_denominator = 0

        """when"""
        """event will be called directly in assert"""

        """then"""
        with self.assertRaises(NullDenominatorException):
            Fraction(expected_numerator, expected_denominator)

    def test_constructor_float_parameter_success(self):
        """given"""
        given_numerator = 10.00
        expected_numerator = 10
        given_denominator = 2.00
        expected_denominator = 2
        fraction = Fraction(expected_numerator, expected_denominator)

        """when"""
        """events will be called directly in assert"""

        """then"""
        self.assertEqual(expected_numerator, fraction.get_numerator())
        self.assertEqual(expected_denominator, fraction.get_denominator())

    def test_value_nominal_case_success(self):
        """given"""
        numerator = 10
        denominator = 5
        expected_result = 2
        fraction = Fraction(numerator, denominator)

        """when"""
        actual_result = fraction.value()

        """then"""
        self.assertEqual(expected_result, actual_result)

    def test_equal_nominal_case_success(self):
        """given"""
        numerator = 10
        denominator = 5
        fraction = Fraction(numerator, denominator)
        fraction_to_compare = Fraction(numerator, denominator)

        """when"""
        """event will be called directly in assert"""

        """then"""
        self.assertEqual(True, fraction.is_equal(fraction_to_compare))

    def test_equal_parameter_is_not_a_fraction_throwException(self):
        """given"""
        numerator = 10
        denominator = 5
        fraction = Fraction(numerator, denominator)
        fraction_to_compare = 25

        """when"""

        """then"""
        with self.assertRaises(ParameterIsNotAFractionException):
            fraction.is_equal(fraction_to_compare)


if __name__ == '__main__':
    unittest.main()
