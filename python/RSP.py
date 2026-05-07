# RSP Game
from enum import Enum


class RSP(Enum):
    ROCK = 1
    SCISSORS = 2
    PAPER = 3

    # def __str__(self):
    #     return self.name


print(RSP.ROCK.name)
