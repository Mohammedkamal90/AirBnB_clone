#!/usr/bin/python3
"""unittests the basemodels class"""
import unittest
import os
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """tests for basemodel"""
    @classmethod
    def setUpClass(cls):
        """sets up BaseModel to test"""
        cls.testBase = BaseModel()
        cls.testBase.x = "x"
        cls.testBase.y = 100

    @classmethod
    def tearDownClass(cls):
        """deletes the BaseMosel we set up"""
        del cls.testBase
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_basemodel(self):
        """tests for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_check_functions(self):
        """tests func"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attribute_basemodel(self):
        """tests attributes"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """tests init"""
        self.assertTrue(isinstance(self.testBase, BaseModel))

    def test_save(self):
        """tests save"""
        self.testBase.save()
        self.assertNotEqual(self.testBase.created_at, self.testBase.updated_at)

    def test_to_dict(self):
        """tests dict"""
        copy = self.testBase.to_dict()
        self.assertEqual(self.testBase.__class__.__name__, 'BaseModel')
        self.assertIsInstance(copy['created_at'], str)
        self.assertIsInstance(copy['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
