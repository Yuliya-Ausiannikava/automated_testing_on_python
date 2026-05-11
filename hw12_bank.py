"""
A class has been created for calculating profit from a bank deposit with monthly capitalization.

Classes for currency conversion have been created.
"""

from logging_config import get_logger

logger = get_logger("logger_bank_app")


class Bank:

    def __init__(self):
        self.all_clients = {}

    def register_client(self, name, client_id):

        if client_id in self.all_clients:
            logger.error('Client with id %s already exists.', client_id)
            raise ValueError(f'Client with id {client_id} already exists.')

        self.all_clients[client_id] = {
            'name': name,
            'registered': True,
            'deposit_is_open': False,
            'start_balance': 0,
            'years': 0
        }
        logger.info('Client %s, id %s, registration was successful.', name, client_id)
        return True

    def open_deposit_account(self, client_id, start_balance, years):

        if client_id not in self.all_clients:
            logger.error('Client id %s has not been registered, '
                         'so he cannot open a deposit.', client_id)
            raise ValueError(f'Client id {client_id} has not been registered.')

        client = self.all_clients[client_id]
        if client['deposit_is_open']:
            logger.error('Client %s, id %s already has an open deposit.', client['name'], client_id)
            raise ValueError(f'Client {client["name"]} already has an open deposit.')

        client['deposit_is_open'] = True
        client['start_balance'] = start_balance
        client['years'] = years
        logger.info('Client %s, id %s, has opened a deposit.', client['name'], client_id)
        return True

    def calc_deposit_interest_rate(self, client_id):

        if client_id not in self.all_clients:
            logger.error('Client id %s does not exist.', client_id)
            raise ValueError(f'Client id {client_id} does not exist.')

        client = self.all_clients[client_id]
        if not client['deposit_is_open']:
            logger.error('Client %s, id %s has not opened a deposit '
                         'and cannot calculate profit.', client['name'], client_id)
            raise ValueError(f'Client id {client_id} has not opened a deposit.')

        percent_years = 0.10
        month = client['years'] * 12
        percent_month = percent_years / 12
        logger.info('Profit from investments of client %s, '
                    'id %s calculated.', client['name'], client_id)
        profit = round(client['start_balance'] * (1 + percent_month) ** month, 2)
        return profit

    def close_deposit(self, client_id):

        if client_id not in self.all_clients:
            logger.error('Client id %s does not exist.', client_id)
            raise ValueError(f'Client id {client_id} does not exist.')

        client = self.all_clients[client_id]
        if not client['deposit_is_open']:
            logger.error('Client %s, id %s, has not opened '
                         'a deposit to close.', client['name'], client_id)
            raise ValueError(f'Client {client["name"]}, id {client_id}, '
                             f'has not opened a deposit to close.')

        total = self.calc_deposit_interest_rate(client_id)
        if total is not False:
            client['deposit_is_open'] = False
            logger.info('Client %s, id %s has closed the deposit. '
                        'Total amount: %s', client['name'], client_id, total)
            return total
        return None


bank1 = Bank()
bank1.register_client('Yuliya', '0001')
bank1.open_deposit_account('0001', 1000, 1)
assert bank1.calc_deposit_interest_rate(client_id='0001') == 1104.71, \
    "The amount was calculated incorrectly"
bank1.close_deposit(client_id='0001')


# Classes for currency conversion have been created.
class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        logger.debug('Person with currency %s created.', currency)


class CurrencyConverter:

    def __init__(self):
        self.exchange_rates = {'BYN': 1.0, 'USD': 2.9364, 'EUR': 3.3894, 'RUB': 3.7179}

    def exchange_currency(self, currency, amount, to_currency='BYN'):
        if currency not in self.exchange_rates:
            logger.error('Currency %s does not exist.', currency)
            raise ValueError(f"Unknown currency: {currency}")

        if to_currency not in self.exchange_rates:
            logger.error('To_currency %s does not exist.', to_currency)
            raise ValueError(f"Unknown target currency: {to_currency}")

        if amount < 0:
            logger.error('Amount %s is negative.', amount)
            raise ValueError("Amount cannot be negative.")

        total_byn = amount * self.exchange_rates[currency]
        total_other = total_byn / self.exchange_rates[to_currency]
        logger.info('Conversion completed')
        return round(total_other, 2), to_currency


converter = CurrencyConverter()

vasya = Person('USD', 10)
petya = Person('EUR', 5)

# Если валюта не задана, то конвертация происходит в BYN:
assert converter.exchange_currency(vasya.currency, vasya.amount) == (29.36, "BYN"), \
    'Incorrect conversion value'
assert converter.exchange_currency(petya.currency, petya.amount) == (16.95, "BYN"), \
    'Incorrect conversion value'

# Конвертация из BYN в заданную валюту:
assert converter.exchange_currency(vasya.currency, vasya.amount, 'EUR') == (8.66, "EUR"), \
    'Incorrect conversion value'
assert converter.exchange_currency(petya.currency, petya.amount, 'USD') == (5.77, "USD"), \
    'Incorrect conversion value'
assert converter.exchange_currency(petya.currency, petya.amount, 'RUB') == (4.56, "RUB"), \
    'Incorrect conversion value'
