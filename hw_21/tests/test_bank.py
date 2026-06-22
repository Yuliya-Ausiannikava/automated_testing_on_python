import pytest
from hw_12 import hw12_bank
from logging_config import get_logger

logger = get_logger(__name__)


@pytest.fixture(scope="function")
def bank_fixt():
    logger.info("Setting up test environment")
    new_bank = hw12_bank.Bank()
    yield new_bank
    logger.info("Tearing down test environment")


@pytest.fixture(scope="function")
def conv():
    logger.info("Setting up test environment for Converter tests")
    converter = hw12_bank.CurrencyConverter()
    yield converter
    logger.info("Tearing down test environment for Converter tests")


@pytest.fixture(scope='session', autouse=True)
def session_bank():
    logger.info("Starting Bank App Tests")
    yield
    logger.info("Ending Bank App Tests")


# class Bank
# Testing the Creating an instance of the Bank class
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.bank
def test_bank_creation(bank_fixt):
    logger.info("Testing Bank Creation")

    assert bank_fixt is not None

    logger.info("Bank Creation test passed")


# Tests to verify client registration functionality
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.bank
def test_register_client(bank_fixt):
    logger.info("Testing successful Bank Client Registration")

    assert bank_fixt.register_client(name='Yuliya', client_id='0001') is True
    assert len(bank_fixt.all_clients) == 1

    logger.info("Bank Client Registration test passed")


@pytest.mark.negative
@pytest.mark.registration
@pytest.mark.bank
def test_register_duplicate_client(bank_fixt):
    logger.info("Testing duplicate client registration")

    bank_fixt.register_client(name='Yuliya', client_id='0001')

    logger.debug("Attempting to register clients with the same ID should result in an error.")
    with pytest.raises(ValueError) as context:
        bank_fixt.register_client(name='Masha', client_id='0001')

    assert 'Client with id 0001 already exists.' in str(context.value)
    assert len(bank_fixt.all_clients) == 1

    logger.info("Duplicate client registration test passed")


# Tests to verify the functionality of opening a deposit
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.bank
def test_register_client_with_different_id(bank_fixt):
    logger.info("Testing registration of multiple clients")

    bank_fixt.register_client(name='Yuliya', client_id='0001')
    bank_fixt.register_client(name='Masha', client_id='0002')

    assert len(bank_fixt.all_clients) == 2
    assert bank_fixt.all_clients['0001']['name'] == 'Yuliya'
    assert bank_fixt.all_clients['0002']['name'] == 'Masha'

    logger.info("Multiple clients registration test passed")


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.deposit
@pytest.mark.bank
def test_open_deposit(bank_fixt):
    logger.info("Testing successful opening deposit")

    bank_fixt.register_client(name='Yuliya', client_id='0001')
    assert bank_fixt.open_deposit_account(client_id='0001', start_balance=1000, years=1) is True

    client = bank_fixt.all_clients['0001']
    assert client['deposit_is_open'] is True
    assert client['start_balance'] == 1000
    assert client['years'] == 1

    logger.info("Opening deposit test passed")


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.deposit
@pytest.mark.bank
def test_open_deposit_multiple_users(bank_fixt):
    logger.info("Testing successful opening deposit with multiple users")

    bank_fixt.register_client(name='Yuliya', client_id='0001')
    bank_fixt.register_client(name='Masha', client_id='0002')

    assert bank_fixt.open_deposit_account(client_id='0001', start_balance=1000, years=1) is True
    assert bank_fixt.all_clients['0001']['deposit_is_open'] is True
    assert bank_fixt.open_deposit_account(client_id='0002', start_balance=3000, years=2) is True
    assert bank_fixt.all_clients['0002']['deposit_is_open'] is True

    logger.info("Opening deposit by several users test passed")


@pytest.mark.negative
@pytest.mark.deposit
@pytest.mark.bank
def test_open_deposit_already_open(bank_fixt):
    logger.info("Testing the opening of a deposit that has already been opened")

    bank_fixt.register_client(name='Yuliya', client_id='0001')
    bank_fixt.open_deposit_account(client_id='0001', start_balance=1000, years=1)

    logger.debug("A client attempting to reopen a deposit should result in an error.")
    with pytest.raises(ValueError) as context:
        bank_fixt.open_deposit_account(client_id='0001', start_balance=1000, years=1)
    assert 'Client Yuliya already has an open deposit.' in str(context.value)

    logger.info("Opening the same deposit twice test passed")


