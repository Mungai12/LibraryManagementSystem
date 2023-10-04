from os import system
import pick_save
import exit_application as ea


class User:
    """A class modelling a library user."""

    def __init__(self, first_name, last_name, ID_no, year, registration_number, password):
        # Initialize the user attributes.
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_registration = year
        self.ID_no = ID_no
        self.registration_number = registration_number
        self.password = password

        # Initialize  user's dynamic attributes i.e can change during runtime
        self.books_borrowed_list = []
        self.debt_to_library = 0

        # this dictionary contains the users information
        self.user_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'year_of_registration': self.year_of_registration,
            'ID_no': self.ID_no,
            'registration_number': self.registration_number,
            'password': self.password,
            'books_borrowed_list': self.books_borrowed_list,
            'debt_to_library': self.debt_to_library,
        }


def view_details(me):
    """
    Show my user details, books I have borrowed and money I owe
    to the library if any.
    """
    system('cls')
    system('color 0B')
    library_users = pick_save.load_object('library_users.pkl')

    for library_user in library_users:
        if library_user.first_name == me:
            print("\n\n\t\t\t\t\t\t\t\t  ****** ACCOUNT DETAILS ******\n")
            for key, value in library_user.user_dict.items():
                if key == 'books_borrowed_list':
                    print("\n\n\t\t\t\t\t\t\t\t\t>>>> BOOKS LOANED <<<<\n")
                    for book in library_user.books_borrowed_list:
                        print("\t\t\t\t\t\t\t\t\t\t.", book)
                elif key == 'debt_to_library':
                    print("\n\n\t\t\t\t\t\t\t\t\t   OVERDUE BALANCE: ", library_user.debt_to_library)

                else:
                    print("\t\t\t\t\t\t\t\t\t", key.title() + ":", value)

    choice = input(str("Enter 1 to return to menu or 0 to exit: "))
    if choice == '1':
        pass
    elif choice == '0':
        ea.leave()

