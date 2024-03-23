#!/usr/bin/python3
"""Define user information"""
from models.base_model import BaseModel


class user(BaseModel):
    """Represent a user"""

    def (self, email="", password="", first_name="", last_name=""):
        """Define a new user

        """
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
