"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10, 9)
        self.assertEqual(res, 1)

    def test_multiplicating_numbers(self):
        """Test multiplicating numbers"""
        res = calc.multiply(10, 10)
        self.assertEqual(res, 100)

    def test_dividing_numbers(self):
        """Test dividing numbers"""
        res = calc.divide(100, 10)
        self.assertEqual(res, 10)
