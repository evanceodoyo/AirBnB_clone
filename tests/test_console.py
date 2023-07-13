#!/usr/bin/python3

"""
Defines tests for the console (command intepreter).
"""

import os
import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Tests for the console (command interpreter).
    """

    maxDiff = None

    def setUp(self):
        """
        Set up testing environment.
        """
        self.backup = os.path.exists("file.json")
        if os.path.exists("file.json"):
            os.rename("file.json", "file.json.temp")
        with open("file.json", "w") as f:
            f.write("{}")
        self.c = HBNBCommand()

    def tearDown(self):
        """
        Tear down testing environment.
        """
        if self.backup:
            os.remove("file.json")
        else:
            os.rename("file.json.temp", "file.json")
        del self.c

    def test_docstrings_in_console(self):
        """
        Test docstrings.
        """
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_docstrings_in_test_console(self):
        """
        Test docstrings.
        """
        self.assertIsNotNone(TestConsole.__doc__)

    # TODO write more tests
