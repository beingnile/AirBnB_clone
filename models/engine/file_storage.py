#!/usr/bin/python3
import json

class FileStorage:
    __file_path = ""
    __objects = {}

    def all(self):
        return __class__.__objects
    def new(self, obj):
        __class__.__objects['obj'] = f'type(self).__name__'
    def save(self):
        json.dump(__class__.__objects, __class__.__file_path)
