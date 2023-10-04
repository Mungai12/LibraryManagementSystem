"""
This is a very important module.It controls the files of the program
tweak things here wisely!!
"""

import pickle
from time import sleep
import exit_application as ea
import interface_functions as int_fs


def save_object(obj, filename):
    """Save the object to the pickle file."""
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


def load_object(filename):
    """Load the object from the pickle file and return it to caller."""
    with open(filename, 'rb') as inp:
        obj = pickle.load(inp)
    return obj


def create_user_list():
    """Make the list once and never enter the function again."""
    library_users = []
    save_object(library_users, 'library_users.pkl')

    choice = input(str("Enter (1) to return to menu or (0) to exit: "))
    if choice == '1':
        pass
    elif choice == '0':
        ea.leave()


def create_book_list():
    """Make the list once and never enter the function again."""
    book_list = []
    save_object(book_list, 'book_list.pkl')
    print("File created!")
    sleep(3)
    int_fs.admin_home()
