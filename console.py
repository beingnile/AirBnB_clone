#!/usr/bin/python3
"""Defines a cmd prompt"""
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from sys import modules


cls_list = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']
classes = set(cls_list)


class HBNBCommand(cmd.Cmd):
    """Defines a cmd object"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Override empty line to do nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a model
        and saves it to a JSON file
        """
        if not arg:
            print("** class name missing **")
        elif arg in classes:
            my_class = getattr(modules[__name__], arg)
            b = my_class()
            b.save()
            print(b.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) == 1:
                token = ''.join(args)
                if token in classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            elif len(args) == 2:
                if args[0] in classes:
                    key = args[0] + '.' + args[1]
                    my_objs = storage.all()
                    try:
                        my_dict_obj = my_objs[key]
                        my_class = getattr(modules[__name__], args[0])
                        model = my_class(**my_dict_obj)
                        print(model)
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the
        class name and id
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) == 1:
                token = ''.join(args)
                if token in classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            elif len(args) == 2:
                if args[0] in classes:
                    key = args[0] + '.' + args[1]
                    try:
                        del (storage.all()[key])
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name
        """
        my_objs_list = []
        my_objs = storage.all()
        if not arg:
            for key, value in my_objs.items():
                cls = value.get('__class__')
                my_class = getattr(modules[__name__], cls)
                new_obj = my_class(**value)
                str_rep = new_obj.__str__()
                my_objs_list.append(str_rep)
            print(my_objs_list)
        elif arg in classes:
            for key, value in my_objs.items():
                if value.get('__class__') == arg:
                    my_class = getattr(modules[__name__], arg)
                    new_obj = my_class(**value)
                    str_rep = new_obj.__str__()
                    my_objs_list.append(str_rep)
            print(my_objs_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) == 1:
                token = ''.join(args)
                if token in classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            elif len(args) >= 2:
                if args[0] in classes:
                    key = args[0] + '.' + args[1]
                    my_objs = storage.all()
                    if key in my_objs:
                        if len(args) == 2:
                            print("** attribute name missing **")
                        elif len(args) == 3:
                            print("** value missing **")
                        elif len(args) > 3:
                            attr = args[2]
                            value = args[3].strip("\"")
                            my_dict_obj = my_objs[key]
                            my_class = getattr(modules[__name__], args[0])
                            model = my_class(**my_dict_obj)
                            setattr(model, attr, value)
                            model.save()
                            storage.new(model)
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
