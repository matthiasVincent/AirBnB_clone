#!/usr/bin/python3
"""Instantiating a fileStorage class for
our application"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
