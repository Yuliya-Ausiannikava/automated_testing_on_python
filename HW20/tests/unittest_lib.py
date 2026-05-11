"""
Test module for a library application
"""

import unittest
import logging
import hw12_library

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - '
                                                '%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Tests for the Book class
class TestLibraryApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.disable(logging.CRITICAL)
        logger.info("Starting Library App Tests")

    @classmethod
    def tearDownClass(cls):
        logging.disable(logging.NOTSET)
        logger.info("Ending Library App Tests")

    def setUp(self):
        logger.info('Setting up test environment')

        self.book1 = hw12_library.Book(
            book_name="The Hobbit",
            author="Books by J.R.R. Tolkien",
            num_pages=400,
            isbn="0006754023"
        )

        self.book2 = hw12_library.Book(
            book_name="A Good Year",
            author="Peter Mayle",
            num_pages=320,
            isbn="9785389173118"
        )

        self.reader1 = hw12_library.Reader("VASYA")
        self.reader2 = hw12_library.Reader("PETYA")

        logger.info("Test environment set up successfully")

    def tearDown(self):
        logger.info('Tearing down test environment')

        del self.book1
        del self.book2
        del self.reader1
        del self.reader2

        logger.info('Test environment tear down successfully')

    # Book and Reader Creation Tests
    def test_book_creation(self):
        logger.info('Testing book creation successful')

        self.assertEqual(self.book1.book_name, "The Hobbit")
        self.assertEqual(self.book1.author, "Books by J.R.R. Tolkien")
        self.assertEqual(self.book1.num_pages, 400)
        self.assertEqual(self.book1.isbn, "0006754023")
        self.assertEqual(self.book2.book_name, "A Good Year")
        self.assertEqual(self.book2.author, "Peter Mayle")
        self.assertEqual(self.book2.num_pages, 320)
        self.assertEqual(self.book2.isbn, "9785389173118")

        logger.debug('Books creation successful')
        logger.info('Testing book creation successfully test passed')

    def test_reader_creation(self):
        logger.info('Testing reader creation successful')

        self.assertEqual(self.reader1.name, "VASYA")
        self.assertEqual(self.reader2.name, "PETYA")

        logger.debug('Readers creation successful')
        logger.info('Testing reader creation successful test passed')

    # Book reservation tests
    def test_book_reservation(self):
        logger.info('Testing the free book reservation function '
                    '(including testing multiple reservations by '
                    'different users of different books)')

        self.reader1.reserve_book(self.book1)
        self.reader2.reserve_book(self.book2)
        self.assertEqual(self.book1.is_reserved_book, self.reader1)
        self.assertEqual(self.book2.is_reserved_book, self.reader2)

        logger.debug('Free book reservation successful')
        logger.info('Testing reserve book successful test passed')

    def test_book_reservation_twice(self):
        logger.info('Testing reserving the same book twice by the same user')

        self.reader1.reserve_book(self.book1)
        self.assertEqual(self.book1.is_reserved_book, self.reader1)

        logger.debug('Attempting to reserve the same book '
                     'by a reader more than once should result in an error')
        with self.assertRaises(PermissionError) as context:
            self.reader1.reserve_book(self.book1)
        self.assertEqual(str(context.exception), 'User can not reserve a book. '
                                                 'Another reader has already taken this book.')

        logger.info('Book reservation test passed twice')

    def test_reserved_book_reservation(self):
        logger.info('Testing the reservation of a book that was reserved by another user')

        self.reader1.reserve_book(self.book1)

        logger.debug('Attempting to reserve a book that is already reserved '
                     'by another reader should result in an error')
        with self.assertRaises(PermissionError) as context:
            self.reader2.reserve_book(self.book1)
        self.assertEqual(str(context.exception), 'User can not reserve a book. '
                                                 'Another reader has already taken this book.')

        logger.info('Testing the reservation of a reserved book test passed')

    def test_taken_book_reservation(self):
        logger.info('Testing the reservation of a book that was taken by another user')

        self.reader1.reserve_book(self.book1)
        self.reader1.get_book(self.book1)

        logger.debug('Attempting to reserve a book that was already taken by '
                     'another user should result in an error')
        with self.assertRaises(PermissionError) as context:
            self.reader2.reserve_book(self.book1)
        self.assertEqual(str(context.exception), 'User can not reserve a book. '
                                                 'Another reader has already taken this book.')

        logger.info('Testing the reservation of a book '
                    'that was taken by another user test passed')

    # Tests for removing books from reserve
    def test_cancel_reservation(self):
        logger.info('Testing the cancel reservation of a book')

        self.reader1.reserve_book(self.book1)
        self.assertEqual(self.book1.is_reserved_book, self.reader1)
        self.reader1.cancel_reserve(self.book1)
        self.assertIsNone(self.book1.is_reserved_book)

        logger.info('Testing the cancel reservation of a book test passed')

    def test_cancel_reservation_twice(self):
        logger.info('Testing the cancel reservation of a book twice by the same user')

        self.reader1.reserve_book(self.book1)
        self.assertEqual(self.book1.is_reserved_book, self.reader1)
        self.reader1.cancel_reserve(self.book1)
        self.assertIsNone(self.book1.is_reserved_book)

        logger.debug('Attempting to cancel a book reservation twice '
                     'by the same reader should result in an error')
        with self.assertRaises(PermissionError) as context:
            self.reader1.cancel_reserve(self.book1)
        self.assertEqual(str(context.exception), "VASYA can not cancel a book, "
                                                 "because he didn't reserve it")

        logger.info('Cancellation test passed twice')

    def test_cancel_reservation_without_reservation(self):
        logger.info('Testing cancellation of a book reservation by a user who did not reserve it')

        logger.debug('Attempting to cancel a book reservation '
                     'by a user who did not reserve it should result in an error')
        with self.assertRaises(PermissionError) as context:
            self.reader1.cancel_reserve(self.book1)
        self.assertEqual(str(context.exception), "VASYA can not cancel a book, "
                                                 "because he didn't reserve it")

        logger.info('The reader was unable to return a book they had not reserved. Test passed.')

    # Tests for obtaining books
    def test_get_book(self):
        logger.info('Testing the get_book function (Including several readers)')

        self.reader1.reserve_book(self.book1)
        self.assertEqual(self.book1.is_reserved_book, self.reader1)
        self.reader1.get_book(self.book1)
        self.assertEqual(self.book1.is_get_book, self.reader1)
        self.assertIsNone(self.book1.is_reserved_book)
        self.reader2.reserve_book(self.book2)
        self.assertEqual(self.book2.is_reserved_book, self.reader2)
        self.reader2.get_book(self.book2)
        self.assertEqual(self.book2.is_get_book, self.reader2)
        self.assertIsNone(self.book2.is_reserved_book)

        logger.info('The get book function test passed')

    def test_get_book_reserved_another_user(self):
        logger.info('Testing the function of retrieving '
                    'a book that is reserved by another user')

        self.reader1.reserve_book(self.book2)

        logger.debug('Attempting to get a book that is reserved '
                     'by another user should result in an error')
        with self.assertRaises(PermissionError) as context:
            self.reader2.get_book(self.book2)
        self.assertEqual(str(context.exception), "PETYA can not get a book 'A Good Year'")

        logger.info('The test for retrieving a book '
                    'reserved by another user has been passed')

    def test_get_book_received_another_user(self):
        logger.info('Testing the function of retrieving '
                    'a book that is received by another user')

        self.reader1.reserve_book(self.book2)
        self.assertEqual(self.book2.is_reserved_book, self.reader1)
        self.reader1.get_book(self.book2)
        self.assertEqual(self.book2.is_get_book, self.reader1)

        logger.debug('Attempting to get a book that is received '
                     'by another user should result in an error')
        with self.assertRaises(PermissionError) as context:
            self.reader1.get_book(self.book2)
        self.assertEqual(str(context.exception), "VASYA can not get a book 'A Good Year'")

        logger.info('The test for retrieving a book that is '
                    'received by another user has been passed')

    # Book Return Tests
    def test_return_book(self):
        logger.info('Testing the successfully return of a book')

        self.reader1.reserve_book(self.book1)
        self.assertEqual(self.book1.is_reserved_book, self.reader1)
        self.reader1.get_book(self.book1)
        self.assertIsNone(self.book1.is_reserved_book)
        self.assertEqual(self.book1.is_get_book, self.reader1)
        self.reader1.return_book(self.book1)
        self.assertIsNone(self.book1.is_get_book)

        logger.info('Return of the book test passed')

    def test_return_book_not_take1(self):
        logger.info('Testing the return of a book that the user did not take but reserved')

        self.reader1.reserve_book(self.book1)
        self.assertEqual(self.book1.is_reserved_book, self.reader1)

        logger.debug('Attempts to return a book that the user '
                     'did not borrow but reserved should result in an error')
        with self.assertRaises(PermissionError) as context:
            self.reader1.return_book(self.book1)
        self.assertEqual(str(context.exception), "VASYA can not return a book 'The Hobbit', "
                                                 "because he didn't take it")

        logger.info('Returning a book that was reserved but not taken, the test passed')

    def test_return_book_not_take2(self):
        logger.info('Testing the return of a book that the user did not take or reserve')

        logger.debug('Attempting to return a book that the user '
                     'did not take or reserved should result in an error')
        with self.assertRaises(PermissionError) as context:
            self.reader1.return_book(self.book1)
        self.assertEqual(str(context.exception), "VASYA can not return a book 'The Hobbit', "
                                                 "because he didn't take it")


if __name__ == '__main__':
    unittest.main()
