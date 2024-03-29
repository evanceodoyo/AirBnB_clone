#!/bin/usr/python3

"""
Defines the City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city (within a state).
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new City.
        """
        super().__init__(*args, **kwargs)
