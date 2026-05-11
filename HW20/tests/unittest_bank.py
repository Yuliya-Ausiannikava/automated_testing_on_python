"""
Test module for a banking application
"""

import unittest
import hw12_bank
from logging_config import get_logger

logger = get_logger("test_bank")


# Tests for the Bank class
class TestBank(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("Starting Bank App Tests")

    @classmethod
    def tearDownClass(cls):
        logger.info("Ending Bank App Tests")

    def setUp(self):
        logger.info("Setting up test environment")
        self.bank1 = hw12_bank.Bank()
        logger.info("Test environment set up successfully")

    def tearDown(self):
        logger.info("Tearing down test environment")
        del self.bank1
        logger.info("Test environment tear down successfully")

    def test_register_client(self):
        logger.info("Testing registration of multiple different clients")

        self.assertEqual(self.bank1.register_client(name='Yuliya', client_id='0001'), True)
        self.assertEqual(self.bank1.register_client(name='Nastya', client_id='0002'), True)

        logger.info("Multiple clients registration test passed")

    def test_register_duplicate_client(self):
        logger.info("Testing duplicate client")

        self.bank1.register_client(name='Yuliya', client_id='0001')

        logger.debug("Attempting to register clients with the same ID should result in an error.")

        with self.assertRaises(ValueError) as context:
            self.bank1.register_client(name='Katya', client_id='0001')
        self.assertEqual(str(context.exception), "Client with id 0001 already exists.")
        self.assertEqual(len(self.bank1.all_clients), 1)
        self.assertEqual(self.bank1.all_clients['0001']['name'], 'Yuliya')

        logger.info("Duplicate clients registration test passed")

    def test_open_deposit(self):
        logger.info("Testing the opening of a deposit account")

        self.bank1.register_client(name='Yuliya', client_id='0001')
        self.assertEqual(self.bank1.open_deposit_account(client_id='0001',
                                                         start_balance=1000, years=1), True)

        logger.info("Opening a deposit account test passed")

    def test_open_deposit_multiple_users(self):
        logger.info("Testing the opening of a deposit by several users")

        self.bank1.register_client(name='Yuliya', client_id='0001')
        self.bank1.register_client(name='Nastya', client_id='0002')
        self.assertEqual(self.bank1.open_deposit_account(client_id='0001',
                                                         start_balance=1000, years=1), True)
        self.assertEqual(self.bank1.open_deposit_account(client_id='0002',
                                                         start_balance=3000, years=2), True)

        logger.info("Opening deposit by several users test passed")

    def test_open_deposit_without_registration(self):
        logger.info("Testing opening deposit client without registration")
        logger.debug("Attempting to open a deposit by an "
                     "unregistered client should result in an error.")

        with self.assertRaises(ValueError) as context:
            self.bank1.open_deposit_account(client_id='0001', start_balance=1000, years=1)
        self.assertEqual(str(context.exception), "Client id 0001 has not been registered.")

        logger.info("Opening deposit client without registration test passed")

    def test_open_deposit_twice(self):
        logger.info("Testing opening deposit twice")

        self.bank1.register_client(name='Yuliya', client_id='0001')
        self.bank1.open_deposit_account(client_id='0001', start_balance=1000, years=1)

        logger.debug("A client attempting to reopen a deposit should result in an error.")

        with self.assertRaises(ValueError) as context:
            self.bank1.open_deposit_account(client_id='0001', start_balance=1000, years=1)
        self.assertEqual(str(context.exception), "Client Yuliya already has an open deposit.")

        logger.info("Opening deposit twice test passed")

    def test_open_deposit_checks_client_data(self):
        logger.info("Testing deposit data saving")

        self.bank1.register_client(name='Yuliya', client_id='0001')
        self.bank1.open_deposit_account(client_id='0001', start_balance=1000, years=1)
        client = self.bank1.all_clients['0001']
        self.assertEqual(client['deposit_is_open'], True)
        self.assertEqual(client['start_balance'], 1000)
        self.assertEqual(client['years'], 1)

        logger.info("Deposit data saving test passed")

    def test_calc_deposit_interest_rate(self):
        logger.info("Testing successful calculating deposit interest rate")

        self.bank1.register_client(name='Yuliya', client_id='0001')
        self.bank1.register_client(name='Nastya', client_id='0002')
        self.bank1.open_deposit_account(client_id='0001', start_balance=1000, years=1)
        self.bank1.open_deposit_account(client_id='0002', start_balance=5000, years=2)
        profit_0001 = self.bank1.calc_deposit_interest_rate('0001')
        profit_0002 = self.bank1.calc_deposit_interest_rate('0002')
        self.assertEqual(profit_0001, 1104.71)
        self.assertEqual(round(profit_0002, 2), 6101.95)

        logger.info("Calculating deposit interest rate test passed")

    def test_calc_deposit_interest_rate_without_registration(self):
        logger.info("Testing the calculation of the interest rate "
                    "on a deposit for a non-existent client")

        with self.assertRaises(ValueError) as context:
            self.bank1.calc_deposit_interest_rate('0001')
        self.assertEqual(str(context.exception), "Client id 0001 does not exist.")

        logger.info("Calculating deposit interest rate for a non-existent client test passed")

    def test_calc_deposit_interest_rate_not_open_deposit(self):
        logger.info("Testing calculating interest rate on a deposit without opening a deposit.")

        self.bank1.register_client(name='Yuliya', client_id='0001')
        with self.assertRaises(ValueError) as context:
            self.bank1.calc_deposit_interest_rate('0001')
        self.assertEqual(str(context.exception), "Client id 0001 has not opened a deposit.")

        logger.info("Calculating interest rate on a deposit without an open deposit test passed")

    def test_calc_deposit_interest_rate_after_close(self):
        logger.info("Testing calculating interest rate on a deposit after deposit is closed")

        self.bank1.register_client(name='Yuliya', client_id='0001')
        self.bank1.open_deposit_account(client_id='0001', start_balance=1000, years=1)
        self.bank1.close_deposit(client_id='0001')

        logger.debug("Attempting to close a deposit twice "
                     "by the same client should result in an error.")

        with self.assertRaises(ValueError) as context:
            self.bank1.calc_deposit_interest_rate('0001')
        self.assertEqual(str(context.exception), "Client id 0001 has not opened a deposit.")

        logger.info("Calculating interest rate on a deposit after deposit is closed test passed")

    def test_close_deposit(self):
        logger.info("Testing successful closing of a deposit by a bank client")

        self.bank1.register_client(name='Yuliya', client_id='0001')
        self.bank1.open_deposit_account(client_id='0001', start_balance=1000, years=1)
        result = self.bank1.close_deposit(client_id='0001')
        self.assertEqual(result, 1104.71)

        logger.info("Closed a deposit by a bank client test passed")

    def test_close_deposit_without_registration(self):
        logger.info("Testing closing a deposit for a non-existent client")
        logger.debug("Attempting to close a deposit by an unregistered "
                     "client should result in an error.")

        with self.assertRaises(ValueError) as context:
            self.bank1.close_deposit(client_id='0001')
        self.assertEqual(str(context.exception), "Client id 0001 does not exist.")

        logger.info("Closed a deposit by a non-existent client test passed")

    def test_close_deposit_not_open_deposit(self):
        logger.info("Testing closing a deposit without opening a deposit.")

        self.bank1.register_client(name='Nastya', client_id='0002')

        logger.debug("Attempting to close a deposit by a client "
                     "who did not open it should result in an error.")

        with self.assertRaises(ValueError) as context:
            self.bank1.close_deposit(client_id='0002')
        self.assertEqual(str(context.exception), "Client Nastya, id 0002, "
                                                 "has not opened a deposit to close.")

        logger.info("Closed a deposit without opening a deposit test passed")

    def test_close_deposit_multiple_times(self):
        logger.info("Testing closing already closed deposit")

        self.bank1.register_client(name='Nastya', client_id='0002')
        self.bank1.open_deposit_account(client_id='0002', start_balance=5000, years=2)
        result_1 = self.bank1.close_deposit(client_id='0002')
        self.assertEqual(round(result_1, 2), 6101.95)

        logger.debug("Attempting to close already closed deposit - should raise error")

        with self.assertRaises(ValueError) as context:
            self.bank1.close_deposit(client_id='0002')
        self.assertEqual(str(context.exception), "Client Nastya, id 0002, "
                                                 "has not opened a deposit to close.")
        logger.info("An attempt to close an already "
                    "closed deposit resulted in an error test passed.")


# Tests for the Person class
class TestPerson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("Starting Library App Tests")

    @classmethod
    def tearDownClass(cls):
        logger.info("Ending Library App Tests")

    def setUp(self):
        logger.info("Setting up test environment for Person tests")

    def tearDown(self):
        logger.info("Tearing down test environment for Person tests")

    def test_create_person(self):
        logger.info("Creating a person")

        person_1 = hw12_bank.Person(currency='USD', amount=10)
        person_2 = hw12_bank.Person(currency='EUR', amount=5)

        self.assertEqual(person_1.currency, 'USD')
        self.assertEqual(person_1.amount, 10)
        self.assertEqual(person_2.currency, 'EUR')
        self.assertEqual(person_2.amount, 5)

        logger.info("Person creation test passed")


# Tests for the CurrencyConverter class
class TestConverter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("Starting Library App Tests")

    @classmethod
    def tearDownClass(cls):
        logger.info("Ending Library App Tests")

    def setUp(self):
        logger.info("Setting up test environment for Converter tests")
        self.converter = hw12_bank.CurrencyConverter()
        logger.info('Setting up test environment for Converter tests')

    def tearDown(self):
        logger.info("Tearing down test environment for Converter tests")
        del self.converter
        logger.info("Tearing down test environment for Converter tests")

    def test_exchange_currency_byn(self):
        logger.info("Testing conversion to default target (BYN)")

        result_1 = self.converter.exchange_currency('USD', 10)
        result_2 = self.converter.exchange_currency('EUR', 5)
        self.assertEqual(result_1, (29.36, "BYN"))
        self.assertEqual(result_2, (16.95, "BYN"))

        logger.info("Default target test passed")

    def test_currency_exchange_specified_rate(self):
        logger.info("Testing conversion to specified rate")

        result_1 = self.converter.exchange_currency('USD', 10, to_currency='EUR')
        result_2 = self.converter.exchange_currency('EUR', 5, to_currency='USD')
        result_3 = self.converter.exchange_currency('EUR', 5, to_currency='RUB')
        self.assertEqual(result_1, (8.66, "EUR"))
        self.assertEqual(result_2, (5.77, "USD"))
        self.assertEqual(result_3, (4.56, "RUB"))

        logger.info("Specified target test passed")

    def test_conversion_unknown_currency(self):
        logger.info("Testing conversion of an unknown currency")
        logger.debug("Attempting to convert an unknown currency should result in an error")

        with self.assertRaises(ValueError) as context:
            self.converter.exchange_currency(currency='unknown', amount=10, to_currency='USD')
        self.assertEqual(str(context.exception), "Unknown currency: unknown")

        logger.info("Conversion of an unknown currency test passed")

    def test_conversion_unknown_to_currency(self):
        logger.info("Testing conversion to an unknown currency")
        logger.debug("Attempting to convert to an unknown currency should result in an error.")

        with self.assertRaises(ValueError) as context:
            self.converter.exchange_currency(currency='USD', amount=10, to_currency='unknown')
        self.assertEqual(str(context.exception), "Unknown target currency: unknown")

        logger.info("Conversion of to an unknown currency test passed")

    def test_conversion_currency_zero_amount(self):
        logger.info("Testing zero amount")

        result_1 = self.converter.exchange_currency(currency='USD', amount=0)
        result_2 = self.converter.exchange_currency(currency='EUR', amount=0, to_currency='USD')
        self.assertEqual(result_1, (0, "BYN"))
        self.assertEqual(result_2, (0, "USD"))

        logger.info("Zero-amount test passed")

    def test_conversion_currency_negative_amount(self):
        logger.info("Testing negative amount")
        logger.debug("Attempting to convert a negative amount should result in an error.")

        with self.assertRaises(ValueError) as context1:
            self.converter.exchange_currency(currency='USD', amount=-10)
        self.assertEqual(str(context1.exception), "Amount cannot be negative.")

        with self.assertRaises(ValueError) as context2:
            self.converter.exchange_currency(currency='EUR', amount=-10, to_currency='USD')
        self.assertEqual(str(context2.exception), "Amount cannot be negative.")

        logger.info("Conversion of negative amount test passed")


if __name__ == '__main__':
    unittest.main()
