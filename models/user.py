#!/usr/bin/python3
"""
This module defines the User class, which inherits from BaseModel.
It is designed to represent a user with specific attributes such as
email, password, first_name, and last_name.
"""
from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically used to initialize
                      the object with a dictionary of attributes.

        This method calls the parent class (BaseModel) constructor
        to initialize common attributes
        such as id, created_at, and updated_at.
        """
        super().__init__(*args, **kwargs)
