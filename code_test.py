from enum import Enum


class PlayerStatus(Enum):
    WIN = 1
    LOST = 2
    DRAW = 3


class Player:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

status = PlayerStatus.WIN
new_player = Player("JOHNNNNN")
list_of_cards = {}
list_of_cards[new_player] = ['Ace', '2', '3']
list_of_cards['Steve'] = ['K', '2', '3']
list_of_cards['Steve'].append('J')
print(list_of_cards)
