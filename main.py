from screenwriting.screenwriting import dur_type
from classicmode import classicmode
from algor import algorithmode
import sys
import random


def menu():
    dur_type("what would you like to do?")
    dur_type("type 'classic' to play classic mode")
    dur_type("type 'algor' to play algorithmic mode")
    dur_type("type 'friendhouse' to play hard mode")
    dur_type("type 'medal' to view achievements")
    dur_type("type 'exit' to exit the game")
    choice = input()
    if choice == "classic":
        classicmode()
    elif choice == "algor":
        algorithmode()


menu()
