'''
Goal: develop a class Deck to represent a standard deck of 52 playing cards.
The class Deck should support methods:
Deck(): Initializes the deck to contain a standard deck of 52 playing cards.
shuffle(): Shuffles the deck.
dealcard(): Deals a card from the deck.
'''

import random

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit

class Deck():
    def __init__(self):
        self.cards = []
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suits = ['\u2660', '\u2661', '\u2662', '\u2663']
        for rank in range(1,14):
            for suit in range(4):
                self.cards.append(Card(self.ranks[rank-1], self.suits[suit-1]))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def dealcard(self):
        return self.cards.pop(0)
