#!/usr/bin/python3
"""Defines testcases for city model"""
import json
import os
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Testcases for the City class"""
    def setUp(self):
        """Sets up test methods"""
        self.city = City()

    def tearDown(self):
        """Tears down test methods"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance(self):
        """Tests that city is an instance of BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_default_attributes(self):
        """Tests default attributes are empty strings"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_set_attributes(self):
        """Tests setting attributes"""
        self.city.state_id = "1234"
        self.city.name = "San Francisco"
        self.assertEqual(self.city.state_id, "1234")
        self.assertEqual(self.city.name, "San Francisco")

    def test_attributes_types(self):
        """Tests attribute types"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_none_attributes(self):
        """Tests setting attributes to None"""
        self.city.state_id = None
        self.city.name = None
        self.assertIsNone(self.city.state_id)
        self.assertIsNone(self.city.name)

    def test_save_method(self):
        """Tests save method from BaseModel"""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_to_dict_method(self):
        """Tests to_dict method from BaseModel"""
        self.city.state_id = "1234"
        self.city.name = "San Francisco"
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['state_id'], "1234")
        self.assertEqual(city_dict['name'], "San Francisco")
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_save_to_file(self):
        """Tests if city model is saved to the file"""
        self.city.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            data = json.load(file)
            key = f"City.{self.city.id}"
            self.assertIn(key, data)


if __name__ == '__main__':
    unittest.main()
