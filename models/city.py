#!/user/bin/python3
"""City class inheriting from BaseModel"""
from models.base_models import BaseModel


class City(BaseModel):
    """representing City"""
    state_id = ""
    name = ""
