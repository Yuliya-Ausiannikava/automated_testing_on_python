import pytest
from hw_12 import hw12_library
from logging_config import get_logger

logger = get_logger(__name__)


@pytest.fixture(scope="function")
def library():
    logger.info('Setting up test environment')

    book1 = hw12_library.Book(
        book_name="The Hobbit",
        author="J.R.R. Tolkien",
        num_pages=400,
        isbn="0006754023"
    )
    book2 = hw12_library.Book(
        book_name="A Good Year",
        author="Peter Mayle",
        num_pages=320,
        isbn="9785389173118"
    )

    reader1 = hw12_library.Reader("VASYA")
    reader2 = hw12_library.Reader("PETYA")

    logger.info("Test environment set up successfully")

    yield {
        'book1': book1,
        'book2': book2,
        'reader1': reader1,
        'reader2': reader2
    }


@pytest.fixture(scope="session", autouse=True)
def library_session():
    logger.info("Starting Library App Tests")
    yield
    logger.info("Ending Library App Tests")


# Book and Reader Creation Tests
@pytest.mark.smoke
@pytest.mark.regression
def test_book_creation(library):
    logger.info('Testing book creation successful')

    book_1 = library['book1']
    book_2 = library['book2']
    assert book_1.book_name == "The Hobbit"
    assert book_1.author == "J.R.R. Tolkien"
    assert book_1.isbn == "0006754023"
    assert book_1.num_pages == 400
    assert book_2.book_name == "A Good Year"
    assert book_2.author == "Peter Mayle"
    assert book_2.isbn == "9785389173118"
    assert book_2.num_pages == 320

    logger.debug('Books creation successful')
    logger.info('Testing book creation successfully test passed')


@pytest.mark.smoke
@pytest.mark.regression
def test_reader_creation(library):
    logger.info('Testing reader creation successful')

    reader_1 = library['reader1']
    reader_2 = library['reader2']
    assert reader_1.name == "VASYA"
    assert reader_2.name == "PETYA"

    logger.debug('Readers creation successful')
    logger.info('Testing reader creation successful test passed')


# Book reservation tests
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.reservation_book
def test_book_reservation(mocker, library):
    logger.info('Testing the successful reservation of one book (USE MOCK)')

    reader = library['reader1']
    mock_book = mocker.Mock()

    reader.reserve_book(mock_book)
    mock_book.reserve.assert_called_once_with(reader)

    logger.debug('The books are reserved')
    logger.info('Testing reserve book successful test passed')


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.reservation_book
def test_books_reservation_multiple(mocker, library):
    logger.info('Testing the successful reservation of several books by one reader (use MOCK)')

    reader_1 = library['reader1']
    reader_2 = library['reader2']
    mock_book1 = mocker.Mock()
    mock_book2 = mocker.Mock()

    reader_1.reserve_book(mock_book1)
    reader_2.reserve_book(mock_book2)
    mock_book1.reserve.assert_called_once_with(reader_1)
    mock_book2.reserve.assert_called_once_with(reader_2)

    logger.debug('The books are reserved')
    logger.info('Checking the reservations of different books by different readers was successful')


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.reservation_book
def test_diff_books_reservation_one_reader(mocker, library):
    logger.info('Testing the reservation of different books by one reader')

    reader_1 = library['reader1']
    mock_book1 = mocker.Mock()
    mock_book2 = mocker.Mock()
    reader_1.reserve_book(mock_book1)
    reader_1.reserve_book(mock_book2)
    mock_book1.reserve.assert_called_once_with(reader_1)
    mock_book2.reserve.assert_called_once_with(reader_1)

    logger.debug('The books are reserved')
    logger.info('Checking the reservations of different books by one reader was successful')


@pytest.mark.negative
@pytest.mark.reservation_book
def test_book_reservation_twice(library):
    logger.info('Testing reserving the same book twice by the same user')

    reader_1 = library['reader1']
    book_1 = library['book1']
    reader_1.reserve_book(book_1)

    logger.debug('Attempting to reserve the same book '
                 'by a reader more than once should result in an error')
    with pytest.raises(PermissionError) as context:
        reader_1.reserve_book(book_1)
    assert str(context.value) == ("User can not reserve a book. "
                                  "Another reader has already taken this book.")

    logger.info('Book reservation test passed twice')


