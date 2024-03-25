# -*- coding: utf-8 -*-

from . import base_model, amenity, city, place, review, state
from . import user
from .engine.file_storage import FileStorage
#from tests.test_models.test_base_model import *

storage = FileStorage()
storage.reload()
__all__ = ['BaseModel', 'User', 'FileStorage']
