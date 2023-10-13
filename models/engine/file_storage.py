#!/usr/bin/python3
"""class serializes instances to JSON file & deserializes JSON to instances"""
import JSON
from models.base_models import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """the FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        js = {}
        for key, val in self.__objects.items():
            js[key] = val.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(js, f)

    def reload(self):
        """deserializes JSON file to __objects if it exists (__file_path)"""
        try:
            with open(self.__file_path, 'r') as f:
                ob = json.load(f)
                for key, obj in data.items():
                    val = eval(obj['__class__'])(**obj)
                    self.__objects[key] = val
        except FileNotFoundError:
            pass
