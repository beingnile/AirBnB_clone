#!/usr/bin/python3
"""Defines a City class"""
from .base_model import BaseModel


class City(BaseModel):
    """Defines a city model"""
    state_id = ""  # state.id
    name = ""
