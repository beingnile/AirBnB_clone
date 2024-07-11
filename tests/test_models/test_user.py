#!/usr/bin/python3
"""Defines testcases for the user model"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Testcases for the User class"""
    def setUp(self):
        """Sets up test methods"""
        self.user = User()

    def tearDown(self):
        """Tears down test methods"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance(self):
        """Tests that user is an instance of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_default_attributes(self):
        """Tests default attributes are empty strings"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_set_attributes(self):
        """Tests setting attributes"""
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_attributes_types(self):
        """Tests attribute types"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_none_attributes(self):
        """Tests setting attributes to None"""
        self.user.email = None
        self.user.password = None
        self.user.first_name = None
        self.user.last_name = None
        self.assertIsNone(self.user.email)
        self.assertIsNone(self.user.password)
        self.assertIsNone(self.user.first_name)
        self.assertIsNone(self.user.last_name)

    def test_save_method(self):
        """Tests save method from BaseModel"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)

    def test_to_dict_method(self):
        """Tests to_dict method from BaseModel"""
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

    def test_save_to_file(self):
        """Tests if the user is saved to the file"""
        self.user.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            data = json.load(file)
            key = f"User.{self.user.id}"
            self.assertIn(key, data)


if __name__ == '__main__':
    unittest.main()
