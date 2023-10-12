#!/usr/bin/python3
"""class Place inherits from BaseModel class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """defines class Place with attributes:
    city_id: string, empty
    user_id: string, empty
    name: string, empty
    description: string, empty
    number_rooms: integer, 0
    number_bathrooms: integer, 0
    max_guest: integer, 0
    price_by_night: integer, 0
    latitude: float, 0.0
    longitude: float, 0.0
    amenity_ids: list of strings, empty
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
