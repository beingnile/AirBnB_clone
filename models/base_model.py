#!/usr/bin/python3

"""Defines a base class BaseModel"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes for other classes"""
    def __init__(self, *args, **kwargs):
        """Runs on instantiation of BaseModel class"""
        sformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, sformat)
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """Overwrites the inbuilt __str__ method

        Returns:
            [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Adds a key __class__ with the class name of object
        Converts created_at and updated_at to string object in ISO format

        Returns:
            A dictionary containing all keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = type(self).__name__
        return my_dict
