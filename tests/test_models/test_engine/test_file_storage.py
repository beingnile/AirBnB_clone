#!/usr/bin/python3
"""Defines tests for file_storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Defines tests for FileStorage class"""
    def setUp(self):
        """Sets up an instance of FileStorage"""
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """Deletes the instance"""
        self.storage = None

    def test_initialization(self):
        """Tests the initialization of FileStorage class"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_new_method(self):
        """Tests the new method"""
        self.storage.new(self.base_model)
        key = f'BaseModel.{self.base_model.id}'
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.base_model.to_dict())

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
        self.assertEqual(self.storage.all()[key], self.base_model.to_dict())


if __name__ == '__main__':
    unittest.main()
