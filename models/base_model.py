#!/usr/bin/python3
"""
Define the BaseModel of the console
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(val))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dic_t = self.__dict__.copy()
        dic_t["__class__"] = type(self).__name__
        dic_t["created_at"] = self.created_at.isoformat()
        dic_t["updated_at"] = self.updated_at.isoformat()
        return (dic_t)
