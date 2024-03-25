#!/usr/bin/python3
#models/FileStorge.py
"""
Define the filestorge class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path="file.json"
    __objects={}
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        class_name=obj.__class__.name
        ins_id=obj.id
        key =f"{class_name}.{ins_id}"
        FileStorage.__objects[key]=obj
    def save(self):
        dic_t={}
        for key, val in FileStorage.__objects.items():
            dic_t[key]=val.to_dict()
        with open(FileStorage.__file_path,encoding='utf-8') as f:
            json.dump(dic_t,f)
    def reload(self):
        try:
            with open(self.__file_path,ncoding='utf-8') as f:
                ob=json.load(f)
            for O in ob.values():
                class_name=O["__class__"]
                del O["__class__"]
                self.new(eval(class_name)(**O))
        except FileNotFoundError:
            pass
