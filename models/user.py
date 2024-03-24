#!/usr/bin/python3
#models/user.py
""" class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represent user
    """
    email=""
    password=""
    first_name=""
    last_name=""
