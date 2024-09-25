#!/usr/bin/python3
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json


class Testsquare(unittest.TestCase):

    def test_size_initialization(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
    def test_size_x(self):
        square = Square(1, 2)
        self.assertEqual((square.size, square.x), (1, 2))
    def test_square_y(self):
        square = Square(1, 2, 3)
        self.assertEqual((square.size, square.x, square.y), (1, 2, 3))
    def test_size_str(self):
        with self.assertRaises(TypeError):
            Square("1")
    def test_y_str(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
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
        with self.assertRaises(ValueError):
            Square(1, -2)
    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)
    def test_str_method(self):
        square = Square(5, 4, 3, 2)
        exepted_str = "[Square] (2) 4/3 - 5"
        self.assertEqual(str(square), exepted_str)
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
        square.update(6, 1, 1, 5)
        exepect_update = {
            'id': 6,
            'size': 1,
            'x': 1,
            'y': 5
        }
        self.assertEqual(square.to_dictionary(), exepect_update)
    def test_create_id(self):
        square = Square(1, 2, 3)
        square.update(**{ 'id': 89 })
        sq = square.to_dictionary()
        sq2 = square.create(**sq)
        self.assertIsInstance(sq2, Square)
    def test_create_size(self):
        square = Square(1, 2, 3)
        square.update(**{ 'id': 89, 'size': 1 })
        sq = square.to_dictionary()
        sq2 = square.create(**sq)
        self.assertIsInstance(sq2, Square)
    def test_create_x(self):
        square = Square(1, 2, 3)
        square.update(**{ 'id': 89, 'size': 1, 'x': 2 })
        sq = square.to_dictionary()
        sq2 = square.create(**sq)
        self.assertIsInstance(sq2, Square)
    def test_create_y(self):
        square = Square(1, 2, 3)
        square.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        sq = square.to_dictionary()
        sq2 = square.create(**sq)
        self.assertIsInstance(sq2, Square)
    def test_save_to_file_None(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[]')
    def test_save_to_file_empty(self):
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")
    def test_save_to_file_square(self):
        square = Square(1)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            content = file.read()
            list = json.loads(content)
            self.assertEqual(list, [square.to_dictionary()])
    def test_load_from_file(self):
        square = Square(1, 2)
        Square.save_to_file([square])
        loaded_square = Square.load_from_file()
        self.assertTrue(os.path.exists("Square.json"))
        self.assertIsInstance(loaded_square, list)
        self.assertEqual(len(loaded_square), 1)
        self.assertEqual(loaded_square[0].to_dictionary(), square.to_dictionary(),os.remove("Square.json") )
            

if __name__ == "__main__":
    unittest.main()
    