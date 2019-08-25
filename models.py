#!/usr/bin/python3


from enum import Enum
import random

from exceptions import *
import roulette

NUMBERS_RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
NUMBERS_BLACK = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
NUMBERS_GREEN = [0]
BET_NUMBER_MIN = 0
BET_NUMBER_MID = 18
BET_NUMBER_MAX = 36
DEFAULT_PAYOUT_RATE = 1


class BetColor(Enum):
    red = 'red'
    black = 'black'
    green = 'green'


class BetParity(Enum):
    even = 'even'
    odd = 'odd'


class BetRange(Enum):
    low = 'low'
    high = 'high'


class BetType(Enum):
    parity = 'parity'
    color_rb = 'color_rb'
    color_green = 'color_green'
    number = 'number'
    range = 'range'


PAYOUT_RATES = {
    BetType.parity: 1,
    BetType.color_rb: 1,
    BetType.color_green: 35,
    BetType.number: 36,
    BetType.range: 1,
}


class Roll:
    def __init__(self):
        self.number = random.randint(BET_NUMBER_MIN, BET_NUMBER_MAX)
        self.color = roulette.get_number_color(self.number)
        if self.color is False:
            raise InvalidRollNumberException()
        self.parity = roulette.get_number_parity(self.number)
        self.range = roulette.get_number_range(self.number)

    def __str__(self):
        return 'Roll: {number: %s, color: %s, parity: %s, range: %s}' % \
            (self.number, self.color, self.parity, self.range)


class Bet:
    def __init__(self, bet, wager):
        self.bet = bet
        self.type = roulette.validate_bet(self.bet)
        if self.type is False:
            raise InvalidBetException()
        try:
            self.wager = float(wager)
        except ValueError as e:
            raise InvalidWagerException()

    def __str__(self):
        return 'Bet: {bet: %s, type: %s}' % (self.bet, self.type)


class Payout:
    def __init__(self, did_win, wager, bet_type):
        self.did_win = did_win
        self.wager = wager
        self.type = bet_type
        self.payout_rate = PAYOUT_RATES.get(bet_type, DEFAULT_PAYOUT_RATE) if did_win else 0
        self.payout_amount = wager + wager * self.payout_rate if did_win else 0

    def __str__(self):
        return 'Payout: {did_win: %s, wager: %s, type: %s, payout_rate: %s, payout_amount: %s' % \
            (self.did_win, self.wager, self.type, self.payout_rate, self.payout_amount)

