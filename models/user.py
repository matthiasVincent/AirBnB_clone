#!/usr/bin/python3
"""class User inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """defines a User class with the following attributes
    email: string, empty
    password: string, empty
    first_name: string, empty
    last_name: string, empty
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
