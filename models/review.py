#!/usr/bin/python3
"""Defines a class review"""
from .base_model import BaseModel


class Review(BaseModel):
    """Defines a model for reviews"""
    place_id = ""  # Place.id
    user_id = ""  # User.id
    text = ""
