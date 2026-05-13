import sys
from pathlib import Path
import pytest
import hw12_bank

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from logging_config import get_logger
logger = get_logger("pytest bank")

@pytest.fixture(scope="function", autouse=True)
def bank():
    logger.info("Setting up test environment")
    new_bank = hw12_bank.Bank()
    yield new_bank
    logger.info("Tearing down test environment")

@pytest.fixture(scope='session', autouse=True)
def session_bank():
    logger.info("Starting Bank App Tests")
    yield
    logger.info("Ending Bank App Tests")

# Testing the Creating an instance of the Bank class
def test_bank_creation(bank):
    logger.info("Testing Bank Creation")

    assert bank is not None

    logger.info("Bank Creation test passed")

# Testing the registration function
def test_register_client(bank):
    logger.info("Testing successful Bank Client Registration")

    assert bank.register_client(name='Yuliya', client_id='0001') is True
    assert len(bank.all_clients) == 1

    logger.info("Bank Client Registration test passed")

def test_register_duplicate_client(bank):
    logger.info("Testing duplicate client registration")

    bank.register_client(name='Yuliya', client_id='0001')

    logger.debug("Attempting to register clients with the same ID should result in an error.")
    with pytest.raises(ValueError) as context:
        bank.register_client(name='Masha', client_id='0001')

    assert 'Client with id 0001 already exists.' in str(context.value)
    assert len(bank.all_clients) == 1

    logger.info("Duplicate client registration test passed")

def test_register_client_with_different_id(bank):
    logger.info("Testing registration of multiple clients")

    bank.register_client(name='Yuliya', client_id='0001')
    bank.register_client(name='Masha', client_id='0002')

    assert len(bank.all_clients) == 2
    assert bank.all_clients['0001']['name'] == 'Yuliya'
    assert bank.all_clients['0002']['name'] == 'Masha'

    logger.info("Multiple clients registration test passed")

def test_open_deposit(bank):
    logger.info("Testing successful opening deposit")

    bank.register_client(name='Yuliya', client_id='0001')

    assert bank.open_deposit_account(client_id='0001', start_balance=1000, years=1) is True
    assert bank.all_clients['0001']['deposit_is_open'] is True

    logger.info("Opening deposit test passed")

def test_open_deposit_multiple_users(bank):
    logger.info("Testing successful opening deposit with multiple users")

    bank.register_client(name='Yuliya', client_id='0001')
    bank.register_client(name='Masha', client_id='0002')

    assert bank.open_deposit_account(client_id='0001', start_balance=1000, years=1) is True
    assert bank.all_clients['0001']['deposit_is_open'] is True
    assert bank.open_deposit_account(client_id='0002', start_balance=3000, years=2) is True
    assert bank.all_clients['0002']['deposit_is_open'] is True

    logger.info("Opening deposit by several users test passed")

def test_open_deposit_already_open(bank):
    logger.info("Testing the opening of a deposit that has already been opened")

    bank.register_client(name='Yuliya', client_id='0001')
    bank.open_deposit_account(client_id='0001', start_balance=1000, years=1)

    logger.debug("A client attempting to reopen a deposit should result in an error.")
    with pytest.raises(ValueError) as context:
        bank.open_deposit_account(client_id='0001', start_balance=1000, years=1)
    assert 'Client Yuliya already has an open deposit.' in str(context.value)

    logger.info("Opening the same deposit twice test passed")














