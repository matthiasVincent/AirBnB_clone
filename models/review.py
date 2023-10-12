#!/usr/bin/python3
"""class Review inherits from BaseModel class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """defines Review class with attributes:
    place_id: string, empty
    user_id: string, empty
    text: string, empty"""
    place_id = ""
    user_id = ""
    text = ""
