#!/usr/bin/python3
"""Unittest for base.py
"""
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """Defines a class to evaluate diferent test cases for base.py file"""

    def test_instance_type_id_class(self):
        """Checks for a instance of the class
        """
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertFalse(type(b1) == type(Base))
        self.assertFalse(id(b1) == id(Base))
        b2 = Base()
        self.assertTrue(type(b1) == type(b2))
        self.assertFalse(id(b1) == id(b2))

    def test_none_id(self):
        """Checks ID assignment when no id is provided"""
        valid_numbers = [1, 2.5, 3j]
        invalid_value = None

        for value in valid_numbers:
            self.assertIsNotNone(value)

    def test_id_value(self):
        """Checks when id has a integer value
        """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b1.id = 4
        self.assertEqual(b1.id, 4)
        b2 = Base(50)
        self.assertEqual(b2.id, 50)
        b1 = Base(-4)
        self.assertEqual(b1.id, -4)
        b2 = Base(0)
        self.assertEqual(b2.id, 0)
        b1 = Base(100e+1000)
        self.assertEqual(b1.id, 100e+1000)
        b1.__init__(30)
        self.assertEqual(b1.id, 30)

