#!/usr/bin/python3
"""
This module defines the Amenity class, which inherits from BaseModel.
It represents an amenity with attributes for naming the amenity.
"""
from models.base_model import BaseModel
from models import storage


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.

    Attributes:
        name (str): The name of the amenity. Initialized as an empty string.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Amenity instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, used to initialize
                      the object with a dictionary of attributes.

        This method calls the parent class (BaseModel)
        constructor to initialize
        common attributes such as id, created_at, and updated_at.
        """
        super().__init__(*args, **kwargs)
