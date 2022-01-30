#!/usr/bin/python3
import json

class FileStorage:
    __file_path = ""
    __objects = {}

    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        FileStorage.__objects['obj'] = f'type(self).__name__'
    def save(self):
        json.dump(FileStorage.__objects, FileStorage.__file_path)
