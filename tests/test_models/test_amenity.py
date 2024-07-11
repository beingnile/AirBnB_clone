#!/usr/bin/python3
"""Defines testcases for amenity model"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""
    def setUp(self):
        """Set up test methods"""
        self.amenity = Amenity()

    def test_instance(self):
        """Test that amenity is an instance of BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_default_attributes(self):
        """Test default attributes are empty strings"""
        self.assertEqual(self.amenity.name, "")

    def test_set_attributes(self):
        """Test setting attributes"""
        self.amenity.name = "Wifi"
        self.assertEqual(self.amenity.name, "Wifi")

    def test_attributes_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.amenity.name, str)

    def test_none_attributes(self):
        """Test setting attributes to None"""
        self.amenity.name = None
        self.assertIsNone(self.amenity.name)

    def test_save_method(self):
        """Test save method from BaseModel"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method from BaseModel"""
        self.amenity.name = "Wifi"
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Wifi")
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
