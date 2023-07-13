#!/usr/bin/python3

"""
Defines tests for the Place class.
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Tests the Place class.
    """

    def test_docstring(self):
        """
        Tests the presence of a docstring.
        """
        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        """
        Tests the attributes of Place.
        """
        base = Place()
        base.city_id = "0001"
        base.user_id = "0001"
        base.name = "The awesome house"
        base.description = "The awesome house is warm and cozy."
        base.number_rooms = 4
        base.number_bathrooms = 2
        base.max_guest = 10
        base.price_by_night = 300
        base.latitude = 37.773972
        base.longitude = -122.431297
        base.amenity_ids = ["0001", "0002"]
        self.assertEqual(base.city_id, "0001")
        self.assertEqual(base.user_id, "0001")
        self.assertEqual(base.name, "The awesome house")
        self.assertEqual(base.description,
                         "The awesome house is warm and cozy.")
        self.assertEqual(base.number_rooms, 4)
        self.assertEqual(base.number_bathrooms, 2)
        self.assertEqual(base.max_guest, 10)
        self.assertEqual(base.price_by_night, 300)
        self.assertEqual(base.latitude, 37.773972)
        self.assertEqual(base.longitude, -122.431297)
        self.assertEqual(base.amenity_ids, ["0001", "0002"])

    def test_inheritance(self):
        """
        Tests inheritance.
        """
        base = Place()
        self.assertIsInstance(base, Place)
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_to_dict(self):
        """
        Tests to_dict method.
        """
        base = Place()
        base.city_id = "0001"
        base.user_id = "0001"
        base.name = "The awesome house"
        base.description = "The awesome house is warm and cozy."
        base.number_rooms = 4
        base.number_bathrooms = 2
        base.max_guest = 10
        base.price_by_night = 300
        base.latitude = 37.773972
        base.longitude = -122.431297
        base.amenity_ids = ["0001", "0002"]
        base_dict = base.to_dict()
        self.assertEqual(base_dict["city_id"], "0001")
        self.assertEqual(base_dict["user_id"], "0001")
        self.assertEqual(base_dict["name"], "The awesome house")
        self.assertEqual(base_dict["description"],
                         "The awesome house is warm and cozy.")
        self.assertEqual(base_dict["number_rooms"], 4)
        self.assertEqual(base_dict["number_bathrooms"], 2)
        self.assertEqual(base_dict["max_guest"], 10)
        self.assertEqual(base_dict["price_by_night"], 300)
        self.assertEqual(base_dict["latitude"], 37.773972)
        self.assertEqual(base_dict["longitude"], -122.431297)
        self.assertEqual(base_dict["amenity_ids"], ["0001", "0002"])
        self.assertEqual(base_dict["__class__"], "Place")


if __name__ == "__main__":
    unittest.main()
