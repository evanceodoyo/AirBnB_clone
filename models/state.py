#!/bin/usr/python3

"""
Defines the State class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state.
    Attributes:
        name (str): The state's name.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new State.
        """
        super().__init__(*args, **kwargs)
