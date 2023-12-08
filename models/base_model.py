#!/usr/bin/python3
"""Defines a BaseModel"""
from datetime import datetime
import uuid


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Overwrites __str__ to print
        [<class name>] (<self.id>) <self.__dict__>
        """
        s = f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
        return s

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance.
        A key __class__ is added with the class name
        of the object. Both created_at and updated_at
        attributes are converted into isoformat

        Returns: A dict representation of the object
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()

        return dict_rep
