#!/usr/bin/python3
"""Defines a User class inheriting from BaseModel"""
from .base_model import BaseModel


class User(BaseModel):
    """Defines a user model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
