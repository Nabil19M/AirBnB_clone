#!/usr/bin/python3
""" import cmd (command line oriented) module
    """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB."""
    prompt = "(hbnb) "

    def erroring(self, line, num_of_args):
        """Displays error messages to user

        Args:
            line(any): gets user input using command line
            num_of_args(int): number of input arguments

        Description:
            Displays output to the use based on
            the input commands.

        """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        error = ["** class name missing **",
                 "** class doesn't exist **",
                 "** instance id missing **",
                 "** no instance found **",
                 "** attribute name missing **",
                 "** value missing **"]
        if not line:
            print(error[0])
            return 1
        args = line.split()
        if num_of_args >= 1 and args[0] not in classes:
            print(error[1])
            return 1
        elif num_of_args == 1:
            return 0
        if num_of_args >= 2 and len(args) < 2:
            print(error[2])
            return 1
        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in objects:
            print(error[3])
            return 1
        if num_of_args >= 3 and len(args) < 3:
            print(error[4])
            return 1
        if num_of_args >= 3 and len(args) < 4:
            print(error[5])
            return 1

    def do_quit(self, line):
        """Quit command to exit the program.\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program.\n"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id\n
            Ex: $ create BaseModel"""
        if self.erroring(line, 1) == 1:
            return
        args = line.split(" ")
        obj = eval(args[0])()
        storage.new(obj)
        storage.save()
        print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
            based on the class name and id
            \nEx: $ show BaseModel 1234-1234-1234."""
        if self.erroring(line, 2) == 1:
            return
        args = line.split(" ")
        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        print(objects[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id\n
        Ex: $ destroy BaseModel 1234-1234-1234."""
        if self.erroring(line, 2) == 1:
            return
        args = line.split(" ")
        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        del (objects[key])
        storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instances
            based or not on the class name.
            \nEx: $ all BaseModel or $ all. """
        args = line.split(" ")
        objects = storage.all()
        if not line:
            for v in objects.values():
                print([str(v)])
            return
        if (self.erroring(line, 1) == 1):
            return
        print([str(v) for v in objects.values()
              if v.__class__.__name__ == args[0]])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        \nEx: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if self.erroring(line, 4) == 1:
            return
        args = line.split(" ")
        attr_name = args[2]
        attr_value = args[3]
        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        upd_obj = objects[key]
        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            elif float(attr_value):
                attr_value = float(attr_value)
        except ValueError:
            pass
        setattr(upd_obj, attr_name, attr_value)
        upd_obj.save()

    def emptyline(self):
        """Override emptyline method to do nothing on an empty input line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
