#!/usr/bin/python3
"""
This module defines the State class, which inherits from BaseModel.
It represents a geographical state with a name attribute.
"""
from models.base_model import BaseModel
from models import storage


class State(BaseModel):
    """
    State class that inherits from BaseModel.

    Attributes:
        name (str): The name of the state.
        Initialized as an empty string.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new State instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, used to initialize
                      the object with a dictionary of attributes.

        This method calls the parent class (BaseModel) constructor
        to initialize common attributes
        such as id, created_at, and updated_at.
        """
        super().__init__(*args, **kwargs)
