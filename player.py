from card import Card


class Player:
    def __init__(self):
        pass
        self.cards_in_hand = []

    def get_card(self, card: Card):
        self.cards_in_hand.append(card)

    def calculate_points(self):
        points = 0
        aces_in_hand = len([card for card in self.cards_in_hand if card.value == 'Ace'])
        if aces_in_hand == 2 and len(self.cards_in_hand) == 2:
            return 12
        for card in self.cards_in_hand:
            if card.value in ['Jack', 'Queen', 'King']:
                points += 10
            elif card.value == 'Ace':
                if len(self.cards_in_hand) > 2:
                    points += 1
                else:
                    points += 11
            else:
                points += card.value
        return points

