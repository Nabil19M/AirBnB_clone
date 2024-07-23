#!/usr/bin/python3
"""
This module defines the BaseModel class, which serves as the foundation
for all other models in the application. It provides common attributes
and methods for object serialization, deserialization, and management.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class provides common attributes and methods for other classes.

    Attributes:
        id (str): A unique identifier for each instance, generated using UUID.
        created_at (datetime): The timestamp when an instance is created.
        updated_at (datetime): The timestamp when an instance is last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, used to initialize
                      the object with a dictionary of attributes.

        If kwargs is provided, it initializes the instance with the
        attributes found in the dictionary, including handling the
        conversion of string dates to datetime objects. Otherwise,
        it generates a new id and sets the creation and update timestamps.
        """
        from models import storage

        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    pass
                elif k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance.

        Returns:
            str: A string in the format:
            [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with
        the current datetime and saves the instance to storage.

        This method calls the storage.save() method to persist the changes.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of the instance's __dict__.

        The dictionary includes a key '__class__'
        with the class name of the object
        and converts created_at and updated_at to ISO format strings.

        Returns:
            dict: A dictionary representation of the instance.
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
