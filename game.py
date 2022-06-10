from deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck(1)
        self.deck.shuffle_cards()

    def play(self):
        pass