"""
Sample Test
"""

from django.test import SimpleTestCase

from app import cal


class CalcTests(SimpleTestCase):
    """Test the cal module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = cal.add(5, 5)

        self.assertEqual(res, 10)

    def test_substract_numbers(self):
        """Test substracting numbers"""

        res = cal.subtract(10, 5)
        self.assertEqual(res, 5)
