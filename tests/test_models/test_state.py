#!/usr/bin/python3

"""
Defines tests for the State class.
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Tests the State class.
    """

    def test_docstring(self):
        """
        Tests the presence of a docstring.
        """
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """
        Tests the attributes of State.
        """
        base = State()
        base.name = "California"
        self.assertEqual(base.name, "California")

    def test_inheritance(self):
        """
        Tests inheritance.
        """
        base = State()
        self.assertIsInstance(base, State)
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_to_dict(self):
        """
        Tests to_dict method.
        """
        base = State()
        base.name = "California"
        base_dict = base.to_dict()
        self.assertEqual(base_dict["name"], "California")
        self.assertEqual(base_dict["__class__"], "State")


if __name__ == "__main__":
    unittest.main()
