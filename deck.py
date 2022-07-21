import random
from card import Card


class Deck:

    def __init__(self, number_of_decks):
        self.cards = []
        for i in range(number_of_decks):
            for color in Card.possible_colors:
                for value in Card.possible_values:
                    self.cards.append(Card(color=color, value=value))

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def hit(self):
        return self.cards.pop()


