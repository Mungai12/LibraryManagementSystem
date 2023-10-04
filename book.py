class Book:
    """A class modelling a library book."""

    def __init__(self, title, author, genre, ISBN, publication_year):
        # Initialize book attributes
        self.title = title.title()
        self.author = author.title()
        self.genre = genre.title()
        self.ISBN = str(ISBN)
        self.publication_year = str(publication_year)

        # Initialize dynamic attributes; that can change within runtime
        self.borrow_status = 'available'
        self.return_date = 'null'

        # This dictionary should contain all the books info
        self.book_dict = {
                          'Title': self.title,
                          'Author': self.author,
                          'Genre': self.genre,
                          'ISBN': self.ISBN,
                          'Publication_year': self.publication_year,
                          'Borrow status': self.borrow_status,
                          'Return Date': self.return_date,
                          }