@pytest.mark.negative
@pytest.mark.deposit
@pytest.mark.bank
def test_open_deposit_without_registration(bank_fixt):
    logger.info("Testing opening deposit client without registration")
    logger.debug("Attempting to open a deposit by an "
                 "unregistered client should result in an error.")

    with pytest.raises(ValueError) as context:
        bank_fixt.open_deposit_account(client_id='0001', start_balance=1000, years=1)
    assert 'Client id 0001 has not been registered.' in str(context.value)

    logger.info("Opening deposit client without registration test passed")


# Tests on calculating interest rates on deposits
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.interest
@pytest.mark.bank
def test_calc_deposit_interest_rate(bank_fixt):
    logger.info("Testing successful calculating deposit interest rate")

    bank_fixt.register_client(name='Yuliya', client_id='0001')
    bank_fixt.register_client(name='Nastya', client_id='0002')
    bank_fixt.open_deposit_account(client_id='0001', start_balance=1000, years=1)
    bank_fixt.open_deposit_account(client_id='0002', start_balance=5000, years=2)
    profit_0001 = bank_fixt.calc_deposit_interest_rate('0001')
    profit_0002 = bank_fixt.calc_deposit_interest_rate('0002')

    assert round(profit_0001, 2) == 1104.71
    assert round(profit_0002, 2) == 6101.95

    logger.info("Calculating deposit interest rate test passed")


@pytest.mark.negative
@pytest.mark.interest
@pytest.mark.bank
def test_calc_deposit_interest_rate_without_registration(bank_fixt):
    logger.info("Testing the calculation of the interest rate "
                "on a deposit for a non-existent client")

    logger.debug("Attempting to calculate the interest rate on a deposit "
                 "for a non-existent client should result in an error.")
    with pytest.raises(ValueError) as context:
        bank_fixt.calc_deposit_interest_rate('0001')
    assert 'Client id 0001 does not exist.' in str(context.value)

    logger.info("Calculating deposit interest rate for a non-existent client test passed")


@pytest.mark.negative
@pytest.mark.interest
@pytest.mark.bank
def test_calc_deposit_interest_rate_not_open_deposit(bank_fixt):
    logger.info("Testing calculating interest rate on a deposit without opening a deposit.")

    bank_fixt.register_client(name='Yuliya', client_id='0001')

    logger.debug("Attempting to calculate the interest rate on a deposit "
                 "without opening a deposit should result in an error.")
    with pytest.raises(ValueError) as context:
        bank_fixt.calc_deposit_interest_rate('0001')
    assert 'Client id 0001 has not opened a deposit.' in str(context.value)

    logger.info("Calculating interest rate on a deposit without opening a deposit test passed")


@pytest.mark.negative
@pytest.mark.interest
@pytest.mark.bank
def test_calc_deposit_interest_rate_after_close(bank_fixt):
    logger.info("Testing calculating interest rate on a deposit after deposit is closed")

    bank_fixt.register_client(name='Yuliya', client_id='0001')
    bank_fixt.open_deposit_account(client_id='0001', start_balance=1000, years=1)
    bank_fixt.close_deposit(client_id='0001')

    logger.debug("Attempting to close a deposit twice "
                 "by the same client should result in an error.")
    with pytest.raises(ValueError) as context:
        bank_fixt.calc_deposit_interest_rate('0001')
    assert 'Client id 0001 has not opened a deposit.' in str(context.value)

    logger.info("Calculating interest rate on a deposit after deposit is closed test passed")


# Tests for closing a deposit
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.close
@pytest.mark.bank
def test_close_deposit(bank_fixt):
    logger.info("Testing successful closing of a deposit by a bank client")

    bank_fixt.register_client(name='Yuliya', client_id='0001')
    bank_fixt.open_deposit_account(client_id='0001', start_balance=1000, years=1)
    result = bank_fixt.close_deposit(client_id='0001')
    assert round(result, 2) == 1104.71

    logger.info("Closed a deposit by a bank client test passed")


@pytest.mark.negative
@pytest.mark.close
@pytest.mark.bank
def test_close_deposit_without_registration(bank_fixt):
    logger.info("Testing closing a deposit for a non-existent client")

    logger.debug("Attempting to close a deposit by an unregistered "
                 "client should result in an error.")
    with pytest.raises(ValueError) as context:
        bank_fixt.close_deposit(client_id='0001')
    assert 'Client id 0001 does not exist.' in str(context.value)

    logger.info("Closed a deposit by a non-existent client test passed")


@pytest.mark.negative
@pytest.mark.close
@pytest.mark.bank
def test_close_deposit_not_open_deposit(bank_fixt):
    logger.info("Testing closing a deposit without opening a deposit.")

    bank_fixt.register_client(name='Nastya', client_id='0002')

    logger.debug("Attempting to close a deposit by a client "
                 "who did not open it should result in an error.")
    with pytest.raises(ValueError) as context:
        bank_fixt.close_deposit(client_id='0002')
    assert 'Client Nastya, id 0002, has not opened a deposit to close.' in str(context.value)

    logger.info("Closed a deposit without opening a deposit test passed")


