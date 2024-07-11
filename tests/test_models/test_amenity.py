#!/usr/bin/python3
"""Defines testcases for amenity model"""
import json
import os
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Tests cases for the Amenity class"""
    def setUp(self):
        """Sets up test methods"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tears down test methods"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance(self):
        """Tests that amenity is an instance of BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_default_attributes(self):
        """Tests default attributes are empty strings"""
        self.assertEqual(self.amenity.name, "")

    def test_set_attributes(self):
        """Tests setting attributes"""
        self.amenity.name = "Wifi"
        self.assertEqual(self.amenity.name, "Wifi")

    def test_attributes_types(self):
        """Tests attribute types"""
        self.assertIsInstance(self.amenity.name, str)

    def test_none_attributes(self):
        """Tests setting attributes to None"""
        self.amenity.name = None
        self.assertIsNone(self.amenity.name)

    def test_save_method(self):
        """Tests save method from BaseModel"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_to_dict_method(self):
        """Tests to_dict method from BaseModel"""
        self.amenity.name = "Wifi"
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Wifi")
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_save_to_file(self):
        """Test if the amenity is saved to the file"""
        self.amenity.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            data = json.load(file)
            key = f"Amenity.{self.amenity.id}"
            self.assertIn(key, data)


if __name__ == '__main__':
    unittest.main()
