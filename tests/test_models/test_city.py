#!/usr/bin/python3
"""unittests city class"""
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """tests city"""

    @classmethod
    def setUp(cls):
        """creates city to test"""
        cls.testCity = City()
        cls.testCity.name = "Rabat"
        cls.testCity.state_id = "X"

    @classmethod
    def tearDown(cls):
        """deletes the tested city"""
        del cls.testCity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_city(self):
        """tests for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings_city(self):
        """tests for docstrings"""
        self.assertTrue(len(City.__doc__) > 0)
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)

    def test_init_and_class_variables_city(self):
        """tests the init and class variables"""
        self.assertTrue(isinstance(self.testCity, City))
        self.assertTrue(issubclass(type(self.testCity), BaseModel))
        self.assertTrue(self.testCity.name == "test")
        self.assertTrue(self.testCity.state_id == "T")
        self.assertIsNotNone(self.testCity.id)
        self.assertIsNotNone(self.testCity.updated_at)
        self.assertIsNotNone(self.testCity.created_at)

    def test_save_city(self):
        """tests for save func"""
        self.testCity.save()
        self.assertTrue(self.testCity.updated_at != self.testCity.created_at)


if __name__ == '__main__':
    unittest.main()
