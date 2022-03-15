""" BlackJack game """
import random

"""
function itertools
valrus:=operator
Cards: 2,3,4,5,6,7,8,9,10,J,Q,K,A (kier karo trefl pik)
shuffle -> pop
Classes:
Game
Deck
Card
Player: Human Croupier

Exceptions:
GameOverException
GameOverPlayerException - player lost
GameOverCroupierException - player win

Additional:
Counting cards
graphic interface - tkinter
auto play game till you win with coins
split cards

"""


class Deck:

    def __init__(self, number_of_decks):
        self.standard_deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4 * number_of_decks
        random.shuffle(self.standard_deck)
        random.shuffle(self.standard_deck)
        random.shuffle(self.standard_deck)
        suits = ['H', 'D', 'S', 'C']
        # Hearts, Diamonds, Spades, Clubs (Kier, Karo, Pik, Trefl)




class Player:
    pass


class Croupier:
    pass


class Game:
    def __init__(self, num_of_decks):
        self.deck = Deck(num_of_decks)
    def draw_card(self, player):
        card = self.standard_deck.pop(-1)
        return card

deck = Deck(2)
print(deck.standard_deck)
print(deck.draw_card())
print(deck.standard_deck)
