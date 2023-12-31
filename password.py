import os
from time import sleep

import exit_application as ea
import interface_functions as int_fs
import registration as reg
import pick_save

# We set the root pass word here
password_1 = 'x'
password_2 = 'y'
count = 0


def get_password(first_name):
    """Retrieve the password from the sql user table ."""
    member = first_name

    user_flag = pick_save.confirm_user_exists(first_name)

    if user_flag:
        password_key = pick_save.get_password_from_sql(first_name)
        user_password_comp(password_key)

        # Move verified user to member interface
        int_fs.member_home(member)
    else:
        print("\n\n\t\t\t\t\t\t\t\t\t\tError: Username does not exist. Please register first!")
        sleep(3)
        reg.home_page()


def user_password_comp(root_password):
    """check for a password match."""
    # Compare root_password with password
    os.system('cls')
    os.system('color 0A')
    password = input("\n\n\t\t\t\t\t\t\t\t\t\tEnter password: ")
    if password == root_password:
        print("\n\n\t\t\t\t\t\t\t\t\t\tprocessing data", end='')
        for i in range(4):
            print("", end='.')
            sleep(1.0)
        print("\n\n\t\t\t\t\t\t\t\t\t\tpassword match!")

    elif password != root_password:
        print("password Incorrect!")
        pass_flag = input(str("\n\n\t\t\t\t\t\t\t\t\t\tEnter 1 to try again and 0 to exit: "))
        if pass_flag == '1':
            user_password_comp(root_password)
        elif pass_flag == '0':
            ea.leave()


def admin_password_comp():
    """Verify admin login."""
    passcode = input("\n\n\t\t\t\t\t\t\t\t\t\tEnter password: ")

    if passcode == 'admin123':
        print("\n\n\t\t\t\t\t\t\t\t\t\tprocessing data", end='')
        for i in range(4):
            print("", end='.')
            sleep(1.0)
        print("\n\n\t\t\t\t\t\t\t\t\t\tpassword match!")
        int_fs.admin_home()

    elif passcode != 'admin123':
        print("password Incorrect!")
        pass_flag = input(str("\n\n\t\t\t\t\t\t\t\t\t\tEnter 1 to try again and 0 to exit: "))
        if pass_flag == '1':
            admin_password_comp()
        elif pass_flag == '0':
            ea.leave()
