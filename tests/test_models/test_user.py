#!/usr/bin/python3

"""
Tests for the User class.
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test the User class.
    """

    def test_docstring(self):
        """
        Test docstring.
        """
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        """
        Test User attributes.
        """
        base = User()
        base.first_name = "Betty"
        base.last_name = "Bar"
        base.email = "betty@mail.com"
        base.password = "root"
        self.assertEqual(base.first_name, "Betty")
        self.assertEqual(base.last_name, "Bar")
        self.assertEqual(base.email, "betty@mail.com")
        # self.assertEqual(base.password, "root")

    def test_inheritance(self):
        """
        Test inheritance.
        """
        base = User()
        self.assertIsInstance(base, User)
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_to_dict(self):
        """
        Test to_dict method.
        """
        base = User()
        base.first_name = "Betty"
        base.last_name = "Bar"
        base.email = "betty@mail.com"
        base.password = "root"
        base_dict = base.to_dict()
        self.assertEqual(base_dict["first_name"], "Betty")
        self.assertEqual(base_dict["last_name"], "Bar")
        self.assertEqual(base_dict["email"], "betty@mail.com")
        # self.assertEqual(base_dict["password"], "root")
        self.assertEqual(base_dict["__class__"], "User")

    def test_str(self):
        """
        Test __str__ method.
        """
        base = User()
        string = "[User] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(string, str(base))

    def test_save(self):
        """
        Test save method.
        """
        base = User()
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)
