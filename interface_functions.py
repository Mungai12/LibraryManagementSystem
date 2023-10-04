"""A module to hold all interfaces."""
import user
import pick_save
from os import system
import book_functions as bf
import exit_application as ea


# Only  the admin can access these interface.
def admin_home():
    """Display the lib member interface."""
    system('cls')
    print("\n\n\t\t\t\t\t\t\t\t****** WELCOME ADMIN TO THE LINCOLN LIBRARY ******")
    print("\t\t\t\t\t\t\t\t\t    ~ Readers Are Leaders ~\n")
    print("\t\t\t\t\t\t\t\t\t\t 1.add a book")
    print("\t\t\t\t\t\t\t\t\t\t @.create book_list")
    print("\t\t\t\t\t\t\t\t\t\t 2.Exit Application")

    choice = input(str("\n\n\t\t\t\t\t\t\t\t\t\t <> Enter choice: "))

    # Pass control to the appropriate module
    if choice == '1':
        system('cls')
        bf.book_home()
        admin_home()

    elif choice == '@':
        # I choose a strange sign so that you
        # invoke this method with prudence.
        # Call this only once to create the initial books list
        # Otherwise your data will be overwritten
        pick_save.create_book_list()
        admin_home()

    elif choice == '2':
        system('cls')
        ea.leave()


# Only registered members can access these interface.
# 'me' represents the first name of the current user
def member_home(first_name):
    """Display the library member interface."""
    system('cls')
    print("\n\n\t\t\t\t\t\t\t\t****** WELCOME " + first_name.upper() + " TO THE LINCOLN LIBRARY ******")
    print("\t\t\t\t\t\t\t\t\t    ~ Readers Are Leaders ~\n")
    print("\t\t\t\t\t\t\t\t\t\t 1.see catalogue")
    print("\t\t\t\t\t\t\t\t\t\t 2.Borrow a book")
    print("\t\t\t\t\t\t\t\t\t\t 3.Return a book")
    print("\t\t\t\t\t\t\t\t\t\t 4.Clear Overdue")
    print("\t\t\t\t\t\t\t\t\t\t 5.View  Account details")
    print("\t\t\t\t\t\t\t\t\t\t 6.Exit Application")

    choice = input(str("\n\n\t\t\t\t\t\t\t\t\t\t <> Enter choice: "))

    if choice == '1':
        bf.view_catalogue(first_name)
        system('cls')
        member_home(first_name)

    if choice == '2':
        bf.borrow_book(first_name)
        system('cls')
        member_home(first_name)

    if choice == '3':
        bf.return_book(first_name)
        system('cls')
        member_home(first_name)

    if choice == '4':
        bf.clear_overdue(first_name)
        system('cls')
        member_home(first_name)

    if choice == '5':
        user.view_details(first_name)
        system('cls')
        member_home(first_name)

    if choice == '6':
        ea.leave()
