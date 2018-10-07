#!/usr/bin/env python

# Imports
from ETM import *
import sys

# Variables
running = True

# Functions
def u_input():
    usr = input('> ')
    
    if usr == '1':
        m.about()
    elif usr == '2':
        sys.exit(0)

# Main
m = ETM.Menu(' MyApp ','-')
m.add_option('Print info')
m.add_option('Exit')
m.print_all()
while running == True:    
    u_input()
