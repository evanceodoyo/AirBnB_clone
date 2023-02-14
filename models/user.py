#!/usr/bin/python3

"""
Defines the User class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes user.
        """
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """
        Sets a password with md5 encryption.
        """
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
