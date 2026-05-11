# RSP Game

import os
import sys
import random
import time
from enum import Enum


# Variables store the game score
player_score = 0
computer_score = 0


class RSP(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
        return self.name.capitalize()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def determine_winner(player, computer):
    global player_score
    global computer_score

    if player == computer:
        print("Tie Game 😒😒")

    elif (
        (player == RSP.ROCK and computer == RSP.SCISSORS)
        or (player == RSP.PAPER and computer == RSP.ROCK)
        or (player == RSP.SCISSORS and computer == RSP.PAPER)
    ):
        player_score += 1
        print("Player Wins 🎉🎉")

    else:
        computer_score += 1
        print("Computer Wins 😢😢")


def view_score():
    clear()

    print("===== SCORE =====\n")
    print(f"Player Score".ljust(20, ".") + str(player_score))
    print(f"Computer Score".ljust(20, ".") + str(computer_score))

    input("\nPress Enter to continue...")


def reset_score():
    global player_score
    global computer_score

    player_score = 0
    computer_score = 0

    print("\nScores Reset Successfully ✅")
    time.sleep(1)


def welcome():
    clear()

    print("===== ROCK PAPER SCISSORS =====\n")

    print("Play".ljust(20, ".") + "1")
    print("View Score".ljust(20, ".") + "2")
    print("Reset Score".ljust(20, ".") + "3")
    print("Exit".ljust(20, ".") + "4")


def game():
    clear()

    player_choice = 0

    while player_choice not in [1, 2, 3]:
        try:
            player_choice = int(
                input(
                    "Choose:\n"
                    "1 - Rock\n"
                    "2 - Paper\n"
                    "3 - Scissors\n\n> "
                )
            )

        except ValueError:
            player_choice = 0

    computer_choice = random.randint(1, 3)

    player = RSP(player_choice)
    computer = RSP(computer_choice)

    clear()

    print(f"You Chose      : {player}")
    print(f"Computer Chose : {computer}\n")

    determine_winner(player, computer)

    input("\nPress Enter to continue...")


# Main Loop
while True:

    welcome()

    choice = 0

    while choice not in [1, 2, 3, 4]:

        try:
            choice = int(input("\nSelect Option: "))

        except ValueError:
            choice = 0

    if choice == 1:
        game()

    elif choice == 2:
        view_score()

    elif choice == 3:
        reset_score()

    elif choice == 4:
        clear()
        print("Thanks For Playing 👋")
        sys.exit()
