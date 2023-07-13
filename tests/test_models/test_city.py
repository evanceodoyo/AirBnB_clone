#!/usr/bin/python3

"""
Defines tests for the City class.
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Tests the City class.
    """

    def test_docstring(self):
        """
        Tests the presence of a docstring.
        """
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """
        Tests the attributes of City.
        """
        base = City()
        base.name = "San Francisco"
        base.state_id = "CA"
        self.assertEqual(base.name, "San Francisco")
        self.assertEqual(base.state_id, "CA")

    def test_inheritance(self):
        """
        Tests inheritance.
        """
        base = City()
        self.assertIsInstance(base, City)
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_to_dict(self):
        """
        Tests to_dict method.
        """
        base = City()
        base.name = "San Francisco"
        base.state_id = "CA"
        base_dict = base.to_dict()
        self.assertEqual(base_dict["name"], "San Francisco")
        self.assertEqual(base_dict["state_id"], "CA")
        self.assertEqual(base_dict["__class__"], "City")


if __name__ == "__main__":
    unittest.main()
