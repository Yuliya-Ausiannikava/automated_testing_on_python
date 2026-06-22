"""
A program that contains a list of cards, can shuffle them,
and allows the user to select a card from the deck by its number.
"""

import logging
import random
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("my_logger")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger.setLevel(logging.DEBUG)

file_handler = TimedRotatingFileHandler(
    filename="user_actions.log",
    when='midnight',
    interval=1,
    backupCount=7,
    encoding='utf-8'
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class Card:

    number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    mast_list = ['♠', '♥', '♦', '♣']
    jokers_list = ['Red Joker', 'Black Joker']

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __str__(self):
        return f"{self.number} {self.mast}"


class CardsDeck:
    def __init__(self):
        self.cards = []
        for mast in Card.mast_list:
            for number in Card.number_list:
                self.cards.append(Card(number, mast))
                logger.debug('Added 1 card: %s and %s', number, mast)
        for joker in Card.jokers_list:
            self.cards.append(Card(joker, ''))
            logger.debug('Added joker')
        logger.debug('A deck of 54 cards is created')

    def shuffle(self):
        random.shuffle(self.cards)
        logger.info('A deck of 54 cards is shuffled')

    def get_cards(self, index):
        if 0 <= index < len(self.cards):
            logger.debug('Getting a card from the deck')
            return self.cards[index]
        else:
            logger.error('Getting a card from the deck')
            raise IndexError('A non-existent index was entered. '
                             'You must enter an integer between 0 and 53')


deck = CardsDeck()
deck.shuffle()

card_number = int(input('Choose a card from a deck of 54 cards: '))
card = deck.get_cards(card_number)
print(f'You card is: {card}')

card_number = int(input('Choose a card from a deck of 54 cards: '))
card = deck.get_cards(card_number)
print(f'You card is: {card}')
