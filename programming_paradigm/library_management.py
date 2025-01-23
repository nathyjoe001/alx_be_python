class Book:
    def __init__(self, title, author):
        """
        Initialize a Book instance with a title, author, and its availability.
        :param title: Title of the book.
        :param author: Author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Mark the book as checked out.
        """
        if self._is_checked_out:
            return False  # Book is already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """
        Mark the book as returned (available).
        """
        if not self._is_checked_out:
            return False  # Book is already available
        self._is_checked_out = False
        return True

    def is_available(self):
        """
        Check if the book is available.
        :return: True if the book is not checked out, False otherwise.
        """
        return not self._is_checked_out


class Library:
    def __init__(self):
        """
        Initialize a Library instance with an empty collection of books.
        """
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Add a Book instance to the library's collection.
        :param book: Book object to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title, marking it as unavailable.
        :param title: Title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                return
        print(f"'{title}' is either unavailable or not in the library.")

    def return_book(self, title):
        """
        Return a book by title, marking it as available.
        :param title: Title of the book to return.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"'{title}' has been returned.")
                return
        print(f"'{title}' is either not checked out or not in the library.")

    def list_available_books(self):
        """
        Print the list of books that are available for checkout.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
