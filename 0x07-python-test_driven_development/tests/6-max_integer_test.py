#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_max_at_start(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)
    def test_max_one_negative(self):
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
    def test_max_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    def test_max_empty(self):
        self.assertEqual(max_integer([]), None)
    def test_max_floats(self):
        self.assertEqual(max_integer([1.2, 2.3, 3.4, 3.9]), 3.9)
    def test_max_one_element(self):
        self.assertEqual(max_integer([5]), 5)


if __name__ == "__main__":
    unittest.main()