@pytest.mark.negative
@pytest.mark.close
@pytest.mark.bank
def test_close_deposit_multiple_times(bank_fixt):
    logger.info("Testing closing already closed deposit")

    bank_fixt.register_client(name='Nastya', client_id='0002')
    bank_fixt.open_deposit_account(client_id='0002', start_balance=5000, years=2)
    result = bank_fixt.close_deposit(client_id='0002')
    assert round(result, 2) == 6101.95

    logger.debug("Attempting to close already closed deposit - should raise error")
    with pytest.raises(ValueError) as context:
        bank_fixt.close_deposit(client_id='0002')
    assert 'Client Nastya, id 0002, has not opened a deposit to close.' in str(context.value)

    logger.info("An attempt to close an already "
                "closed deposit resulted in an error test passed.")


# Tests for the Person class
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.person
def test_create_person():
    logger.info("Successful user creation")

    person = hw12_bank.Person(currency='USD', amount=10)
    assert person.currency == 'USD'
    assert person.amount == 10

    logger.info("User creation test passed")


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.person
def test_create_multiple_persons():
    logger.info("Successfully create multiple users")

    person1 = hw12_bank.Person(currency='USD', amount=10)
    person2 = hw12_bank.Person(currency='EUR', amount=5)
    assert person1.currency == 'USD'
    assert person1.amount == 10
    assert person2.currency == 'EUR'
    assert person2.amount == 5

    logger.info("multiple users creation test passed")


# Tests for the CurrencyConverter class
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.converter
def test_exchange_currency_byn(conv):
    logger.info("Testing conversion to default target (BYN)")

    result1 = conv.exchange_currency(currency='USD', amount=10)
    result2 = conv.exchange_currency(currency='EUR', amount=5)

    assert result1 == (29.36, "BYN")
    assert result2 == (16.95, "BYN")

    logger.info("Default target test passed")


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.converter
def test_currency_exchange_specified_rate(conv):
    logger.info("Testing conversion to specified rate")

    result_1 = conv.exchange_currency(currency='USD', amount=10, to_currency='EUR')
    result_2 = conv.exchange_currency(currency='EUR', amount=5, to_currency='USD')
    result_3 = conv.exchange_currency(currency='EUR', amount=5, to_currency='RUB')

    assert result_1 == (8.66, "EUR")
    assert result_2 == (5.77, "USD")
    assert result_3 == (4.56, "RUB")

    logger.info("Specified target test passed")


@pytest.mark.negative
@pytest.mark.converter
def test_conversion_unknown_currency(conv):
    logger.info("Testing conversion of an unknown currency")

    logger.debug("Attempting to convert an unknown currency should result in an error")
    with pytest.raises(ValueError) as context:
        conv.exchange_currency(currency='unknown', amount=10, to_currency='USD')
    assert str(context.value) == "Unknown currency: unknown"

    logger.info("Conversion of an unknown currency test passed")


@pytest.mark.negative
@pytest.mark.converter
def test_conversion_unknown_to_currency(conv):
    logger.info("Testing conversion to an unknown currency")

    logger.debug("Attempting to convert to an unknown currency should result in an error.")
    with pytest.raises(ValueError) as context:
        conv.exchange_currency(currency='USD', amount=10, to_currency='unknown')
    assert str(context.value) == "Unknown target currency: unknown"

    logger.info("Conversion of to an unknown currency test passed")


@pytest.mark.converter
def test_conversion_currency_zero_amount(conv):
    logger.info("Testing zero amount")

    result_1 = conv.exchange_currency(currency='USD', amount=0)
    result_2 = conv.exchange_currency(currency='EUR', amount=0, to_currency='USD')
    assert result_1 == (0, "BYN")
    assert result_2 == (0, "USD")

    logger.info("Zero-amount test passed")


@pytest.mark.negative
@pytest.mark.converter
def test_conversion_currency_negative_amount(conv):
    logger.info("Testing negative amount")

    logger.debug("Attempting to convert a negative amount should result in an error.")
    with pytest.raises(ValueError) as context:
        conv.exchange_currency(currency='USD', amount=-10)
    assert str(context.value) == "Amount cannot be negative."

    with pytest.raises(ValueError) as context:
        conv.exchange_currency(currency='EUR', amount=-10, to_currency='USD')
    assert str(context.value) == "Amount cannot be negative."

    logger.info("Conversion of negative amount test passed")
