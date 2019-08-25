#!/usr/bin/python3


import models


# Validates bet and returns the type
def validate_bet(bet):
    bet = bet.lower()
    if bet.isdigit():
        bet = int(bet)
        if bet < models.BET_NUMBER_MIN or bet > models.BET_NUMBER_MAX:
            return False
        return models.BetType.number
    elif bet in set(item.value for item in models.BetColor):
        return models.BetType.color_green if bet == models.BetColor.green else models.BetType.color_rb
    elif bet in set(item.value for item in models.BetParity):
        return models.BetType.parity
    elif bet in set(item.value for item in models.BetRange):
        return models.BetType.range
    return False


def get_number_parity(num: int):
    return models.BetParity.even if num % 2 == 0 else models.BetParity.odd


def get_number_color(num: int):
    if num in models.NUMBERS_RED:
        return models.BetColor.red
    elif num in models.NUMBERS_BLACK:
        return models.BetColor.black
    elif num in models.NUMBERS_GREEN:
        return models.BetColor.green
    return False


def get_number_range(num: int):
    return models.BetRange.low if num <= models.BET_NUMBER_MID else models.BetRange.high


# Returns True for win, False for loss, None for invalid bet type
def check_bet_win(bet: models.Bet, roll: models.Roll):
    if bet.type == models.BetType.parity:
        return roll.parity.value == bet.bet
    elif bet.type in {models.BetType.color_rb, models.BetType.color_green}:
        return roll.color.value == bet.bet
    elif bet.type == models.BetType.number:
        return roll.number == int(bet.bet)
    elif bet.type == models.BetType.range:
        return roll.range.value == bet.bet


def play(bet, wager):
    roll = models.Roll()
    bet = models.Bet(bet, wager)
    did_win = check_bet_win(bet, roll)
    payout = models.Payout(did_win, bet.wager, bet.type)
    return {
        'success': True,
        'roll': {
            'number': roll.number,
            'color': roll.color.value,
            'parity': roll.parity.value
        },
        'bet': {
            'bet': bet.bet,
            'wager': '%.2f' % bet.wager,
            'win': did_win,
            'payout_rate': payout.payout_rate,
            'payout': '%.2f' % payout.payout_amount
        }
    }
