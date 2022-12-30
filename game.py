import random as r
import sys


class RockPaperScissors:
    def __init__(self):
        self.default_choices = ["rock", "paper", "scissors"]
        self.player_choices = None
        self.player = ""
        self.computer = ""
        self.winner = ""
        self.name = ""
        self.score = 0

    def get_player_name(self):
        self.name = input("Enter your name: ")
        print(f"Hello, {self.name}")

    def check_file_scores(self):
        f = open('rating.txt', 'r')
        for line in f:
            if line.startswith(f"{self.name}"):
                self.score = int(line.strip(f"{self.name}"))
        f.close()

    def get_player_input(self):
        valid = False
        while not valid:
            self.player = input().lower()
            valid = self.validate_player_input()

    def get_player_choices(self):
        self.player_choices = [x for x in input().lower().split(",")]
        if self.player_choices == [""]:
            self.player_choices = self.default_choices
        print("Okay, let's start")

    def validate_player_input(self):
        valid_choices = ["!exit", "!rating"]
        if self.player in self.player_choices:
            return True
        elif self.player == valid_choices[0]:
            print("Bye!")
            sys.exit()
        elif self.player == valid_choices[1]:
            self.give_rating()
            return False
        else:
            print("Invalid input")
            return False

    def give_rating(self):
        print(f"Your rating: {self.score}")

    def computer_turn(self):
        self.computer = r.choice(self.player_choices)

    def determine_winner(self):
        # re-order list for winning choices to be in the first half, if player choice not the last element
        re_ordered_choices = [x for x in self.player_choices]
        if re_ordered_choices.index(self.player) != len(self.player_choices) - 1:
            for x in re_ordered_choices[-1: re_ordered_choices.index(self.player): -1]:
                re_ordered_choices.insert(0, x)
                re_ordered_choices.pop()
        # remove player choice from list
        re_ordered_choices.pop(re_ordered_choices.index(self.player))
        winning_choice = re_ordered_choices[:int(len(re_ordered_choices) / 2)]

        if self.player == self.computer:
            self.winner = "draw"
            self.score += 50
        elif self.computer in winning_choice:
            self.winner = "computer"
        else:
            self.winner = "player"
            self.score += 100

    def display_winner(self):
        if self.winner == "draw":
            print(f"There is a draw {self.computer}")
        elif self.winner == "player":
            print(f"Well done. The computer chose {self.computer} and failed")
        else:
            print(f"Sorry, but the computer chose {self.computer}")

    def game_loop(self):
        self.get_player_name()
        self.check_file_scores()
        self.get_player_choices()
        while True:
            self.get_player_input()
            self.computer_turn()
            self.determine_winner()
            self.display_winner()

game = RockPaperScissors()
game.game_loop()

