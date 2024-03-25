#!/usr/bin/python3
# models/review.py
"""class review"""
from models.base_model import BaseMode


class Review (BaseModel):
    """
    Represent Review
    """
    place_id = ""
    user_id = ""
    text = ""
