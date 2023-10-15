#!/usr/bin/python3
"""unittests for amenity class"""
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """tests the Amenity"""

    @classmethod
    def setUpClass(cls):
        """set up amenity to test"""
        cls.lord = Amenity()
        cls.lord.name = "Spa"

    @classmethod
    def teardown(cls):
        """delete what we setup"""
        del cls.lord

    def tearDown(self):
        """delete"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_Amen(self):
        """Tests for the pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_Amen(self):
        """tests for the docstrings"""
        self.assertIsNotNone(self.lord.__doc__)

    def test_attr_Amen(self):
        """tests amenity attibutes"""
        self.assertTrue('id' in self.lord.__dict__)
        self.assertTrue('created_at' in self.lord.__dict__)
        self.assertTrue('updated_at' in self.lord.__dict__)
        self.assertTrue('name' in self.lord.__dict__)

    def test_inheritance_Amen(self):
        """tests inheritance"""
        self.assertTrue(issubclass(self.lord.__class__, BaseModel), True)

    def test_attrtype_Amen(self):
        """tests attribute types"""
        self.assertEqual(type(self.lord.name), str)

    def test_save(self):
        """tests save func"""
        self.lord.save()
        self.assertNotEqual(self.lord.created_at, self.lord.updated_at)

    def test_to_dict(self):
        """tests for dict"""
        self.assertEqual('to_dict' in dir(self.lord), True)


if __name__ == "__main__":
    unittest.main()
