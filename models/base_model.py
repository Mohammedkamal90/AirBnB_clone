#!/usr/bin/python3
"""class BaseModels defining all common attributes/methosesfor other classes"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """the class BaseModel"""
    def __init__(self, *args, **kwargs):
        """initializing the class"""
        if kwargs:
            for key, val in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """updates public instance attribute updated_at with current date"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary with all keys/values of __dict__ s"""
        dictionary = dict(self.__dict__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['__class__'] = str(self.__class__.__name__)
        return dictionary

    def __str__(self):
        """BaseModel string representation"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """returns the __str__"""
        return self.__str__()
