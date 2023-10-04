# This module just exits the application
from os import system
import interface_functions as int_fs


def return_main_menu(first_name):
    """Return to the previous menu."""
    choice = input(str("Enter (1) to return to the previous menu or (0) to exit: "))
    if choice == '1':
        int_fs.member_home(first_name)
    elif choice == '0':
        leave()


def leave():
    system('cls')
    print("\n\n\t\t\t\t\t\t\t\t ****** THANK YOU FOR USING THE LMS APPLICATION ******")
    print("\t\t\t\t\t\t\t\t\t   >>> Akkada  Data Science Technology >>>")
    exit()
