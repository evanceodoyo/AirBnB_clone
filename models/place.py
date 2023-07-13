#!/usr/bin/python3

"""
Defines the Place class.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place.
    Attributes:
        city_id (str): The place's city id.
        user_id (str): The place's user id.
        name (str): The place's name.
        description (str): The place's description.
        number_rooms (int): The number of rooms the place has.
        number_bathrooms (int): The number of bathrooms the place has.
        max_guest (int): The maximum number of guests the place can hold.
        price_by_night (int): The price by night for the place.
        latitude (float): The place's latitude.
        longitude (float): The place's longitude.
        amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Place.
        """
        super().__init__(*args, **kwargs)
