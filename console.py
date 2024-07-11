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

    def default(self, line):
        """Handles one-liner commands
        """
        import ast
        import sys
        from io import StringIO
        tokens = line.split('.')
        if len(tokens) != 2:
            return

        class_name = tokens[0]
        command = tokens[1]
        buf = StringIO()
        stdout = sys.stdout
        sys.stdout = buf
        self.do_all(class_name)
        sys.stdout = stdout
        cls_list = ast.literal_eval(buf.getvalue().strip())
        if command == 'all()':
            print(cls_list)
        elif command == 'count()':
            print(len(cls_list))
        elif 'show' in command:
            model_id = command.strip('show').strip('("")')
            arg = f'{class_name} {model_id}'
            self.do_show(arg)
        elif 'destroy' in command:
            model_id = command.strip('destroy').strip('("")')
            arg = f'{class_name} {model_id}'
            self.do_destroy(arg)
        elif 'update' in command:
            args = ast.literal_eval(command.strip('update()'))
            args_lst = list(args)
            if type(args_lst[1]) == dict:
                model_id = args_lst[0].strip('\"\' ')
                mydict = args_lst[1]
                for key, value in mydict.items():
                    attr = key.strip('\"\' ')
                    try:
                        val = value.strip('\"\' ')
                    except Exception:
                        val = value
                    arg = f'{class_name} {model_id} {attr} {value}'
                    self.do_update(arg)
            else:
                args = command.strip('update()').split(',')
                unparsed = [x.strip('\"\' ') for x in args]
                parsed = ' '.join(unparsed)
                arg = f'{class_name} {parsed}'
                self.do_update(arg)

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
                        model = my_objs[key]
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
            for value in my_objs.values():
                str_rep = value.__str__()
                my_objs_list.append(str_rep)
            print(my_objs_list)
        elif arg in classes:
            for value in my_objs.values():
                if value.to_dict().get('__class__') == arg:
                    str_rep = value.__str__()
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
                            model = my_objs[key]
                            setattr(model, attr, value)
                            model.save()
                            storage.new(model)
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
