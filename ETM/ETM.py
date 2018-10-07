#!/usr/bin/env python

opt = []
__author__ = 'Pedro Henrique Santos (Blackman White)'
__version__ = 1.0
__license__ = 'GNU General Public License v3.0'

class Menu():
    def __init__(self, title, character):
        self.title = title
        self.character = character

    def print_menu(self):
        print('{0}{0}{0}{0}{0}{0}{0}{0}{1}{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.character, self.title))

    def print_options(self):
        option_n = 1
        for option in opt:
            print('[{}] {}'.format(option_n, option))
            option_n += 1

    def print_all(self):
        print('{0}{0}{0}{0}{0}{0}{0}{0}{1}{0}{0}{0}{0}{0}{0}{0}{0}'.format(self.character, self.title))
        option_n = 1
        for option in opt:
            print('[{}] {}'.format(option_n, option))
            option_n += 1

    def add_option(self, option):
        opt.append(option)

    def print_info(self):
        print('Title: {}\nOption amount: {}\nOptions: {}'.format(self.title, len(opt), opt))

    def about(self):
        print('Made by {}\nVersion: {}\nLicense: {}'.format(__author__,__version__,__license__))
        
