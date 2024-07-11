#!/usr/bin/python3
"""Defines testcases for the user model"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime

class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up test methods"""
        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def test_instance(self):
        """Test that user is an instance of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test attributes of the User class"""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_attributes_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_save_method(self):
        """Test save method from BaseModel"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method from BaseModel"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
