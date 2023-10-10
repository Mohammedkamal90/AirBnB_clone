#!/usr/bin/python3
""" console """

import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.user import User
import shlex
from models.amenity import Amenity

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