@pytest.mark.negative
@pytest.mark.reservation_book
def test_reserved_book_reservation(library):
    logger.info('Testing the reservation of a book that was reserved by another user')

    reader_1 = library['reader1']
    reader_2 = library['reader2']
    book_1 = library['book1']
    reader_1.reserve_book(book_1)

    logger.debug('Attempting to reserve a book that is already reserved '
                 'by another reader should result in an error')
    with pytest.raises(PermissionError) as context:
        reader_2.reserve_book(book_1)
    assert str(context.value) == ("User can not reserve a book. "
                                  "Another reader has already taken this book.")

    logger.info('Testing the reservation of a reserved book test passed')


@pytest.mark.negative
@pytest.mark.reservation_book
def test_taken_book_reservation(library):
    logger.info('Testing the reservation of a book that was taken by another user')

    reader_1 = library['reader1']
    reader_2 = library['reader2']
    book_1 = library['book1']
    reader_1.reserve_book(book_1)
    reader_1.get_book(book_1)

    logger.debug('Attempting to reserve a book that was already taken by '
                 'another user should result in an error')
    with pytest.raises(PermissionError) as context:
        reader_2.reserve_book(book_1)
    assert str(context.value) == ("User can not reserve a book. "
                                  "Another reader has already taken this book.")

    logger.info('Testing the reservation of a book '
                'that was taken by another user test passed')


# Tests for removing books from reserve
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cancel_reservation
def test_cancel_reservation(mocker, library):
    logger.info('Testing the cancel reservation of a book (use MOCK)')

    reader_1 = library['reader1']
    mock_book = mocker.Mock()

    reader_1.reserve_book(mock_book)
    reader_1.cancel_reserve(mock_book)
    mock_book.cancel_reserve.assert_called_once_with(reader_1)

    logger.info('Testing the cancel reservation of a book test passed')


@pytest.mark.negative
@pytest.mark.cancel_reservation
def test_cancel_reservation_twice(library):
    logger.info('Testing the cancel reservation of a book twice by the same user')

    reader_1 = library['reader1']
    book_1 = library['book1']
    reader_1.reserve_book(book_1)
    reader_1.cancel_reserve(book_1)

    logger.debug('Attempting to cancel a book reservation twice '
                 'by the same reader should result in an error')
    with pytest.raises(PermissionError) as context:
        reader_1.cancel_reserve(book_1)
    assert str(context.value) == ("VASYA can not cancel a book, "
                                  "because he didn't reserve it")

    logger.info('Cancellation test passed twice')


@pytest.mark.negative
@pytest.mark.cancel_reservation
def test_cancel_reservation_without_reservation(library):
    logger.info('Testing cancellation of a book reservation by a user who did not reserve it')

    reader_1 = library['reader1']
    book_1 = library['book1']

    logger.debug('Attempting to cancel a book reservation '
                 'by a user who did not reserve it should result in an error')
    with pytest.raises(PermissionError) as context:
        reader_1.cancel_reserve(book_1)
    assert str(context.value) == ("VASYA can not cancel a book, "
                                  "because he didn't reserve it")

    logger.info('The reader was unable to return a book they had not reserved. Test passed.')


# Tests for obtaining books
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.receiving_book
def test_get_book(mocker, library):
    logger.info('Testing the successful receipt of one book by one user (use MOCK)')

    reader_1 = library['reader1']
    mock_book = mocker.Mock()

    reader_1.reserve_book(mock_book)
    reader_1.get_book(mock_book)
    mock_book.get_book.assert_called_once_with(reader_1)

    logger.info('Testing the successful receipt of one book test passed')


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.receiving_book
def test_get_book_multiple(mocker, library):
    logger.info('Testing the successful receipt of different books by different users (use MOCK)')

    reader_1 = library['reader1']
    reader_2 = library['reader2']
    mock_book_1 = mocker.Mock()
    mock_book_2 = mocker.Mock()

    reader_1.reserve_book(mock_book_1)
    reader_2.reserve_book(mock_book_2)
    reader_1.get_book(mock_book_1)
    reader_2.get_book(mock_book_2)
    mock_book_1.get_book.assert_called_once_with(reader_1)
    mock_book_2.get_book.assert_called_once_with(reader_2)

    logger.info('Testing the successful receipt of different book test passed')


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.receiving_book
def test_diff_get_book_one_reader(mocker, library):
    logger.info('Testing the successful receipt of multiple books by one user (use MOCK)')

    reader_1 = library['reader1']
    mock_book_1 = mocker.Mock()
    mock_book_2 = mocker.Mock()

    reader_1.reserve_book(mock_book_1)
    reader_1.reserve_book(mock_book_2)
    reader_1.get_book(mock_book_1)
    reader_1.get_book(mock_book_2)
    mock_book_1.get_book.assert_called_once_with(reader_1)
    mock_book_2.get_book.assert_called_once_with(reader_1)

    logger.info('Testing the successful receipt of of multiple books by one user test passed')


