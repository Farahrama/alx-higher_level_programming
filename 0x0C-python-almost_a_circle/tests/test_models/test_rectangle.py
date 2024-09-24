#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    def test_initialization(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual((rectangle.width, rectangle.height), (3, 4))
    def test_set_x(self):
        rectangle = Rectangle(1, 2, 3)
        self.assertEqual((rectangle.width, rectangle.height, rectangle.x), (1, 2, 3))
    def test_set_y(self):
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual((rectangle.width, rectangle.height,\
                rectangle.x, rectangle.y), (1, 2, 3, 4))
    def test_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
    def test_str_width(self):
        with self.assertRaises(TypeError):
            Rectangle("2", 2)
    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-2, 2)
    def test_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -1)
    def test_str_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "1")
    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
    def test_str_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
    def test_str_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
    def test_area(self):
        rectangle = Rectangle(4, 2)
        self.assertEqual(rectangle.area(), 8)
    def test_str_(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        excepted_str = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(rectangle.__str__(), excepted_str)
    def test_display_None(self):
        rectangle = Rectangle(1, 2)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), "#\n#\n")
    def test_display_without_y(self):
        rectangle = Rectangle(1, 2, 3)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), "   #\n   #\n")
    def test_to_dictionary(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        dict_rectangle = {
            'id': 5,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4
            }
        self.assertEqual(rectangle.to_dictionary(), dict_rectangle)
    def test_update(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle.update(), None)
    def test_update_id(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(89)
        dict_rectangle = {
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4
            }
        self.assertEqual(rectangle.to_dictionary(), dict_rectangle)
    def test_update_width(self):
        rectangle = Rectangle(10, 2, 3, 4, 5)
        rectangle.update(89, 1)
        dict_rectangle = {
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4
            }
        self.assertEqual(rectangle.to_dictionary(), dict_rectangle)
    def test_update_height(self):
        rectangle = Rectangle(10, 12, 3, 4, 5)
        rectangle.update(89, 1, 2)
        dict_rectangle = {
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4
            }
        self.assertEqual(rectangle.to_dictionary(), dict_rectangle)
    def test_update_x(self):
        rectangle = Rectangle(10, 12, 13, 4, 5)
        rectangle.update(89, 1, 2, 3)
        dict_rectangle = {
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4
            }
        self.assertEqual(rectangle.to_dictionary(), dict_rectangle)
    def test_update_y(self):
        rectangle = Rectangle(10, 12, 13, 14, 5)
        rectangle.update(89, 1, 2, 3, 4)
        dict_rectangle = {
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4
            }
        self.assertEqual(rectangle.to_dictionary(), dict_rectangle)
    def test_update_idk(self):
        rectangle = Rectangle(10, 12, 13, 14, 5)
        rectangle.update(**{ 'id': 89 })
        dict_rectangle = {
            'id': 89,
            'width': 10,
            'height': 12,
            'x': 13,
            'y': 14
            }
        self.assertEqual(rectangle.to_dictionary(), dict_rectangle)
    def test_update_widthk(self):
        rectangle = Rectangle(10, 12, 13, 14, 5)
        rectangle.update(**{ 'id': 89, 'width': 1 })
        dict_rectangle = {
            'id': 89,
            'width': 1,
            'height': 12,
            'x': 13,
            'y': 14
            }
        self.assertEqual(rectangle.to_dictionary(), dict_rectangle)
    def test_update_heightk(self):
        rectangle = Rectangle(10, 12, 13, 14, 5)
        rectangle.update(**{ 'id': 89, 'width': 1, 'height': 2 })
        dict_rectangle = {
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 13,
            'y': 14
            }
        self.assertEqual(rectangle.to_dictionary(), dict_rectangle)
    def test_update_xk(self):
        rectangle = Rectangle(10, 12, 13, 14, 5)
        rectangle.update(**{ 'id': 89, 'width': 1, 'height': 2 , 'x': 3})
        dict_rectangle = {
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 14
            }
        self.assertEqual(rectangle.to_dictionary(), dict_rectangle)
    def test_update_yk(self):
        rectangle = Rectangle(10, 12, 13, 14, 5)
        rectangle.update(**{ 'id': 89, 'width': 1, 'height': 2 , 'x': 3, 'y': 4})
        dict_rectangle = {
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4
            }
        self.assertEqual(rectangle.to_dictionary(), dict_rectangle)
    
        
        
if __name__ == '__main__':
    unittest.main()