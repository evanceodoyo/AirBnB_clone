#!/usr/bin/python3
"""
Contains the entry point of the command inteprete using the cmd module.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Console command processor class.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Execute nothing on empty line + ENTER.
        """
        pass

    def do_EOF(self, line):
        """
        Exit the program on EOF.
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        print("")
        return True

    def help_quit(self):
        """
        Prints the help text for the quit command.
        """
        print("Quit command to exit the program")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
