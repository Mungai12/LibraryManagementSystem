# Register a person to the library by collecting details
# And assigning a registration number
import os
import sys
import time
import random
import psycopg2
import pick_save
import exit_application as ea


# We set the root pass word here
password_1 = 'x'
password_2 = 'y'
count = 0


def typingPrint(text):
    for character in text:
        os.system('color 0A')
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.0)


def home_page():
    """print the welcome page."""
    os.system('cls')
    typingPrint("\n\n\n\t\t\t\t\t\t\t\tHello, Welcome to the lincoln library")
    for i in range(5):
        print(".", end='')
        time.sleep(0.05)

    typingPrint("\n\n\n\t\t\t\t\t\t\t\tPlease fill in the following fields.\n\n")
    time.sleep(1)
    input_data()


def set_key():
    """Set the password."""
    global password_1
    global password_2
    global count

    while password_2 != password_1:
        if count > 0:
            print("\n\nconfirmation error!\n\n")
            time.sleep(1)
        password_1 = input("Create password:")
        password_2 = input("Confirm password:")
        count += 1

    return password_2


def input_data():
    """Collect the user's personal data."""
    first_name = input("\n\t\t\t\t\t\t\t\t\t > First Name:").title()
    last_name = input("\n\t\t\t\t\t\t\t\t\t > Last Name:").title()
    ID_no = input(str("\n\t\t\t\t\t\t\t\t\t > ID_no:"))
    year_of_registration = input(str("\n\t\t\t\t\t\t\t\t\t > year of registration:"))

    registration_no = "LL|" + str(random.randint(1000, 10000)) + "|" + year_of_registration
    print("\n\t\t\t\t\t\t\t\t\t > Your registration number: ", registration_no)

    my_password = set_key()

    pick_save.add_user_to_sql_database(first_name, last_name, year_of_registration, registration_no, my_password)

    print("\n\n\t\t\t\t\t\t\t\t\t\t\a\a >>>>> Password saved >>>>>>")
    print("\n\n\t\t\t\t\t\t\t\t\t\t\a\a ****** Registration success! ******")

    # Go back to main menu.
    choice = input(str("Enter 1 to return to menu or 0 to exit: "))
    if choice == '1':
        pass
    elif choice == '0':
        ea.leave()
