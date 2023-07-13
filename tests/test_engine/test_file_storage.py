#!/usr/bin/python3

"""
Unittest for FileStorage class.
"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Defines tests for class FileStorage.
    """

    def setUp(self):
        """
        Set up testing methods.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Tears down the testing methods.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        del self.storage

    def test_all(self):
        """
        Test that all returns the __objects attribute.
        """
        self.assertIs(self.storage.all(), self.storage._FileStorage__objects)

    def test_new(self):
        """
        Test that new adds an object to the __objects attribute.
        """
        base = BaseModel()
        key = "{}.{}".format(base.__class__.__name__, base.id)
        self.storage.new(base)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """
        Test that save properly saves objects to file.json.
        """
        base = BaseModel()
        base.save()
        with open("file.json", "r") as f:
            self.assertIn(base.id, f.read())

    def test_reload(self):
        """
        Test that reload properly loads objects from file.json.
        """
        base = BaseModel()
        base.save()
        self.storage.reload()
        key = "{}.{}".format(base.__class__.__name__, base.id)
        self.assertIn(key, self.storage.all())

    # def test_reload_no_file(self):
    #     """
    #     Test that reload does not fail if file.json does not exist.
    #     """
    #     self.storage.reload()
    #     self.assertEqual(self.storage.all(), {})

    # def test_reload_empty_file(self):
    #     """
    #     Test that reload does not fail if file.json is empty.
    #     """
    #     with open("file.json", "w") as f:
    #         f.write("")
    #     self.storage.reload()
    #     self.assertEqual(self.storage.all(), {})


if __name__ == "__main__":
    unittest.main()
