#!/usr/bin/env python3

""" Command line interpreter for AirBnB """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program by pressing Ctrl+D"""
        return True

    def help_quit(self):
        """Help guide for quit command"""
        print('Quit command to exit the program')

    def help_EOF(self):
        """Help guide for EOF command"""
        print('EOF command to exit the program')

    def emptyline(self):
        """Handles empty lines"""
        pass

    def do_create(self, arg):
        """ 
            Task: 7. Console 0.1
            Creates new instance of Basemodel, 
            saves it into JSON file
            and prints its id.
        """
        if arg != "" or arg is not None:
            if arg not in storage.classes():
                print("** class doesn't exist **")
            else:
                # create an instance of the given class
                obj_intance = storage.classes()[arg]()
                obj_intance.save()
                print(obj_intance.id)
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
