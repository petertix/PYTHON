#!/usr/bin/python
"""This program prints out playing card hands from a shuffled deck.

It will print num_players hands of cards.
"""

from random import shuffle


class Hand(list):
    """Do something here."""

    pass


class Deck(object):
    """Here is the Deck class."""

    rank = '23456789TJQKA'
    suit = 'CSHD'

    def deal(self, n):
        """Deal the cards."""
        deck = [r+s for r in Deck.rank for s in Deck.suit]
        shuffle(deck)
        return [Hand(sorted(deck[i::n], key=Deck.cmpkey)) for i in xrange(n)]

    @staticmethod
    def cmpkey(card):
        """Do a compare."""
        return Deck.rank.index(card[0]), Deck.suit.index(card[1])


num_players = 4
print Deck().deal(num_players)
