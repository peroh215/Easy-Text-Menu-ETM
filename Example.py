#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Imports
from ETM import *
import sys

# Variables
running = True

# Functions
def print_info():
    m.about()

def changetitle():
    usr = input("Enter new title: ")
    m.change_title(' %s '% (usr))
    m.print_menu()
    
def add_opt():
    option = input("Enter new option: ")
    func = input("Enter function that option will execute: ")
    ETM.Option(option, func)
    m.print_options()

def remove_opt():
    usr = input("Enter option name: ")
    m.remove_option(str(usr))
    m.print_options()

def clear_opt():
    m.clear_option()
    m.print_all()

def exitapp():
    sys.exit(0)
    return None

# Main
m = ETM.Menu(' MyApp ','-')
ETM.Option('Print info', print_info)
ETM.Option('Change title', changetitle)
ETM.Option('Create an option', add_opt)
ETM.Option('Delete an option', remove_opt)
ETM.Option('Clear options', clear_opt)
ETM.Option('Exit', exitapp)
m.print_all()
while running == True:
    m.get_input()
