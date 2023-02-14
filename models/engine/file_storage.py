#!/usr/bin/python3
"""
Contains FileStorage class.
Serializes and deserializes JSON types.
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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
            for key in new_dict:
                self.__objects[key] = classes[
                        new_dict[key]["__class__"]](**new_dict[key])
        except Exception:
            pass
