#!/usr/bin/python3
"""Define a File storage"""
from .. import BaseModel
import json


class FileStorage:
    """Represent a file storage"""

        __file_path = "file.json"
        __objects = {}

    def all(self):
        """Methods to returns the dictionary

        """
        return self.__objects

    def new(self, obj):
        """Method set the object with the key

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Method to save file

        """
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Method to load file

        """
        try:
             with open(self.__file_path, encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    cls = getattr(models, cls_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
