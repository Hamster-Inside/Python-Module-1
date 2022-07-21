from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck(1)
        self.deck.shuffle_cards()

    def play(self):
        user = Player()

        for _ in range (2):
            card = self.deck.hit()
            user.get_card(card)

        print(user.cards_in_hand)
        print(user.calculate_points())
