#!/usr/bin/python3
# test_base.py
"""Defines unittests for the base.py module.

unittest classes:
    TestBase_instantiation - line 
    TestBase_to_json_string - line 
    TestBase_save_to_file - line 
    TestBase_from_json_string - line 
    TestBase_create - line 
    TestBase_load_from_file - line 
"""
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os
import unittest


class TestBase_instantiation(unittest.TestCase):
    """Unittests for the instantiation of class Base."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

class TestBase_to_json_string(unittest.TestCase):
    """Unittests for to_json_string method in the Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(1, 8, 1, 2, 4)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(12, 9, 7, 8, 9)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def clean(self):
        """Delete created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(11, 1, 1, 2, 4)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(3, 7, 4, 89, 8)
        r2 = Rectangle(2, 3, 4, 6, 9)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)
