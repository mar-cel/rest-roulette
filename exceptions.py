#!/usr/bin/python3


class InvalidRollNumberException(Exception):
    """Raised when bet number is below the minimum or above the maximum"""
    pass


class InvalidBetException(Exception):
    """Raised when the bet is invalid"""
    pass


class InvalidWagerException(Exception):
    """Raised when the wager is not a valid number"""
    pass
