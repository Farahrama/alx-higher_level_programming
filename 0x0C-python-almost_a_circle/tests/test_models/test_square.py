#!/usr/bin/python3
from models.square import Square
import unittest


class Testsquare(unittest.TestCase):

    def test_size_initialization(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
    def test_set_size(self):
        square = Square(6)
        self.assertEqual(square.size, 6)
    def test_str_set(self):
        with self.assertRaises(TypeError):
            Square(1, "3")
    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-6)
    def test_initialization(self):
        init = Square(1, 2, 3, 4)
        self.assertEqual((init.size, init.x, init.y, init.id), (1, 2, 3, 4))
    def test_negative_x(self):
        with self.assertRaises(TypeError):
            Square(1, -2)
    def test_negative_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, -3)
    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)
    def test_str_method(self):
        Square(5, 4, 3, 2)
        exepted_str = "[Square] (2) 4/3 - 5"
        self.assertEqual(str(Square), exepted_str)
    def test_to_dictionary(self):
        square = Square(8, 16, 5, 6)
        expected_dictionary = {
            'id': 6,
            'size': 8,
            'x': 16,
            'y': 5
        }
        self.assertEqual(square.to_dictionary(), expected_dictionary)
    def test_update(self):
        square = Square(8, 16, 5, 6)
        square.update(1, 1, 5, 6)
        exepect_update = {
            'id': 6,
            'size': 1,
            'x': 1,
            'y': 5
        }
        self.assertEqual(square.to_dictionary, exepect_update)

if __name__ == "__main__":
    unittest.main()
    