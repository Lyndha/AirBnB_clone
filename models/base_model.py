#!/usr/bin/python3
"""
base_model module: contains a class `BaseModel` that defines all common
attributes/methods for other classes

You can also test file by file by using this command:
python3 -m unittest tests/test_models/test_base_model.py
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """
    BaseModel class: defines all common attributes/methods for other classes

    Methods:
        __init__: instantialization

        __str__: return an informal string representation of an instance

        save: updates the public instance attribute `updated_at` with
        the current datetime

        to_dict: returns a dictionary containing all keys/values of
        __dict__ of the instance
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance

        Args:
            id: (string) - assign with an uuid when an instance is created

            created_at: (datetime) - assign with the current datetime
            when an instance is created

            updated_at: (datetime) - assign with the current datetime when an
            instance is created and it will be updated every time you change
            your object
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        return an informal string representation of an instance

        Return:
            str: string representation of BaseModel atttributes
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute `updated_at` with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance

        Return:
            dict: dictionary containing the attributes of BaseModel
        """
        dicts = self.__dict__.copy()
        dicts["__class__"] = self.__class__.__name__
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.updated_at.isoformat()
        return dicts
