#!/usr/bin/python3
import unittest
from .square import Square


class Testsquare(unittest.TestCase):

    def test_size_initializtion(self):
        square = Square(5)
        self.assertEqual(square.size, 5)