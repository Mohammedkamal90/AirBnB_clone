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


class TestHBNBCommand(unittest.TestCase):
    """tests the HBNBCommand class"""
    def test_emptyline(self):
        """tests for fun emptyline"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("test")
            self.assertEqual("***Unknown syntax: test\n", f.getvalue())

    def test_quit(self):
        """tests for fun quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())
