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
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        local = locals()
        my_dict = {}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                my_dict = json.load(f)
            for key, value in my_dict.items():
                model = local.get(value['__class__'])
                FileStorage.__objects[key] = model(**value)
        except Exception:
            pass
