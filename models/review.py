#!/usr/bin/python3
# models/review.py
"""class review"""
from models.base_model import BaseModel


class Review (BaseModel):
    """
    Represent Review
    """
    place_id = ""
    user_id = ""
    text = ""
