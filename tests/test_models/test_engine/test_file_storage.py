#!/usr/bin/python3
"""Defines tests for file_storage"""
import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Defines tests for FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Ensure file.json is deleted before each test run"""
        if os.path.exists('file.json'):
            os.remove('file.json')
        cls.storage = FileStorage()
        cls.storage.reload()

    def setUp(self):
        """Sets up an instance of base_model"""
        self.base_model = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Deletes the file"""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_initialization(self):
        """Tests the initialization of FileStorage class"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_all_method(self):
        """Tests the all() method returns the __objects dictionary"""
        self.assertEqual(self.storage.all(),
                         self.storage._FileStorage__objects)

    def test_new_method(self):
        """Tests the new method"""
        self.storage.new(self.base_model)
        key = f'BaseModel.{self.base_model.id}'
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)

    def test_save_method(self):
        """Tests the save method"""
        key = f'BaseModel.{self.base_model.id}'
        self.storage.new(self.base_model)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = f.read()
            self.assertIn(key, data)

    def test_reload_method(self):
        """Tests the reload method"""
        self.storage.new(self.base_model)
        key = f'BaseModel.{self.base_model.id}'
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)

    def test_serialize_model(self):
        """Test serialization of model to __objects"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open('file.json', 'r') as f:
            saved_data = json.load(f)
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, saved_data)
        serialized_model = saved_data[key]
        self.assertEqual(serialized_model['id'], model.id)
        self.assertEqual(serialized_model['__class__'],
                         model.__class__.__name__)
        self.assertEqual(serialized_model['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(serialized_model['updated_at'],
                         model.updated_at.isoformat())

    def test_invalid_class_reload(self):
        """Test reloading when encountering an invalid class in file.json"""
        pre = len(self.storage.all())
        invalid_data = {
            'InvalidClass.123': {
                '__class__': 'InvalidClass',
                'id': '123',
                'created_at': '2023-01-01T00:00:00',
                'updated_at': '2023-01-01T00:00:00'
            }
        }
        with open('file.json', 'w') as f:
            json.dump(invalid_data, f)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), pre)


if __name__ == '__main__':
    unittest.main()
