# This is the main module of the program
# The admin password is 'admin'
# From here the interface of the application can be accessed
import exit_application as ea
import book_functions as bf
from time import sleep
import registration
import pick_save
import password
import os

# Clear the screen and set text color to green
os.system('cls')
os.system('color 0A')


def start():
    # Display the welcome screen
    print("\n\n\t\t\t\t\t\t\t\t****** WELCOME TO THE LINCOLN LIBRARY ******")
    print("\t\t\t\t\t\t\t\t\t  ~ Readers Are Leaders ~\n")
    print("\t\t\t\t\t\t\t\t\t\t 1.Sign in as admin")
    print("\t\t\t\t\t\t\t\t\t\t 2.Sign in as user")
    print("\t\t\t\t\t\t\t\t\t\t 3.Sign up")

    print("\t\t\t\t\t\t\t\t\t\t 4.See Catalogue")
    print("\t\t\t\t\t\t\t\t\t\t 5.Exit Application")

    # This should only be done once
    # Do this twice, and you write over your existing database.
    print("\t\t\t\t\t\t\t\t\t\t ~.Create empty list")

    choice = input(str("\n\n\t\t\t\t\t\t\t\t\t\t <> Enter choice: "))

    # Pass control to the appropriate module
    if choice == '1':
        os.system('cls')
        password.admin_password_comp()

    elif choice == '2':
        os.system('cls')
        name = input("\n\n\t\t\t\t\t\t\t\t\t\tEnter your first_name:").title()
        password.get_password(name)

    elif choice == '3':
        registration.home_page()
        os.system('cls')
        start()

    elif choice == '4':
        bf.view_catalogue()
        os.system('cls')
        start()

    elif choice == '5':
        ea.leave()

    elif choice == '~':
        # I choose a strange sign so that you
        # invoke this method with prudence.
        # Call this only once to create the initial user list
        # Otherwise your data will be overwritten
        pick_save.create_user_list()
        print("file opened!")
        sleep(3)
        os.system('cls')
        start()


start()
