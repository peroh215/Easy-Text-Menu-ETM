#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = ('Pedro Henrique Santos (Blackman White)')
__version__ = ('3.5')
__license__ = ('GNU General Public License v3.0')

opt = []
index = 1

class Menu():
    def __init__(self, title, character, char_length):
        self.title = title
        self.character = character
        self.char_length = int(char_length)

    def change_title(self, new_title):
        self.title = new_title

    def print_menu(self):
        return print('{0}{1}{0}'.format(self.character*self.char_length, self.title))
                                                                                 
    def print_options(self):
        option_n = 1
        for Option in opt:
            print('[{}] {}'.format(option_n, Option.option))
            option_n += 1

    def print_all(self):
        self.print_menu()
        self.print_options()

    def add_option(self, option, command):
        o = Option(option, command)
        opt.append(o)

    def remove_option(self, _option):
        for Option in opt:
            if Option.option == _option:
                opt.remove(Option)
    
    def clear_option(self):
        opt.clear()

    def get_input(self):
        usr = input('> ')

        found = False
        for Option in opt:
            if usr == str(Option.index):
                found = True
                Option.command()           
        if found == True:
            pass
        else:
            print("Invalid command")
        
    def about(self):
        return print('Made by {}\nVersion: {}\nLicense: {}'.format(__author__,__version__,__license__))
        
class Option():
    def __init__(self, option, command):
        global index
        self.option = option
        self.command = command
        self.index = index
        opt.append(self)
        index += 1
