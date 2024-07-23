#!/usr/bin/python3
"""
This module defines the Review class, which inherits from BaseModel.
It is designed to represent a review for a place, containing attributes
for the place, user, and review text.
"""
from models.base_model import BaseModel
from models import storage


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Review instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, used to initialize
                      the object with a dictionary of attributes.

        This method calls the parent class (BaseModel) constructor
        to initializecommon attributes
        such as id, created_at, and updated_at.
        """
        super().__init__(*args, **kwargs)
