import pytest
from deck import Deck


def test_number_of_cards_in_deck():
    assert len(Deck(1).cards) == 52
    assert len(Deck(2).cards) == 104


def test_shuffle_deck():
    deck = Deck(1)
    shuffled_deck = deck.cards.copy()
    deck.shuffle_cards()
    assert deck.cards != shuffled_deck


def test_left_cards_after_hit():
    number_of_decks = 1
    deck = Deck(number_of_decks)
    deck.shuffle_cards()
    base_number_of_cards = len(deck.cards)
    deck.hit()
    assert len(deck.cards) == 52 * number_of_decks - 1


def test_hit_card_not_in_deck():
    number_of_decks = 3
    deck = Deck(number_of_decks)
    deck.shuffle_cards()
    taken_card = deck.hit()
    cards_like_taken_in_deck = 0
    for card in deck.cards:
        print(f'card = {card}')
        print(f'taken_card = {taken_card}')
        if repr(card) == repr(taken_card):
            cards_like_taken_in_deck += 1
    print(f'cards like taken in deck: {cards_like_taken_in_deck}')
    assert cards_like_taken_in_deck == number_of_decks-1


def test_last_card_hit_taken():
    number_of_decks = 1
    deck = Deck(number_of_decks)
    deck.shuffle_cards()
    last_card_in_deck = deck.cards[-1]
    taken_card = deck.hit()
    assert last_card_in_deck == taken_card
