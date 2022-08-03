""" BlackJack game """

from game import Game
from exceptions import GameOverException, GameOverUserException, GameOverCroupierException

try:
    new_game = Game()
    new_game.play()
except GameOverUserException:
    print('Wygrywa krupier')
except GameOverCroupierException:
    print('Wygrywa gracz')