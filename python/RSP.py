# RSP Game

from enum import Enum
import sys
import os

player1_score = 0
player2_score = 0
choice = str()


class RSP(Enum):
    ROCK = 1
    SCISSORS = 2
    PAPER = 3

    def __str__(self):
        return self.name


def decide_winner(player1, player2):
    if player1 == RSP.ROCK and player2 == RSP.SCISSORS:
        print("Player 1 wins🎉🎉🎊")
        player1_score += 1
    elif player1 == RSP.SCISSORS and player2 == RSP.PAPER:
        print("Player 1 wins🎉🎉🎊")
        player1_score += 1
    elif player1 == RSP.PAPER and player2 == RSP.ROCK:
        print("Player 1 wins🎉🎉🎊")
        player1_score += 1
    else:
        print("Player 2 Wins🎉🎉🎊 ")
        player2_score += 1


def show_score():
    print("player 1".ljust(15, '.')+str(player1_score))
    print("player 2".ljust(15, '.')+str(player2_score))


def welcome():
    os.system('cls')
    print("welcome".title().center(20, '-'))
    print("2 play".ljust(19, '.')+'1')
    print("2 score".ljust(19, '.')+'2')
    print("2 exit".ljust(19, '.')+'3')
    choice = input("")
    return choice


no = welcome()
while no not in "123":
    no = welcome()


os.system('exit')
