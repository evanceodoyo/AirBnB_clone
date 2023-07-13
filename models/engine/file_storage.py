#!/usr/bin/python3

"""
Contains the FileStorage class.
Serializes instances to a JSON file and deserializes JSON file to instances.
Ensures persistence of an object's data between program execution.
"""

import json
from models.base_model import BaseModel
from models.user import User

models = {"BaseModel": BaseModel, "User": User}


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to\
        instances.
    Ensures persistence of an object's data between program execution.

    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): empty but will store all objects by <class name>.id.

    Methods:
        all: returns the dictionary __objects.
        new: sets in __objects the obj with key <obj class name>.id.
        save: serializes __objects to the JSON file (path: __file_path).
        reload: deserializes the JSON file to __objects (only if the JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised).
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                class_name = value["__class__"]
                del value["__class__"]
                self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
