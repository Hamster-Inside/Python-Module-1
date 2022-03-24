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


class Person:
    def __init__(self, name):
        self.name = name


class Player(Person):
    def __init__(self, player_name):
        super().__init__(player_name)

    def __repr__(self):
        return self.name


class Croupier(Person):
    def __init__(self):
        super().__init__('Stefan')

    def __repr__(self):
        return self.name


class Game:
    def __init__(self, num_of_decks):
        self.deck = Deck(num_of_decks)
        self.croupier = Croupier()
        self.players = [self.croupier]

    def draw_card(self, player):
        card = self.standard_deck.pop(-1)
        return card

    def add_player(self, player_nickname):
        player = Player(player_nickname)
        self.players.append(player)

    def get_player_list(self):
        return self.players


game = Game(3)
game.add_player('Boguś')
game.add_player('Homar')
print(game.get_player_list())
