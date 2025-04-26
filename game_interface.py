import random
from result_tracker import result_tracker


class game_interface():

    def __init__(self):
        self.ROCK = 1
        self.PAPER = 2
        self.SCISSORS = 3

        self.TIE = "Tie"
        self.COMPUTER_WIN = "Computer win!"
        self.PLAYER_WIN = "Player win!"

    def present_player_choices(self):
        print("Choices are:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

    def choose_move(self):
        valid_moves = [0, 1, 2, 3]
        choice = -1
        while (choice not in valid_moves):
            choice = int(input("Enter move:"))
            if (choice not in valid_moves):
                print("Please enter 1, 2, or 3! 0 to exit")

        return choice

    def computer_choice(self):
        return random.randint(1, 3)

    def determine_result(self, player_move, computer_move):

        if (player_move == computer_move):
            return self.TIE

        if (player_move == self.ROCK):
            if (computer_move == self.SCISSORS):
                return self.PLAYER_WIN
            else:
                return self.COMPUTER_WIN

        if (player_move == self.PAPER):
            if (computer_move == self.ROCK):
                return self.PLAYER_WIN
            else:
                return self.COMPUTER_WIN

        if (player_move == self.SCISSORS):
            if (computer_move == self.PAPER):
                return self.PLAYER_WIN
            else:
                return self.COMPUTER_WIN

    def play_game(self):
        tracker = result_tracker()
        initials = input("Please enter your initials:")

        tracker.print_previous_results(initials)

        while (True):
            self.present_player_choices()
            player_move = self.choose_move()

            if (player_move == 0):
                break

            computer_move = self.computer_choice()

            result = self.determine_result(player_move, computer_move)

            print(result)
            tracker.store_result(initials, result)
