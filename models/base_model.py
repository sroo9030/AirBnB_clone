#!/usr/bin/python3
"""
Define the BaseModel of the console
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs is None:
            self.id =str(uuid.uuid4())
            self.created_at = datetime.now()        
            self.updated_at= datetime.now()
        else:
            for key ,val in kwargs.items():
                if key == "__class__":
                    pass
                elif key =="created_at" or key =="updated_at":
                    dt=datetime.fromisoformat(val)
                    setattr(self , key, dt)
                else:
                    setattr(self, key, val)
    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at=datetime.now()
        storge=FileStorge()
        storge.save(self)
    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        dic_t=self.__dict__.copy()
        dic_t["__class__"]=type(self).__class__.__name__
        dic_t["created_at"]=self.created_at.isoformat()
        dic_t["updated_at"]=self.updated_at.isoformat()
        return (dic_t)
