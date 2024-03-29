#!/usr/bin/python3
"""Defines a class FileStorage"""
import json


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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the
        JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        if the JSON file (__file_path) exists;

        Otherwise, it does nothing.
        If the file doesn’t exist, no exception is raised
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except Exception:
            pass
