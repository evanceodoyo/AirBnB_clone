#!/usr/bin/python3
"""
Contains FileStorage class.
Serializes and deserializes JSON types.
"""

import json
from hashlib import md5

classes = {}


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes \
    JSON file to instances.
    """

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """
        Returns the  dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file \
        (__file_path) exists; otherwise, do nothing.
        """
        try:
            with open(self.__file_path, 'r') as f:
                new_dict = json.load(f)
            for value in new_dict.values():
                cls = value["__class__"]
                self.new(eval(cls)(**value))
        except Exception:
            pass
