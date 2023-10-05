"""A module containing all functions related to a book"""
import random

from os import system
from time import sleep
import psycopg2

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
    title = input("\n\t\t\t\t\t\t\t\t\t\tTitle: ").upper()
    author = input("\n\t\t\t\t\t\t\t\t\t\tauthor: ").title()
    genre = input("\n\t\t\t\t\t\t\t\t\t\tgenre: ").title()
    publication_year = input("\n\t\t\t\t\t\t\t\t\t\tpublication year: ")
    ISBN = random.randint(1000000000000, 10000000000000)

    book_add(title, author, genre, ISBN, publication_year)
    print("Book added!!!")
    sleep(3)


def book_add(title, author, genre, ISBN, publication_year):
    """ Add the book to the catalogue."""
    pick_save.add_book_to_sql_database(title, author, genre, ISBN, publication_year)


def view_catalogue(first_name):
    """View the available books."""
    system('cls')
    system('color 0B')
    pick_save.see_catalogue()

    ea.return_main_menu(first_name)


def borrow_book(first_name):
    """Borrow a book."""
    system('color 0B')
    system('cls')
    my_book = input("\n\t\t\t\t\t\t\t\t\t\tEnter book title to borrow: ").upper()

    # Check whether the book exists
    book_exists_flag = book_exists(my_book, first_name)
    if book_exists_flag:
        pick_save.borrow_book(first_name, my_book)
        print("Book loan successful!!")
        sleep(3)

    ea.return_main_menu(first_name)


def book_exists(my_book, first_name):
    """
       This module should check 4 things but checks only one for now because am bored
       with this good for nothing project.
     1.if the book exists
     2.the book is available,
     3.the loan limit of 3 books is not exceeded
     4.no overdue balance exists.
    """
    book_flag = pick_save.confirm_book_in_catalogue(my_book)

    if book_flag:
        return book_flag
    else:
        print("Book not in catalogue!")
        sleep(3)
        ea.return_main_menu(first_name)


def return_book(first_name):
    """Return a book."""
    system("cls")
    system('color 0B')
    my_book = input("\n\t\t\t\t\t\t\t\t\t\tEnter book title to return: ").upper()

    # Use the title to edit the borrow status of the book
    # Check if book is overdue.
    # each week overdue a fine of sh.140 is charged
    # if date.today() > book['Return Date']:
    #     overdue = ((date.today() - book.return_date) / 7) * 140

    pick_save.return_book(first_name, my_book)
    print("Book return successful!!")
    sleep(3)

    ea.return_main_menu(first_name)

