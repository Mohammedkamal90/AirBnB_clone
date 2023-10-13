#!/usr/bin/python3
"""User class inheriting from BaseModel"""
from models.base_models import BaseModel


class User(BaseModel):
    """representing a User of the API"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
