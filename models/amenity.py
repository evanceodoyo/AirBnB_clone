#!/bin/usr/python3

"""
Defines the Amenity class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity (within a place).
    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Amenity.
        """
        super().__init__(*args, **kwargs)
