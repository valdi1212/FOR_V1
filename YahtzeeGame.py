import random

__author__ = 'Valdimar Gunnarsson'


def check_score():
    """This function checks the score of the player and prints it in the console."""
    print("Your current score is: " + str(Yahtzee.playerScore))


def player_roll():
    """This function rolls the dice for the player"""
    for i in range(0, 5):
        Yahtzee.playerDice[i] = random.randint(1, 6)
        print("Dice %d: " + str(Yahtzee.playerDice[i]) % (i + 1))


class Yahtzee:
    playerScore, compScore = 0, 0
    playerDice, compDice = [], []
    print("Welcome to yahtzee.")
    print("To see your score in between rounds, simply type 'score'")
    print("To reroll your dice type 'reroll'")
    print("To pick which dice you wish to reroll, and which to keep, type their numbers in a row.")
    print("E.g. '1,3,4' This would keep dice number 2 and 5, but reroll dice number 1, 3 and 4")
    print("If you wish to reroll all your dice type '0'")
    print("Starting game now.\n")

    print("Testing player_roll function:")

    player_roll()
