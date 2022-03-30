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
        self.croupier = Croupier()
        self.standard_deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4 * number_of_decks
        random.shuffle(self.standard_deck)
        random.shuffle(self.standard_deck)
        random.shuffle(self.standard_deck)
        self.players = []
        suits = ['H', 'D', 'S', 'C']
        # Hearts, Diamonds, Spades, Clubs (Kier, Karo, Pik, Trefl)

    def get_player_list(self):
        return self.players

    def add_player_to_deck(self, player_name):
        self.players.append(player_name)


class Person:
    def __init__(self, name):
        self.name = name


class Player(Person):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_cards = []

    def __repr__(self):
        return self.name

    def add_card_to_player(self, card_to_be_given):
        self.player_cards.append(card_to_be_given)


class Croupier(Person):
    def __init__(self):
        super().__init__('Stefan')
        self.croupier_cards = []

    def __repr__(self):
        return self.name

    def add_card_to_croupier(self, card_to_be_given):
        self.croupier_cards.append(card_to_be_given)


class Game:

    def __init__(self, num_of_decks):
        self.deck = Deck(num_of_decks)
        self.player_list = self.deck.get_player_list()

    def draw_card(self, player_to_draw_to):
        card = self.deck.standard_deck.pop(-1)
        player_to_draw_to.add_card_to_player(card)

    def add_player(self, player_nickname):
        self.deck.add_player_to_deck(player_nickname)

    def start_deck_game(self):
        for i in range(2):
            for player_in_game in self.player_list:
                game.draw_card(player_in_game)

    def view_deck(self):
        return self.deck.standard_deck

    def draw_hidden_card(self, who_draws_card):
        card = self.deck.standard_deck.pop(-1)
        return card


game = Game(num_of_decks=3)
game.add_player('Boguś')
game.add_player('Homar')
game.start_deck_game()
while True:
    game.view_deck()
    for player in game.player_list:
        while True:
            operation = input(f"{player} - What do you want to do? (draw, pass, split)\n")
            match operation.lower():
                case 'draw':
                    game.draw_card(player)
                    break
                case 'pass':
                    print('PASS')
                    break
                case 'split':
                    print('SPLIT')
                    break
                case _:
                    print('Need to Draw, Pass or Split')
