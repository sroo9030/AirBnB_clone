#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    """Unit tests for BaseModel class"""

    def test_init(self):
        """Test initialization of BaseModel instance"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
