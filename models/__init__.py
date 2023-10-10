#!/usr/bin/python3
"""updated to create unique FileStorage instance for the app"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
