#!/usr/bin/python3
'''
A module
'''
import cmd
from datetime import datetime
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    '''
    A command prompt
    '''
    prompt = '(hbnb) '
    validated_classes = ['BaseModel', 'FileStorage']
    update = ['id', 'created_at', 'updated_at']

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        '''For empty line and spaces'''
        pass

    def do_help(self, arg):
        ''' do help '''
        return super().do_help(arg)

    def do_EOF(self, arg):
        '''For EOF characters'''
        return True

    def do_create(self, arg):
        '''Creates an instances'''
        if arg:
            if (arg == 'BaseModel'):
                inst = BaseModel()
                inst.save()
                print(inst.id)
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_show(self, arg):
        ''' Shows Id'''
        className = self.parseline(arg)[0]
        Id_name = self.parseline(arg)[1]

        if className is None:
            print("** class name missing **")
            return
        elif className not in self.validated_classes:
            print("** class doesn't exist **")
            return
        if Id_name == '':
            print("** instance id missing **")
            return
        inst = models.storage.all().get(className + '.' + Id_name)
        if inst is None:
            print("** no instance found **")
        else:
            print(inst)

    def do_destroy(self, arg):
        ''' Destroys an Instance'''
        className = self.parseline(arg)[0]
        Id_name = self.parseline(arg)[1]

        if className is None:
            print("** class name missing **")
            return
        elif className not in self.validated_classes:
            print("** class doesn't exist **")
            return
        elif Id_name == '':
            print("** instance id missing **")
            return
        inst_id = className + '.' + Id_name
        inst = models.storage.all().get(className + '.' + Id_name)
        if inst is None:
            print("** no instance found **")
            return
        else:
            del models.storage.all()[inst_id]
            models.storage.save()

    def do_all(self, arg):
        ''' lists all Instances'''
        command = self.parseline(arg)[0]
        insts = models.storage.all()
        if command is None:
            print([str(insts[inst]) for inst in insts])
        elif command not in self.validated_classes:
            print("** class doesn't exist **")
        else:
            print([str(insts[inst])
                  for inst in insts if inst.startswith(command)])

    def do_update(self, arg):
        ''' Updates an Instances'''
        args = arg.split(' ')
        length = len(args)
        if len(args) == 1:
            print("** class name missing **")
            return
        elif args[0] not in self.validated_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 2:
            print("** instance id missing **")
            return
        inst_id = args[0] + '.' + args[1]
        inst = models.storage.all().get(inst_id)
        if inst is None:
            print("** no instance found **")
            return
        elif len(args) == 23:
            print("** attribute name missing **")
            return
        elif len(args) == 4:
            print("** value missing **")
            return
        elif args[2] not in self.update:
            setattr(inst, args[2], args[3])
            setattr(inst, 'updated_at', datetime.now())
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
