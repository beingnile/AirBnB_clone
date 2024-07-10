#!/usr/bin/python3
"""Defines a class FileStorage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key
        <obj class name>.id
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the
        JSON file (path: __file_path)
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            value = value.to_dict()
            my_dict[key] = value
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        if the JSON file (__file_path) exists;

        Otherwise, it does nothing.
        If the file doesn’t exist, no exception is raised
        """
        my_dict = {}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                my_dict = json.load(f)
            for key, value in my_dict.items():
                FileStorage.__objects[key] = BaseModel(**value)
        except Exception:
            pass
