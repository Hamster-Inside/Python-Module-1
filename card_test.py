from card import Card, InvalidColor, InvalidValue
import pytest


def test_color_creation():
    card = Card('hearts', 'Ace')
    assert card.color == '♡'


def test_value_creation():
    card = Card('hearts', 'Queen')
    assert card.value == 'Queen'


def test_wrong_color_creation():
    with pytest.raises(InvalidColor) as error_message:
        card = Card('xxx', 'Ace')
        assert error_message == "Color does not exist"


def test_wrong_value_creation():
    with pytest.raises(InvalidValue) as error_message:
        card = Card('hearts', 'wow')
        assert error_message == "Value does not exist"


def test_card_creation():
    assert repr(Card('hearts', 'Ace')) == 'Ace -> ♡'
