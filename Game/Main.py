#MAIN

import sys
import os

#Include /src whenever importing any modules so not to include it again and again per import within interior code
#If code not in /src checks from Main.py level hence works both ways
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import clientVal.variables as var

import src.loginMenu as loginMenu

while True:
    if(var.uuid): 
        import src.worldMenu
        break

import src.gameMenu