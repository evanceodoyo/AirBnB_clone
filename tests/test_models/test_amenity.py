#!/usr/bin/python3

"""
Defines tests for the Amenity class.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Tests the Amenity class.
    """

    def test_docstring(self):
        """
        Tests the presence of a docstring.
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        """
        Tests the attributes of Amenity.
        """
        base = Amenity()
        base.name = "Amenity Name"
        self.assertEqual(base.name, "Amemity Name")

    def test_inheritance(self):
        """
        Tests inheritance.
        """
        base = Amenity()
        self.assertIsInstance(base, Amenity)
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_to_dict(self):
        """
        Tests to_dict method.
        """
        base = Amenity()
        base.name = "Amenity Name"
        base_dict = base.to_dict()
        self.assertEqual(base_dict["name"], "Amenity Name")
        self.assertEqual(base_dict["__class__"], "Amenity")


if __name__ == "__main__":
    unittest.main()
