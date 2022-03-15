""" BlackJack game """

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

    def __init__(self):
        print(self.standard_deck)

    standard_deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    # Hearts, Diamonds, Spades, Clubs (Kier, Karo, Pik, Trefl)
    suits = ['H', 'D', 'S', 'C']


class Player:
    pass


class Croupier:
    pass


class Game:
    pass


deck = Deck()
