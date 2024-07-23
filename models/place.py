#!/usr/bin/python3
"""
This module defines the Place class, which inherits from BaseModel.
It is designed to represent a property or accommodation with various
attributes such as location, description, and pricing.
"""
from models.base_model import BaseModel
from models import storage


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
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
        Initializes a new Place instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, used to initialize
                      the object with a dictionary of attributes.

        This method calls the parent class (BaseModel) constructor
        to initialize common attributes
        such as id, created_at, and updated_at.
        """
        super().__init__(*args, **kwargs)
