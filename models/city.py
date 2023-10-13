#!/user/bin/python3
"""City class inheriting from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """representing City"""
    state_id = ""
    name = ""
