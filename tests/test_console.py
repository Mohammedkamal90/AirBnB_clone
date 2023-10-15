#!/usr/bin/python3
"""unittest for console.py"""
import unittest
from unittest import patch
from io import StringIO
import os
import pep8
import tests
import console
from Console import HBNBCommand


class TestConsole(unittest.TestCase):
    """tests the console"""
    @classmethod
    def setUpClass(cls):
        """setup console class to test"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """deletes what we setup"""
        del cls.consol

    def tearDown(self):
        """delete"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """tests for Pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docstrings_console(self):
        """tests for doc strings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """tests empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("test")
            self.assertEqual("*** Unknown syntax: test\n", f.getvalue())

    def test_quit(self):
        """tests quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())

if __name__ == '__main__':
    unittest.main()
