#!/usr/bin/python3
import json


class FileStorage:
    __file_path = ""
    __objects = {}

    def all(self):
        return type(self).__objects

    def new(self, obj):
        type(self).__objects[type(self).id] = obj

    def save(self):
        json.dumps(type(self).__objects, type(self).__file_path)

    def reload(self):
        json.load(type(self).__file_path)
