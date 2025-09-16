import unittest
from adder import add_numbers

class TestAdder(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-3, -5), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add_numbers(-3, 5), 2)

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 5), 5)

if __name__ == "__main__":
    unittest.main()
