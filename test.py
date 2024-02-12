import unittest
from fractions import Fraction
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        expected_result = 6
        result = custom_sum(data)
        self.assertEqual(result, expected_result, f"Expected {expected_result}, but got {result}")

if __name__ == '__main__':
    unittest.main()


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        expected_result = 6
        result = custom_sum(data)
        self.assertEqual(result, expected_result, f"Expected {expected_result}, but got {result}")

    def test_float_values(self):
        """
        Test that it handles summing floating-point values
        """
        data = [1/4, 1/4, 2/5]
        expected_result = 1
        result = custom_sum(data)
        self.assertEqual(result, expected_result, f"Expected {expected_result}, but got {result}")

if __name__ == '__main__':
    unittest.main()
