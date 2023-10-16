#!/usr/bin/python3
"""unittests for class state"""
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """tests state"""

    @classmethod
    def setUpClass(cls):
        """set up a state"""
        cls.state = State()
        cls.state.name = "LA"

    @classmethod
    def teardown(cls):
        """deletes state after test"""
        del cls.state

    def tearDown(self):
        """delete"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_stat(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_stat(self):
        """tests docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_attr_stat(self):
        """tests existance of keys"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_inheritance_stat(self):
        """tests inheritance"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attrtype_stat(self):
        """tests attribute type"""
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        """tests save func"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """tests dict"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
