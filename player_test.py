from player import Player
from card import Card


def test_count():
    #Given
    card_1 = Card('diamonds', 3)
    card_2 = Card('diamonds', 5)
    card_3 = Card('diamonds', 'Jack')
    card_4 = Card('diamonds', 'Ace')
    #When
    player_1 = Player()
    player_1.get_card(card_1)
    player_1.get_card(card_2)

    player_2 = Player()
    player_2.get_card(card_3)
    player_2.get_card(card_1)

    player_3 = Player()
    player_3.get_card(card_4)
    player_3.get_card(card_4)

    player_4 = Player()
    player_4.get_card(card_4)
    player_4.get_card(card_4)
    player_4.get_card(card_3)
    player_4.get_card(card_1)

    #Then
    assert player_1.calculate_points() == 8
    assert player_2.calculate_points() == 13
    assert player_3.calculate_points() == 12
    assert player_4.calculate_points() == 15
