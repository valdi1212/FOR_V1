import random

__author__ = 'Valdimar Gunnarsson'


def check_score(player_score):
    print("Your current score is: " + str(player_score))


def roll(player_dice):
    for i in range(0, 5):
        player_dice[i] = random.randint(1, 6)
        print("Dice %d: %d" % ((i + 1), player_dice[i]))


def reroll(dice, player_dice):
    for item in dice:
        player_dice[item - 1] = random.randint(1, 6)

playerScore = 0
playerDice = [None] * 5
print("Welcome to yahtzee.")
print("To see your score in between rounds, simply type 'score'")
print("To reroll your dice type 'reroll'")
print("To pick which dice you wish to reroll, and which to keep, type their numbers in a row.")
print("E.g. '1,3,4' This would keep dice number 2 and 5, but reroll dice number 1, 3 and 4")
print("If you wish to reroll all your dice type '0'")
print("Starting game now.\n")

print("Testing player_roll function:")

roll(playerDice)

rerollString = raw_input("Reroll your dice: ")
rerollList = rerollString.split(',')
rerollList = [int(i) for i in rerollList]
reroll(rerollList, playerDice)
print(playerDice)
