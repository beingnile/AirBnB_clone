#!/usr/bin/python3
"""Defines testcases for state model"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class"""
    def setUp(self):
        """Set up test methods"""
        self.state = State()

    def test_instance(self):
        """Test that state is an instance of BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_default_attributes(self):
        """Test default attributes are empty strings"""
        self.assertEqual(self.state.name, "")

    def test_set_attributes(self):
        """Test setting attributes"""
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_attributes_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.state.name, str)

    def test_none_attributes(self):
        """Test setting attributes to None"""
        self.state.name = None
        self.assertIsNone(self.state.name)

    def test_save_method(self):
        """Test save method from BaseModel"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method from BaseModel"""
        self.state.name = "California"
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['name'], "California")
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
