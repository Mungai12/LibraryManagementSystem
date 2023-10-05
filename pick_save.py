"""
This is a very important module.It controls the database of the program
tweak things here wisely!!
"""

import psycopg2
from time import sleep
from os import system
import exit_application as ea
import interface_functions as int_fs
from datetime import date, timedelta

#
# def save_object(obj, filename):
#     """Save the object to the pickle file."""
#     with open(filename, 'wb') as outp:  # Overwrites any existing file.
#         pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)
#
#
# def load_object(filename):
#     """Load the object from the pickle file and return it to caller."""
#     with open(filename, 'rb') as inp:
#         obj = pickle.load(inp)
#     return obj

#
# def create_user_list():
#     """Make the list once and never enter the function again."""
#     library_users = []
#     save_object(library_users, 'library_users.pkl')
#
#     choice = input(str("Enter (1) to return to menu or (0) to exit: "))
#     if choice == '1':
#         pass
#     elif choice == '0':
#         ea.leave()
#
#
# def create_book_list():
#     """Make the list once and never enter the function again."""
#     book_list = []
#     save_object(book_list, 'book_list.pkl')
#     print("File created!")
#     sleep(3)
#     int_fs.admin_home()


def add_user_to_sql_database(first_name, last_name, year_of_registration, registration_no, password):
    """Add a user to sql"""
    book_1 = None
    book_2 = None
    book_3 = None
    conn = psycopg2.connect(dbname='lincoln_library', user='postgres', host='localhost', password='Akkada_AI')

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO users(first_name, last_name, year_of_registration, registration_number, password, book_1, book_2, book_3)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s);""",
        (first_name, last_name, year_of_registration, registration_no, password, book_1, book_2, book_3))

    conn.commit()
    cur.close()
    conn.close()


def view_user_detail(first_name):
    """See the details of a specific user."""
    system('cls')
    system('color 0B')

    conn = psycopg2.connect(dbname='lincoln_library', user='postgres', host='localhost', password='Akkada_AI')
    cur = conn.cursor()

    cur.execute("""SELECT * FROM users WHERE first_name = %s;""", (first_name,))

    user = cur.fetchone()

    print("\n\t\t\t\t", 'First_name: ', user[1])
    print("\n\t\t\t\t", 'Last_name: ', user[2])
    print("\n\t\t\t\t", 'Y.O.G: ', user[3])
    print("\n\t\t\t\t", 'Registration_no: ', user[4])
    print("\n\t\t\t\t", 'Password: ', user[5])
    print("\n\t\t\t\t", 'Book_1: ', user[6])
    print("\n\t\t\t\t", 'Book_2: ', user[7])
    print("\n\t\t\t\t", 'Book_3: ', user[8])
    print("\n\n")

    conn.commit()
    cur.close()
    conn.close()

    choice = input(str("Enter 1 to return to menu or 0 to exit: "))
    if choice == '1':
        pass
    elif choice == '0':
        ea.leave()


def get_password_from_sql(first_name):
    """Retrieve the pass word from the database."""

    conn = psycopg2.connect(dbname='lincoln_library', user='postgres', host='localhost', password='Akkada_AI')

    cur = conn.cursor()

    cur.execute("""SELECT password FROM users WHERE first_name = %s;""", (first_name,))
    password = cur.fetchone()

    conn.commit()
    cur.close()
    conn.close()

    return password[0]


def confirm_user_exists(first_name):
    """Check Whether the user is in the database."""
    conn = psycopg2.connect(dbname='lincoln_library', user='postgres', host='localhost', password='Akkada_AI')

    cur = conn.cursor()

    cur.execute("""SELECT EXISTS(SELECT 1 FROM users WHERE first_name = %s);""", (first_name,))

    user_exists_flag = cur.fetchone()

    conn.commit()
    cur.close()
    conn.close()

    return user_exists_flag[0]


def add_book_to_sql_database(title, author, genre, isbn, year_of_publication):
    """Add the book to sql."""

    conn = psycopg2.connect(dbname='lincoln_library', user='postgres', host='localhost', password='Akkada_AI')

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO books(title, author, genre, isbn, year_of_publication, borrow_status, return_date)
        VALUES(%s, %s, %s, %s, %s, %s, %s);""",
        (title, author, genre, isbn, year_of_publication, 'Available', None))

    conn.commit()
    cur.close()
    conn.close()


def see_catalogue():
    """Retrieve the book list from the sql database and format it."""
    conn = psycopg2.connect(dbname='lincoln_library', user='postgres', host='localhost', password='Akkada_AI')
    cur = conn.cursor()

    cur.execute("""SELECT * FROM books
                    ORDER BY id ASC;""")

    books = cur.fetchall()

    for book in books:
        print("\n\t\t\t\t", 'TITLE: ', book[1])
        print("\n\t\t\t\t", 'Author: ', book[2])
        print("\n\t\t\t\t", 'Genre: ', book[3])
        print("\n\t\t\t\t", 'Isbn: ', book[4])
        print("\n\t\t\t\t", 'Y.O.P: ', book[5])
        print("\n\t\t\t\t", 'Borrow status: ', book[6])
        print("\n\t\t\t\t", 'Return date: ', book[7])
        print("\n\n")

    conn.commit()
    cur.close()
    conn.close()


def confirm_book_in_catalogue(my_book):
    conn = psycopg2.connect(dbname='lincoln_library', user='postgres', host='localhost', password='Akkada_AI')

    cur = conn.cursor()

    cur.execute("""SELECT EXISTS(SELECT 1 FROM books WHERE title = %s);""", (my_book,))

    book_exists_flag = cur.fetchone()
    print(book_exists_flag[0])

    conn.commit()
    cur.close()
    conn.close()

    return book_exists_flag[0]


def borrow_book(first_name, my_book):
    """change a book's sql details to be like loaned."""
    # Use the title to edit the borrow status of the book
    conn = psycopg2.connect(dbname='lincoln_library', user='postgres', host='localhost', password='Akkada_AI')

    cur = conn.cursor()

    cur.execute(
        """
        UPDATE users 
        SET book_1 = %s
        WHERE first_name = %s;""",
        (my_book, first_name))
    # set return date to 3 weeks later
    return_date = date.today() + timedelta(weeks=3)

    cur.execute(
        """
        UPDATE books
        SET return_date = %s,
            borrow_status = 'On Loan'
        WHERE title = %s;""", (return_date, my_book))

    conn.commit()
    cur.close()
    conn.close()


def return_book(first_name, my_book):
    """change a book's sql details to be like loaned."""
    # Use the title to edit the borrow status of the book
    conn = psycopg2.connect(dbname='lincoln_library', user='postgres', host='localhost', password='Akkada_AI')

    cur = conn.cursor()

    cur.execute(
        """
        UPDATE users 
        SET book_1 = null
        WHERE first_name = %s;""",
        (first_name,))

    cur.execute(
        """
        UPDATE books
        SET return_date = null,
            borrow_status = 'Available'
        WHERE title = %s;""", (my_book,))

    conn.commit()
    cur.close()
    conn.close()
