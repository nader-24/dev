# RSP Game
import os
import sys
import random
from enum import Enum
import time

# variables store the game score
player_score = 0
computer_score = 0
choice = 0
player_choice = 0
computer_choice = 0


class RSP(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
        return self.name


def determine_winner(player, computer):
    global player_score
    global computer_score
    if player == computer:
        print("Tie Game😒😒")
    elif (
        (player == RSP.ROCK and computer == RSP.SCISSORS)
        or (player == RSP.PAPER and computer == RSP.ROCK)
        or (player == RSP.SCISSORS and computer == RSP.PAPER)
    ):
        player_score += 1
        print("Player Wins🎉🎉")
    else:
        computer_score += 1
        print("Computer Wins😢😢")


def view_score():
    global choice
    choice = 0
    print(f"Player Score".ljust(19, ".") + str(player_score))
    print(f"Computer Score".ljust(19, ".") + str(computer_score))
    time.sleep(5)


def welcome():
    global choice
    choice = 0
    os.system("cls")
    print("Welcome to RSP Game\n")
    print("2 Play".ljust(19, ".") + "1")
    print("2 View Score".ljust(19, ".") + "2")
    print("2 Rest Score".ljust(19, ".") + "3")
    print("2 Exit".ljust(19, ".") + "4")


def reset_score():
    global choice
    choice = 0
    global player_score
    global computer_score
    player_score = 0
    computer_score = 0


def game():
    global player_choice
    while player_choice not in [1, 2, 3]:
        player_choice = int(
            input('Enter...\n1 For Rock\n2 For Paper\n3 For Scissors'))
    computer_choice = random.randint(1, 3)
    determine_winner(player_choice, computer_choice)
    x = input("")
    welcome()


while True:

    while choice not in [1, 2, 3, 4]:
        os.system('cls')
        welcome()
        choice = int(input())

    if choice == 4:
        sys.exit()
    elif choice == 3:
        reset_score()
    elif choice == 2:
        view_score()
    else:
        game()
