#!/usr/bin/python3
"""
Base class for the AirBnB project models.
"""

from uuid import uuid4
from datetime import datetime
# import models


class BaseModel:
    """Custom base model for the AirBnB project.

    Attributes:
      id(str): unique user identity. Created using uuid.
      created_at: datetime when the object is created.
      updated_at: datetime when the object is updated.

    Methods:
      __str__: prints class name, id, and creates a dictionary
      representation of the input values.
      save: updates instance attributes with current datetime.
      to_dict: returns the dictionary values of the  instance object.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the instance attributes on creation.

        Args:
          *args(args): arguments
          **kwargs(dict): keyword args[attribute values]
        """
        DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                        kwargs["created_at"], DATE_TIME_FORMAT)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                        kwargs["updated_at"], DATE_TIME_FORMAT)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id") is None:
                self.id = str(uuid4())

    def __str__(self):
        """
        Returns string representation of the class.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute 'updated_at'\
        with the current datetime.
        """
        self.updated_at = datetime.utcnow()
        # models.storage.new(self)
        # models.storage.save()

    def to_dict(self):
        """
        Returns dictionary with all key-value pairs
        of __dict__ instance.
        """
        obj_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
