"""A module containing all functions related to a book"""
import random
from os import system
from time import sleep
from datetime import date, timedelta

import pick_save
from book import Book
import exit_application as ea


# Add a book to the library catalogue
# Only an admin can do this.
def book_home():
    """Print the welcome page."""
    system("cls")
    system('color 0A')
    print("\n\n\n\t\t\t\t\t\t\t\t Hello, Welcome to the lincoln library!")
    print("\n\n\t\t\t\t\t\t\t\t   Fill in the fields to add a book:")

    # Book details
    title = input("\n\t\t\t\t\t\t\t\t\t\tTitle: ")
    author = input("\n\t\t\t\t\t\t\t\t\t\tauthor: ")
    genre = input("\n\t\t\t\t\t\t\t\t\t\tgenre: ")
    publication_year = input("\n\t\t\t\t\t\t\t\t\t\tpublication year: ")

    ISBN = random.randint(1000000000000, 10000000000000)

    book_add(title, author, genre, ISBN, publication_year)
    print("Book added!!!")
    sleep(3)


def book_add(title, author, genre, ISBN, publication_year):
    """ Add the book to the catalogue."""
    # Load the empty list from the pkl file
    book_list = pick_save.load_object('book_list.pkl')

    # Create an instance of Book using data taken
    book = Book(title, author, genre, ISBN, publication_year)

    # Append the book_dict attribute to the empty list
    book_list.append(book.book_dict)

    # Save the list containing book_dict to the pkl file
    pick_save.save_object(book_list, 'book_list.pkl')


def view_catalogue(first_name):
    """View the available books."""
    system('cls')
    books = pick_save.load_object('book_list.pkl')
    system('color 0B')
    # Print the list
    for book in books:
        for key, value in book.items():
            if key == 'Title':
                key = key.upper()
                value = value.upper()
                print("\t" + key + ": " + value + "\n")
            else:
                print("\t  >" + key + ": ", value, "\n")
        print("\n\n")

    ea.return_main_menu(first_name)


def borrow_book(first_name):
    """Borrow a book."""
    book_exists_flag = False
    system('color 0B')
    system('cls')
    library_users = pick_save.load_object('library_users.pkl')
    books = pick_save.load_object('book_list.pkl')
    my_book = input("\n\t\t\t\t\t\t\t\t\t\tEnter book title to borrow: ").title()

    # Check whether the book exists
    book_exists_flag = book_exists(book_exists_flag, books, first_name, my_book)
    if book_exists_flag:

        # Use the title to edit the borrow status of the book
        for book in books:
            for key, value in book.items():
                if value == my_book:
                    for library_user in library_users:
                        if library_user.first_name == first_name:
                            clear_to_borrow(library_user, book, first_name)
                            library_user.books_borrowed_list.append(value)
                    book['Borrow status'] = 'on loan'

                    # Set the return date to 3 weeks from today
                    book['Return Date'] = date.today() + timedelta(weeks=3)

                    print("Book loan successful!!")
                    sleep(3)

                    # The edited lists are saved and overwritten on the existing pkl file.
                    pick_save.save_object(library_users, 'library_users.pkl')
                    pick_save.save_object(books, 'book_list.pkl')

    ea.return_main_menu(first_name)


def book_exists(book_exists_flag, books, first_name, my_book):
    """check if book exists"""
    for book in books:
        for key, value in book.items():
            if value == my_book:
                book_exists_flag = True

    if book_exists_flag:
        return book_exists_flag
    else:
        print("Book not in catalogue!")
        sleep(3)
        ea.return_main_menu(first_name)


def clear_to_borrow(library_user, book, first_name):
    """
     This module checks 3 things.
     1.if the book exists
     2.the book is available,
     3.the loan limit of 3 books is not exceeded
     4.no overdue balance exists.
    """
    # Check if book is available
    if book['Borrow status'] == 'on loan':
        print("Book is on loan.!!!")
        sleep(3)
        ea.return_main_menu(first_name)

    # Check if the user has borrowed more than 3 books
    if len(library_user.books_borrowed_list) > 2:
        print("you have borrowed the maximum-3 books!!")
        sleep(3)
        ea.return_main_menu(first_name)

    # check if there is any debt
    elif library_user.debt_to_library > 0:
        print("You have an overdue of sh." + str(library_user.debt_to_library))
        sleep(3)
        ea.return_main_menu(first_name)


def return_book(first_name):
    """Return a book."""
    overdue = 0
    system("cls")
    system('color 0B')
    library_users = pick_save.load_object('library_users.pkl')
    books = pick_save.load_object('book_list.pkl')
    my_book = input("\n\t\t\t\t\t\t\t\t\t\tEnter book title to return: ").title()

    # Use the title to edit the borrow status of the book
    for book in books:
        for key, value in book.items():
            if value == my_book:
                # Check if book is overdue.
                # each week overdue a fine of sh.140 is charged
                if date.today() > book['Return Date']:
                    overdue = ((date.today() - book.return_date) / 7) * 140
                book['Borrow status'] = 'Available'
                book['Return Date'] = 'null'
                print("Book return successful!!")
                sleep(3)

    for library_user in library_users:
        if library_user.first_name == first_name:
            # Remove book from users account
            if my_book in library_user.books_borrowed_list:
                library_user.debt_to_library += overdue
                library_user.books_borrowed_list.remove(my_book)

    # The edited lists are saved and overwritten on the existing pkl file.
    pick_save.save_object(library_users, 'library_users.pkl')
    pick_save.save_object(books, 'book_list.pkl')

    ea.return_main_menu(first_name)


def clear_overdue(first_name):
    """Just reset the debt_to_library to 0."""
    library_users = pick_save.load_object('library_users.pkl')
    for library_user in library_users:
        if library_user.first_name == first_name:
            library_user.debt_to_library = 0
            print("Cleared!!")
            sleep(3)

    pick_save.save_object(library_users, 'library_users.pkl')

    ea.return_main_menu(first_name)

