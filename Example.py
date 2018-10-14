#!/usr/bin/env python

# Imports
from ETM import *
import sys

# Variables
running = True

# Functions
def print_info():
    m.about()

def exitapp():
    sys.exit(0)

# Main
m = ETM.Menu(' MyApp ','-')
ETM.Option('Print info', print_info)
ETM.Option('Exit', exitapp)
m.print_all()
while running == True:
    m.get_input()