@pytest.mark.negative
@pytest.mark.receiving_book
def test_get_book_reserved_another_user(library):
    logger.info('Testing the function of retrieving '
                'a book that is reserved by another user')

    reader_1 = library['reader1']
    reader_2 = library['reader2']
    book_1 = library['book1']

    reader_1.reserve_book(book_1)

    logger.debug('Attempting to get a book that is reserved '
                 'by another user should result in an error')
    with pytest.raises(PermissionError) as context:
        reader_2.get_book(book_1)
    assert str(context.value) == "PETYA can not get a book 'The Hobbit'"

    logger.info('The test for retrieving a book '
                'reserved by another user has been passed')


@pytest.mark.negative
@pytest.mark.receiving_book
def test_get_book_received_another_user(library):
    logger.info('Testing the function of retrieving '
                'a book that is received by another user')

    reader_1 = library['reader1']
    reader_2 = library['reader2']
    book_1 = library['book1']
    reader_1.reserve_book(book_1)
    reader_1.get_book(book_1)

    logger.debug('Attempting to get a book that is received '
                 'by another user should result in an error')
    with pytest.raises(PermissionError) as context:
        reader_2.get_book(book_1)
    assert str(context.value) == "PETYA can not get a book 'The Hobbit'"

    logger.info('The test for retrieving a book that is '
                'received by another user has been passed')


# Book Return Tests
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.return_book
def test_return_book(mocker, library):
    logger.info('Testing the successfully return of a book (use MOCK)')

    reader_1 = library['reader1']
    mock_book = mocker.Mock()

    reader_1.reserve_book(mock_book)
    reader_1.get_book(mock_book)
    reader_1.return_book(mock_book)
    mock_book.return_book.assert_called_once_with(reader_1)

    logger.info('Return of the book test passed')


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.return_book
def test_return_books_multiple(mocker, library):
    logger.info('Testing the success of returning different books by different users (use MOCK)')

    reader_1 = library['reader1']
    reader_2 = library['reader2']
    mock_book_1 = mocker.Mock()
    mock_book_2 = mocker.Mock()

    reader_1.reserve_book(mock_book_1)
    reader_2.reserve_book(mock_book_2)
    reader_1.get_book(mock_book_1)
    reader_2.get_book(mock_book_2)
    reader_1.return_book(mock_book_1)
    reader_2.return_book(mock_book_2)

    mock_book_1.return_book.assert_called_once_with(reader_1)
    mock_book_2.return_book.assert_called_once_with(reader_2)

    logger.info('Return of different books by different users test passed')


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.return_book
def test_return_diff_books_one_reader(mocker, library):
    logger.info('Testing the successful return of different books by one user (use MOCK)')

    reader_1 = library['reader1']
    mock_book_1 = mocker.Mock()
    mock_book_2 = mocker.Mock()

    reader_1.reserve_book(mock_book_1)
    reader_1.reserve_book(mock_book_2)
    reader_1.get_book(mock_book_1)
    reader_1.get_book(mock_book_2)
    reader_1.return_book(mock_book_1)
    reader_1.return_book(mock_book_2)
    mock_book_1.return_book.assert_called_once_with(reader_1)
    mock_book_2.return_book.assert_called_once_with(reader_1)

    logger.info('Return of different books by one user test passed')


@pytest.mark.negative
@pytest.mark.return_book
def test_return_book_not_take1(library):
    logger.info('Testing the return of a book that the user did not take but reserved')

    reader_1 = library['reader1']
    book_1 = library['book1']
    reader_1.reserve_book(book_1)

    logger.debug('Attempts to return a book that the user '
                 'did not borrow but reserved should result in an error')
    with pytest.raises(PermissionError) as context:
        reader_1.return_book(book_1)
    assert str(context.value) == ("VASYA can not return a book 'The Hobbit', "
                                  "because he didn't take it")

    logger.info('Returning a book that was reserved but not taken, the test passed')


@pytest.mark.negative
@pytest.mark.return_book
def test_return_book_not_take2(library):
    logger.info('Testing the return of a book that the user did not take or reserve')

    reader_1 = library['reader1']
    book_1 = library['book1']

    logger.debug('Attempting to return a book that the user '
                 'did not take or reserved should result in an error')
    with pytest.raises(PermissionError) as context:
        reader_1.return_book(book_1)
    assert str(context.value) == ("VASYA can not return a book 'The Hobbit', "
                                  "because he didn't take it")

    logger.info('Returning a book, that the user did not receive test passed')
