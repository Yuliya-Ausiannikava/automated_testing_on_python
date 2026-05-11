"""
A program to assist the library was written. Two classes were created.
"""

import logging

logger = logging.getLogger("my_logger")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class Book:

    def __init__(self, book_name, author, num_pages, isbn):
        self.is_reserved_book = None
        self.is_get_book = None
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        logger.debug("Created book %s, author %s", book_name, author)

    def reserve(self, reader_name):
        if self.is_reserved_book is None and self.is_get_book is None:
            self.is_reserved_book = reader_name
            logger.info("The book '%s' has been reserved by the user %s",
                        self.book_name, reader_name.name)
        else:
            raise PermissionError('User can not reserve a book. '
                                  'Another reader has already taken this book.')

    def cancel_reserve(self, reader_name):
        if self.is_reserved_book == reader_name:
            self.is_reserved_book = None
            logger.info("The book '%s' has been cancelled by the user %s",
                        self.book_name, reader_name.name)
        else:
            raise PermissionError(f"{reader_name.name} can not cancel a book, "
                                  f"because he didn't reserve it")

    def get_book(self, reader_name):
        if (self.is_get_book is None and
                (self.is_reserved_book is None or self.is_reserved_book == reader_name)):
            self.is_get_book = reader_name
            self.is_reserved_book = None
            logger.info("The book '%s' was taken by reader %s",
                        self.book_name, reader_name.name)
        else:
            raise PermissionError(f"{reader_name.name} can not get a book '{self.book_name}'")

    def return_book(self, reader_name):
        if self.is_get_book == reader_name:
            self.is_get_book = None
            logger.info("The book '%s' was returned", self.book_name)
        else:
            raise PermissionError(f"{reader_name.name} can not return a book '{self.book_name}', "
                  "because he didn't take it")


class Reader:

    def __init__(self, name):
        self.name = name
        logger.debug("Created reader %s", name)

    def reserve_book(self, book):
        book.reserve(self)

    def cancel_reserve(self, book):
        book.cancel_reserve(self)

    def get_book(self, book):
        book.get_book(self)

    def return_book(self, book):
        book.return_book(self)
