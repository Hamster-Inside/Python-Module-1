""" BlackJack game """

from enum import Enum
import card, deck


class PlayerStatus(Enum):
    PLAYING = 0
    WIN = 1
    LOST = 2
    DRAW = 3


class GameStatus(Enum):
    IN_PROGRESS = 0
    FINISHED = 1


class Person:
    def __init__(self, name):
        self.name = name


class Player(Person):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_cards = []
        self.count = 0
        self.status = PlayerStatus.PLAYING

    def __repr__(self):
        return self.name


class Game:

    def __init__(self, num_of_decks):
        self.deck = Deck(num_of_decks)
        self.player_list = []
        self.game_status = GameStatus.IN_PROGRESS
        self.players_in_game = 0

    def draw_card(self, player_to_draw_to):
        card = self.deck.standard_deck.pop(-1)
        self.deck.deck_cards[player_to_draw_to].append(card)
        self.count_player_cards_value(player_to_draw_to)

    def add_player(self, player_nickname):
        new_player = Player(player_nickname)
        self.players_in_game += 1
        self.player_list.append(new_player)
        self.deck.deck_cards[new_player] = []

    def start_deck_game(self):
        for i in range(2):
            for player_in_game in self.player_list:
                game.draw_card(player_in_game)

    def view_deck(self):
        self.deck.view_table_cards()

    def split_cards(self, player_to_have_split_cards):
        pass

    def count_player_cards_value(self, player_to_count_values_from):
        player_to_count_values_from.count = 0
        for card_val in self.deck.deck_cards[player_to_count_values_from]:
            player_to_count_values_from.count += self.deck.cards.card_value(card_val)
        if player_to_count_values_from.count > 21:
            player_to_count_values_from.status = PlayerStatus.LOST
            self.players_in_game -= 1
            raise GameLostException(f'Player {player_to_count_values_from} LOST, value over 21')

    def croupier_play(self):
        croupier = self.player_list[0]
        while croupier.count < 17:
            self.draw_card(croupier)
            print()
            self.view_deck()

    def win_lost_resolver(self):
        croupier = self.player_list[0]
        for players_comp in self.player_list:
            if players_comp != croupier and players_comp.status != PlayerStatus.LOST:
                if croupier.status != PlayerStatus.LOST:
                    if players_comp.count > croupier.count:
                        players_comp.status = PlayerStatus.WIN
                    elif players_comp.count == croupier.count:
                        players_comp.status = PlayerStatus.DRAW
                    else:
                        players_comp.status = PlayerStatus.LOST
                else:
                    players_comp.status = PlayerStatus.WIN


decks = int(input("Enter number of decks in game\n"))
game = Game(decks)
game.add_player('Croupier')
game.add_player('Boguś')
game.add_player('Homar')
game.add_player('Stefan')
game.add_player('Hamtaro')
game.start_deck_game()  # give 2 cards to every player, where croupier has one hidden

for player in game.player_list:
    if player.name == 'Croupier':
        continue
    while True:
        game.view_deck()
        operation = input(f"{player} - What do you want to do? (draw, pass, split)\n")
        match operation.lower():
            case 'draw':
                try:
                    game.draw_card(player)
                except GameLostException as e:
                    print(e)
                    break
            case 'pass':
                break
            case 'split':
                game.split_cards(player)
            case _:
                print('Need to Draw, Pass or Split')
game.game_status = GameStatus.FINISHED
game.view_deck()
if game.players_in_game > 1:
    try:
        game.croupier_play()
    except GameLostException as e:
        print(e)
    game.win_lost_resolver()
game.view_deck()
