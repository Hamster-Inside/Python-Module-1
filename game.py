from deck import Deck
from player import Player
from exceptions import GameOverException, GameOverUserException, GameOverCroupierException


class Game:
    def __init__(self):
        self.deck = Deck(1)
        self.deck.shuffle_cards()

    @staticmethod
    def _print_menu():
        print("Co chcesz zrobić?")
        print("0 - pasuje")
        print("1 - dobieram kartę")

    def user_plays(self):
        user = Player()

        for _ in range(2):
            card = self.deck.hit()
            user.get_card(card)

        while True:
            print(user.cards_in_hand)
            print(user.calculate_points())
            self._print_menu()
            choice = input("Wybierz 0 lub 1\n")
            if choice == "0":
                print("PLAYER POINTS: ", user.calculate_points())
                break
            elif choice == "1":
                user.get_card(self.deck.hit())
            else:
                print("Must choose 0 or 1")
                continue
        return user.calculate_points()

    def _croupier_plays(self, user_points):
        croupier = Player()
        while user_points > croupier.calculate_points() and croupier.calculate_points() < 17:
            croupier.get_card(self.deck.hit())
        return croupier.calculate_points()



    def play(self):
        try:
            user_points = self.user_plays()
        except GameOverException as error:
            raise GameOverUserException from error
        self._croupier_plays(user_points)

        try:
            croupier_points = self._croupier_plays(user_points)
        except GameOverException as error:
            raise GameOverCroupierException from error
