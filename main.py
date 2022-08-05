""" BlackJack game """

from game import Game
from exceptions import GameOverException, GameOverUserException, GameOverCroupierException

try:
    new_game = Game()
    new_game.play()
except GameOverUserException:
    print('Wygrywa krupier')
except GameOverCroupierException:
    print("CROUPIER CARDS: ", new_game.croupier.cards_in_hand)
    print("CROUPIER POINTS: ", new_game.croupier.calculate_points())
    print('Wygrywa gracz')