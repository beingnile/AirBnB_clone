#!/usr/bin/python3
"""Defines testcases for state model"""
import json
import os
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""
    def setUp(self):
        """Sets up test methods"""
        self.state = State()

    def tearDown(self):
        """Tears down test methods"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance(self):
        """Tests that state is an instance of BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_default_attributes(self):
        """Tests default attributes are empty strings"""
        self.assertEqual(self.state.name, "")

    def test_set_attributes(self):
        """Tests setting attributes"""
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_attributes_types(self):
        """Tests attribute types"""
        self.assertIsInstance(self.state.name, str)

    def test_none_attributes(self):
        """Tests setting attributes to None"""
        self.state.name = None
        self.assertIsNone(self.state.name)

    def test_save_method(self):
        """Tests save method from BaseModel"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

    def test_to_dict_method(self):
        """Tests to_dict method from BaseModel"""
        self.state.name = "California"
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['name'], "California")
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_save_to_file(self):
        """Test if the state is saved to the file"""
        self.state.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            data = json.load(file)
            key = f"State.{self.state.id}"
            self.assertIn(key, data)


if __name__ == '__main__':
    unittest.main()
