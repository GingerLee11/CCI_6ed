# python3
# deck_of_cards.py - Deck of cards implementation. 

from collections import deque
from random import randint


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class DeckIterator:
    """
    Iterator class for DeckOfCards
    """
    def __init__(self, deck):
        self._deck = deck
        self._index = 0

    def __next__(self):
        """
        Returns the next value from object iterables
        """
        if self._index < self._deck.deck_length:
            result = self._deck.deck[self._index]
            self._index += 1
            return result

        raise StopIteration


class Deck:

    def __init__(self):
        self.deck = None
        self.deck_shuffled = False
        self.deck_length = 52
        self.suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.values = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']

    def _create_deck(self):
        new_deck = {}
        for suit in self.suits:
            for value in self.values:
                if suit not in new_deck:
                    new_deck[suit] = [value]
                else:
                    new_deck[suit].append(value)
        
        return new_deck

    def shuffle(self):
        """
        Shuffle the cards into a random order.
        """
        # TODO: Implement ability to do a partial shuffle or shuffle a deck that is entered into the function.

        shuffled_deck = deque()
        new_deck = self._create_deck()
        suit_length = len(new_deck)
        suits = self.suits
        # suits = new_deck.keys()     
        # TODO: Add to check if all the suits in self.suits are in the deck
        # Pop any suit that is not in the inputted deck
        # Add the cards into the shuffled deck in a random order
        while len(shuffled_deck) <= self.deck_length:
            if suit_length == 0:
                break
            suit_indx = randint(0, suit_length - 1)
            suit = suits[suit_indx]
            value_length = len(new_deck[suit])

            # If the list of values is empty, 
            # that means that all the cards from that suit have already been shuffled into the deck.
            # So, the suit can be removed.
            if value_length == 0:
                new_deck.pop(suit)
                suits.pop(suit_indx)
                suit_length = len(new_deck)
            else:
                value_indx = randint(0, value_length - 1)
                value = new_deck[suit].pop(value_indx)
                new_card = Card(suit, value)
                shuffled_deck.append(new_card)
        
        self.deck = shuffled_deck
        self.deck_shuffled = True
        self.deck_length = len(self.deck)
        return self.deck

    def deal(self):
        if self.deck_shuffled == False:
            self.deck = self.shuffle()
            self.deck_length -= 1
            return self.deck.pop()
        else:
            self.deck_length -= 1
            return self.deck.pop()

    def __iter__(self):
        """
        Returns the iterator object
        """
        return DeckIterator(self)

'''
class DeckOfCards:
    deck_class = Deck()

    def __init__(self):
        pass

    def shuffle(self):
        return self._deck.shuffle_deck()

    def deal(self):
        deck = self._deck
        if deck.deck_shuffled == True:
            card = deck.deck.pop()
        else:
            shuffle_deck = deck.shuffle_deck()
            card = shuffle_deck.deck.pop()

        return card
'''


            

deck_of_cards = Deck()
deck_of_cards.shuffle()

print(deck_of_cards.deck_shuffled)

'''
for card in deck_of_cards:
    print(f"{card.value} of {card.suit}")
'''

while deck_of_cards.deck_length != 0:
    card = deck_of_cards.deal()
    print(f"{card.value} of {card.suit}")
