#!/usr/bin/python3
'''
A module
'''
import cmd

class HBNBCommand(cmd.Cmd):
    '''
    A command prompt
    '''
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
