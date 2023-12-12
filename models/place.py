#!/usr/bin/python3
"""Defines a class place"""
from .base_model import BaseModel


class Place(BaseModel):
    """Defines a place model"""
    city_id = ""  # City.id
    user_id = ""  # User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # List of Amenity.id
