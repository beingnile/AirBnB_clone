#!/usr/bin/python3
"""Defines a cmd prompt"""
import cmd
from models.base_model import BaseModel
from models import storage


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
        elif arg == 'BaseModel':
            b = BaseModel()
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
        args = arg.split()
        if len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            if args[0] == 'BaseModel':
                key = args[0] + '.' + args[1]
                storage.reload()
                my_objs = storage.all()
                try:
                    my_dict_obj = my_objs[key]
                    model = BaseModel(**my_dict_obj)
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
        args = arg.split()
        if len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            if args[0] == 'BaseModel':
                key = args[0] + '.' + args[1]
                storage.reload()
                try:
                    del(storage.all()[key])
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
