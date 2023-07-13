#!/usr/bin/python3

"""
Defines the User class.
"""

import hashlib
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user for a MySQL database.
    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.

    Methods:
        __init__: Initializes a new User.
        __setattr__: Set a password with md5 encryption.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User.
        """
        super().__init__(*args, **kwargs)

    # def __setattr__(self, name, value):
    #     """
    #     Set a password with md5 encryption.
    #     """
    #     if name == "password":
    #         value = hashlib.md5(value.encode()).hexdigest()
    #     super().__setattr__(name, value)
