#!/usr/bin/python3
""" importing required models """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
""" Defining File storage class to opertate the saving and retreiveing objects
    by json files
"""


class FileStorage:
    """Defining FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retreive all objects in the storage

        Returns:
            __dicttionary: all objects types BaseModel, user...etc
        """
        return FileStorage.__objects

    def new(self, obj):
        """add new object to storage dictionary by type of class and id
        Ex: User 1234-1334-1234-124

        Args:
            obj (_object_): object should be added
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict()
                    for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as myjsonfile:
            json.dump(obj_dict, myjsonfile)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
          (__file_path) exists; otherwise, do nothing)"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls = value['__class__']
                    self.new(eval(cls)(**value))
        except Exception:
            pass
