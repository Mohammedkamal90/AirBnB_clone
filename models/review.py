#!/usr/bin/python3
"""Review class inheriting from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """representing Review"""
    place_id = ""
    user_id = ""
    text = ""
