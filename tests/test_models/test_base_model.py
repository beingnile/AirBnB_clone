#!/usr/bin/python3
"""Defines unittests for bade_model.py file"""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """Ensure file.json is deleted before each test run"""
        if os.path.exists('file.json'):
            os.remove('file.json')
        # Initialize FileStorage instance for testing
        cls.storage = FileStorage()
        cls.storage.reload()

    def setUp(self):
        """Sets up a BaseModel instance
        This method is run before each testcase
        """
        self.base_model = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Clean up: deletes file.json after all tests are run"""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_init(self):
        """Tests the initialization of new objects"""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_init_with_empty_kwargs(self):
        """Tests the initialization of new objects using kwargs"""
        kwargs = {}
        my_model = BaseModel(**kwargs)
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Tests the initialization of new objects using kwargs"""
        kwargs = self.base_model.to_dict()
        my_model = BaseModel(**kwargs)
        self.assertIsNotNone(my_model.id)
        self.assertEqual(my_model.id, self.base_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertEqual(my_model.created_at, self.base_model.created_at)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertEqual(my_model.updated_at, self.base_model.updated_at)

    def test_timezone_handling(self):
        """Test timezone handling in datetime attributes"""
        now_utc = datetime.utcnow()
        self.base_model.created_at = now_utc
        self.base_model.save()
        loaded_model = self.storage.all()[f"BaseModel.{self.base_model.id}"]
        self.assertEqual(loaded_model.created_at, now_utc)

    @patch('models.base_model.datetime')
    def test_save(self, mock_datetime):
        """Tests the save method. This test case mocks
        the datetime module to ensure that the
        updated_at attribute changes when the save
        method is called.
        """
        initial_count = len(self.storage.all())
        initial_updated_at = self.base_model.updated_at
        mock_datetime.now.return_value = datetime(2023, 1, 1)
        self.base_model.save()
        self.assertTrue(os.path.exists('file.json'))
        after_save_count = len(self.storage.all())
        self.assertEqual(after_save_count, initial_count)
        self.assertNotEqual(self.base_model.updated_at, initial_updated_at)
        self.assertEqual(self.base_model.updated_at, datetime(2023, 1, 1))

    def test_to_dict(self):
        """Tests the to_dict method"""
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str_method(self):
        """Tests the overwritten __str__ method"""
        out = f'[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}'
        self.assertEqual(str(self.base_model), out)

    def test_id_uniqueness(self):
        """Each object should have a unique ID.
        This methods tests for that
        """
        another_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, another_base_model.id)

    def test_to_dict_matches_attributes(self):
        """Tests the to_dict method"""
        model_dict = self.base_model.to_dict()
        self.assertEqual(model_dict['id'], self.base_model.id)
        crtd_iso = self.base_model.created_at.isoformat()
        self.assertEqual(model_dict['created_at'], crtd_iso)
        uptd_iso = self.base_model.updated_at.isoformat()
        self.assertEqual(model_dict['updated_at'], uptd_iso)


if __name__ == '__main__':
    unittest.main()
