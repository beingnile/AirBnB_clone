#!/usr/bin/python3
"""Defines testcases for place model"""
import json
import os
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests cases for the Place class"""
    def setUp(self):
        """Sets up test methods"""
        self.place = Place()

    def tearDown(self):
        """Tears down test methods"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance(self):
        """Tests that place is an instance of BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_default_attributes(self):
        """Tests default attributes are correctly set"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_set_attributes(self):
        """Tests setting attributes"""
        self.place.city_id = "1234"
        self.place.user_id = "5678"
        self.place.name = "Cool Place"
        self.place.description = "A very cool place"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 5
        self.place.price_by_night = 100
        self.place.latitude = 40.7128
        self.place.longitude = -74.0060
        self.place.amenity_ids = ["wifi", "tv"]

        self.assertEqual(self.place.city_id, "1234")
        self.assertEqual(self.place.user_id, "5678")
        self.assertEqual(self.place.name, "Cool Place")
        self.assertEqual(self.place.description, "A very cool place")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 5)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.amenity_ids, ["wifi", "tv"])

    def test_attributes_types(self):
        """Tests attribute types"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_none_attributes(self):
        """Tests setting attributes to None"""
        self.place.city_id = None
        self.place.user_id = None
        self.place.name = None
        self.place.description = None
        self.place.number_rooms = None
        self.place.number_bathrooms = None
        self.place.max_guest = None
        self.place.price_by_night = None
        self.place.latitude = None
        self.place.longitude = None
        self.place.amenity_ids = None

        self.assertIsNone(self.place.city_id)
        self.assertIsNone(self.place.user_id)
        self.assertIsNone(self.place.name)
        self.assertIsNone(self.place.description)
        self.assertIsNone(self.place.number_rooms)
        self.assertIsNone(self.place.number_bathrooms)
        self.assertIsNone(self.place.max_guest)
        self.assertIsNone(self.place.price_by_night)
        self.assertIsNone(self.place.latitude)
        self.assertIsNone(self.place.longitude)
        self.assertIsNone(self.place.amenity_ids)

    def test_save_method(self):
        """Tests save method from BaseModel"""
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)

    def test_to_dict_method(self):
        """Tests to_dict method from BaseModel"""
        self.place.city_id = "1234"
        self.place.user_id = "5678"
        self.place.name = "Cool Place"
        self.place.description = "A very cool place"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 5
        self.place.price_by_night = 100
        self.place.latitude = 40.7128
        self.place.longitude = -74.0060
        self.place.amenity_ids = ["wifi", "tv"]

        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['city_id'], "1234")
        self.assertEqual(place_dict['user_id'], "5678")
        self.assertEqual(place_dict['name'], "Cool Place")
        self.assertEqual(place_dict['description'], "A very cool place")
        self.assertEqual(place_dict['number_rooms'], 3)
        self.assertEqual(place_dict['number_bathrooms'], 2)
        self.assertEqual(place_dict['max_guest'], 5)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 40.7128)
        self.assertEqual(place_dict['longitude'], -74.0060)
        self.assertEqual(place_dict['amenity_ids'], ["wifi", "tv"])
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    def test_save_to_file(self):
        """Tests if the place is saved to the file"""
        self.place.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            data = json.load(file)
            key = f"Place.{self.place.id}"
            self.assertIn(key, data)


if __name__ == '__main__':
    unittest.main()
