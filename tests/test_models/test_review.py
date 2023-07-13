#!/usr/bin/python3

"""
Defines tests for the Review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Tests the Review class.
    """

    def test_docstring(self):
        """
        Tests the presence of a docstring.
        """
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """
        Tests the attributes of Review.
        """
        base = Review()
        base.place_id = "00012"
        base.user_id = "123-123"
        base.text = "Review Text"
        self.assertEqual(base.place_id, "00012")
        self.assertEqual(base.user_id, "123-123")
        self.assertEqual(base.text, "Review Text")

    def test_inheritance(self):
        """
        Tests inheritance.
        """
        base = Review()
        self.assertIsInstance(base, Review)
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_to_dict(self):
        """
        Tests to_dict method.
        """
        base = Review()
        base.place_id = "00012"
        base.user_id = "123-123"
        base.text = "Review Text"
        base_dict = base.to_dict()
        self.assertEqual(base_dict["place_id"], "00012")
        self.assertEqual(base_dict["user_id"], "123-123")
        self.assertEqual(base_dict["text"], "Review Text")
        self.assertEqual(base_dict["__class__"], "Review")


if __name__ == "__main__":
    unittest.main()
