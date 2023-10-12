#!/usr/bin/python3
"""This module defines BaseModel class which contains common attribute
   and methods for other classes"""

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """BaseModel class defines a generic attributes and methods for su
    b classes"""
    def __init__(self, *args, **kwargs):
        """instantiate BaseModel class with attributes:
           id: string-assign unique id when an instance is created
           created_at: datetime-assign current datetime when an instan
           ce is created
           updated_at: datetime-assign current datetime when a previou-
           sly created instance is updated
           args: anonymous positional args, not used
           kwargs: keyworded arguments, used in
           creating instance from a dictionary
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k in ["created_at", "updated_at"]:
                    v = datetime.fromisoformat(v)
                    setattr(self, k, v)
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """print a human readable representation of the instance in the
        format: [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__
        fmt = "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
        return fmt

    def save(self):
        """updates the public instance attribute created_at with the
        current datetime"""
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """returns  a dictionary containing all keys/values of __dict__
        of the instance. key, __class__ is also added. created_at and
        updated_at must be string in ISO format"""
        my_dict = self.__dict__.copy()
        my_dict.update({"__class__": self.__class__.__name__})
        for key in my_dict.keys():
            if key in ["created_at", "updated_at"]:
                my_dict[key] = my_dict[key].isoformat()
        return my_dict
