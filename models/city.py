#!/usr/bin/python3
"""
This module defines the City class, which inherits from BaseModel.
It represents a city with attributes for state association and city name.
"""
from models.base_model import BaseModel
from models import storage


class City(BaseModel):
    """
    City class that inherits from BaseModel.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        Initialized as an empty string.
        name (str): The name of the city. Initialized as an empty string.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new City instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, used to initialize
                      the object with a dictionary of attributes.

        This method calls the parent class (BaseModel) constructor
        to initialize common attributes such as id, created_at, and updated_at.
        """
        super().__init__(*args, **kwargs)
