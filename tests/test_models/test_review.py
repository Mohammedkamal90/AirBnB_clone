#!/usr/bin/python3
"""unittests for class review"""
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """tests for review"""
    @classmethod
    def setUpClass(cls):
        """setup review to test"""
        cls.newreview = Review()
        cls.newreview.place_id = "356987"
        cls.newreview.user_id = "Hali"
        cls.newreview.text = "Place is not clean!"

    @classmethod
    def teardown(cls):
        """deletes the setup review"""
        del cls.newreview

    def tearDown(self):
        """delete"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_review(self):
        """tests for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_review(self):
        """tests for docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """tests attributes"""
        self.assertTrue('id' in self.newreview.__dict__)
        self.assertTrue('created_at' in self.newreview.__dict__)
        self.assertTrue('updated_at' in self.newreview.__dict__)
        self.assertTrue('place_id' in self.newreview.__dict__)
        self.assertTrue('text' in self.newreview.__dict__)
        self.assertTrue('user_id' in self.newreview.__dict__)

    def test_subclass_review(self):
        """tests for inheritance"""
        self.assertTrue(issubclass(self.newreview.__class__, BaseModel), True)

    def test_attr_types_review(self):
        """tests attribute type"""
        self.assertEqual(type(self.newreview.text), str)
        self.assertEqual(type(self.newreview.place_id), str)
        self.assertEqual(type(self.newreview.user_id), str)

    def test_save(self):
        """tests save func"""
        self.newreview.save()
        self.assertNotEqual(self.newreview.created_at,
                            self.newreview.updated_at)

    def test_to_dict(self):
        """test dict"""
        self.assertEqual('to_dict' in dir(self.newreview), True)


if __name__ == "__main__":
    unittest.main()
