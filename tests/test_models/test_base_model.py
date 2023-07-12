#!/usr/bin/python3

"""
Unittest for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Defines tests for class BaseModel.
    """

    def setUp(self):
        """
        Set up testing methods.
        """
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """
        Tears down the testing methods.
        """
        del self.base1
        del self.base2

    def test_uuid(self):
        """
        Test that id is a valid uuid.
        """
        test_uuid = uuid.uuid4()
        self.assertIsInstance(test_uuid, uuid.UUID)

    def test_unique_uuid(self):
        """
        Test that the uuid is unique.
        """
        self.assertNotEqual(self.base1.id, self.base2.id)

    def test_created_at(self):
        """
        Test that created_at is a valid datetime.
        """
        self.assertIsInstance(self.base1.created_at, datetime)

    def test_updated_at(self):
        """
        Test that updated_at is a valid datetime.
        """
        self.assertIsInstance(self.base1.updated_at, datetime)

    def test_str(self):
        """
        Test that the str method has the correct output.
        """
        string = "[BaseModel] ({}) {}".format(
            self.base1.id, self.base1.__dict__)
        self.assertEqual(string, str(self.base1))

    def test_save(self):
        """
        Test that save updates the updated_at attribute.
        """
        old_updated_at = self.base1.updated_at
        self.base1.save()
        self.assertNotEqual(old_updated_at, self.base1.updated_at)

    def test_to_dict(self):
        """
        Test that to_dict returns the correct dictionary.
        """
        base1_dict = self.base1.to_dict()
        self.assertIsInstance(base1_dict, dict)
        self.assertIsInstance(base1_dict["id"], str)
        self.assertIsInstance(base1_dict["created_at"], str)
        self.assertIsInstance(base1_dict["updated_at"], str)
        self.assertIsInstance(base1_dict["__class__"], str)
        self.assertEqual(base1_dict["__class__"], "BaseModel")

    def test_to_dict_iso(self):
        """
        Test that to_dict returns the correct dictionary with isoformat.
        """
        base1_dict = self.base1.to_dict()
        self.assertEqual(base1_dict["created_at"],
                         self.base1.created_at.isoformat())
        self.assertEqual(base1_dict["updated_at"],
                         self.base1.updated_at.isoformat())

    def test_to_dict_class(self):
        """
        Test that __class__ is in the dictionary.
        """
        base1_dict = self.base1.to_dict()
        self.assertIn("__class__", base1_dict)

    def test_to_dict_attr(self):
        """
        Test that to_dict has the correct attributes.
        """
        base1_dict = self.base1.to_dict()
        self.assertIn("id", base1_dict)
        self.assertIn("created_at", base1_dict)
        self.assertIn("updated_at", base1_dict)


if __name__ == "__main__":
    unittest.main()
