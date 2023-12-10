#!/usr/bin/python3
"""Defines a cmd prompt"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
