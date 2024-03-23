#!/usr/bin/python3
"""Define a File storage"""
from .. import base_model


class FileStorage:
    """Represent a file storage"""

    def __init__(self, filename):
        """Initialize a file

        """
        self.filename = filename

    def save(self, data):
        """Method to save file

        """
        with open(self.filename, mode='w', encoding='utf-8') as f:
            json.dump(data, f)

    def load(self):
        """Method to load file

        """
        try:
            with open(self.filename, encoding='utf-8') as f:
                return jason.load(f)
        except:
            FileNotFoundError("File Not Found Error")
