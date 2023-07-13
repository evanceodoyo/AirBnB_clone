#!/usr/bin/python3

"""
Entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "
    __models = {"BaseModel", "User", "Amenity",
                "State", "City", "Place", "Review", }

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
        Creates a new instance of a class, saves it (to the JSON file)
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

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).

        Args:
            arg (str): Argument to enter with command: <class_name> <id>
            <attribute name> "<attribute value>"
            Example: update BaseModel 1234-1234-1234 email "example@mail.com"
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                setattr(storage.all()[key], args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class.

        Args:
            arg (str): Argument to enter with command: <class_name>
            Example: count BaseModel
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        else:
            print(len([key for key in storage.all()
                       if key.startswith(args[0])]))

    def default(self, arg):
        """
        Retrieve all instances of a class by using: <class name>.all().
        Retrieve the number of instances of a class by using:
        <class name>.count().
        Retrieve an instance based on its ID: <class name>.show(<id>).
        Destroy an instance based on his ID: <class name>.destroy(<id>).
        Update an instance based on his ID: <class name>.update(<id>,
        <attribute name>, <attribute value>).

        Args:
            arg (str): Argument to enter with command: <class_name>.<method>()
            Example: User.all()
        """
        args = arg.split(".")
        if len(args) > 1:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.do_count(args[0])
            elif args[1].startswith("show("):
                id = args[1].split("(")[1].split(")")[0]
                self.do_show(args[0] + " " + id)
            elif args[1].startswith("destroy("):
                id = args[1].split("(")[1].split(")")[0]
                self.do_destroy(args[0] + " " + id)
            elif args[1].startswith("update("):
                id = args[1].split("(")[1].split(",")[0]
                attribute = args[1].split("(")[1].split(",")[1]
                value = args[1].split("(")[1].split(",")[2].split(")")[0]
                self.do_update(args[0] + " " + id + " " + attribute + " " +
                               value)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
