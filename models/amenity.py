#!/usr/bin/python3
"""
Contains the class Amenity.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Custom amenity class.

    Attributes:
        name(str): amenity name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Amenity
        """
        super().__init__(*args, **kwargs)
