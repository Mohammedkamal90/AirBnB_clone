#!/usr/bin/python3
""" console """

import cmd
import json
import uuid
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print("")  # Print a new line before exiting
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance based on class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = BaseModel.load_from_file()
            for obj_id, obj in objects.items():
                if obj.id == args[1]:
                    print(obj)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id, then save the change to the JSON file"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = BaseModel.load_from_file()
            obj_to_remove = None
            for obj_id, obj in objects.items():
                if obj.id == args[1]:
                    obj_to_remove = obj
                    break
            if obj_to_remove:
                objects.pop(obj_to_remove.id)
                BaseModel.save_to_file(objects)
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print the string representation of all instances based on class name or all"""
        args = arg.split()
        objects = BaseModel.load_from_file()
        result = []
        if not arg:
            for obj in objects.values():
                result.append(str(obj))
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Update an instance based on class name and id with a new attribute value"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            objects = BaseModel.load_from_file()
            obj_to_update = None
            for obj_id, obj in objects.items():
                if obj.id == args[1]:
                    obj_to_update = obj
                    break
            if obj_to_update:
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj_to_update, attr_name, attr_value)
                obj_to_update.save()
            else:
                print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
