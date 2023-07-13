#!/usr/bin/python3

"""
Entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "
    __models = {"BaseModel", }

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldn’t execute anything.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.

        Args:
            arg (str): Argument to enter with command: <class_name>
            Example: create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__models:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id.

        Args:
            arg (str): Argument to enter with command: <class_name> <id>
            Example: show BaseModel 1234-1234-1234
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).

        Args:
            arg (str): Argument to enter with command: <class_name> <id>
            Example: destroy BaseModel 1234-1234-1234
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.

        Args:
            arg (str): Argument to enter with command: <class_name>
            Example: all BaseModel or all
        """
        args = arg.split()
        if not arg:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items()
                   if key.startswith(args[0])])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
