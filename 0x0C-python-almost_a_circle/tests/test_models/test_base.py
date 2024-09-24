#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_auto_assignment(self):
        base = Base()
        self.assertEqual(base.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
    def test_id_manual_assignment(self):
        base = Base(50)
        self.assertEqual(base.id, 50)
    def test_to_json_string_None_list(self):
        self.assertEqual(Base.to_json_string(None), "[]")
    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")
    def test_to_json_string_valid(self):
        dictionary = [{"id": 12}]
        self.assertEqual(Base.to_json_string(dictionary), '[{"id": 12}]')
    def test_from_json_string_None(self):
        self.assertEqual(Base.from_json_string(None), [])
    def test_from_json_string_empty_list(self):
        dictionary = []
        self.assertEqual(Base.from_json_string(dictionary), [])
    def test_from_json_string_normaltest(self):
        dictionary = [{"id": 12}]
        dict = '[{"id": 12}]'
        self.assertEqual(Base.from_json_string(dict), dictionary)
if __name__ == "__main__":
    unittest.main()