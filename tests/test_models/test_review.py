#!/usr/bin/python3
"""Defines testcases for review model"""
import json
import os
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Testcases for the Review class"""
    def setUp(self):
        """Sets up test methods"""
        self.review = Review()

    def tearDown(self):
        """Tears down test methods"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance(self):
        """Tests that review is an instance of BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_default_attributes(self):
        """Tests default attributes are empty strings"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_set_attributes(self):
        """Tests setting attributes"""
        self.review.place_id = "1234"
        self.review.user_id = "5678"
        self.review.text = "Great place!"
        self.assertEqual(self.review.place_id, "1234")
        self.assertEqual(self.review.user_id, "5678")
        self.assertEqual(self.review.text, "Great place!")

    def test_attributes_types(self):
        """Tests attribute types"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_none_attributes(self):
        """Tests setting attributes to None"""
        self.review.place_id = None
        self.review.user_id = None
        self.review.text = None
        self.assertIsNone(self.review.place_id)
        self.assertIsNone(self.review.user_id)
        self.assertIsNone(self.review.text)

    def test_save_method(self):
        """Tests save method from BaseModel"""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_to_dict_method(self):
        """Tests to_dict method from BaseModel"""
        self.review.place_id = "1234"
        self.review.user_id = "5678"
        self.review.text = "Great place!"
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['place_id'], "1234")
        self.assertEqual(review_dict['user_id'], "5678")
        self.assertEqual(review_dict['text'], "Great place!")
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

    def test_save_to_file(self):
        """Tests if the review is saved to the file"""
        self.review.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            data = json.load(file)
            key = f"Review.{self.review.id}"
            self.assertIn(key, data)


if __name__ == '__main__':
    unittest.main()
