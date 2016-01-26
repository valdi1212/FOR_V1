import random

__author__ = 'Valdimar Gunnarsson'


def check_score(player_score):
    print("Your current score is: %d" % player_score)


def roll(player_dice):
    for i in range(0, 5):
        player_dice[i] = random.randint(1, 6)
        print("Dice %d: %d" % ((i + 1), player_dice[i]))


def reroll(dice, player_dice):
    for item in dice:
        player_dice[item - 1] = random.randint(1, 6)


def dice_num(dice_list, dice_num):
    temp_score = 0
    for dice in dice_list:
        if dice == dice_num:
            temp_score += dice
    return temp_score


def one_pair(dice_list):
    pairs = []
    for i in range(0, 6):
        if dice_list.count((i+1)) >= 2:
            pairs.append((i+1))
    if len(pairs) > 0:
        return max(pairs) * 2
    else:
        return 0


def two_pairs(dice_list):
    pairs = []
    for i in range(0, 6):
        if dice_list.count((i+1)) >= 2:
            pairs.append((i+1))
    if len(pairs) == 2:
        return sum(pairs) * 2
    else:
        return 0


def three_kind(dice_list):
    three = []
    for i in range(0, 6):
        if dice_list.count((i+1)) >= 3:
            three.append((i+1))
    if len(three) > 0:
        return max(three) * 3


def four_kind(dice_list):
    four = []
    for i in range(0, 6):
        if dice_list.count((i+1)) >= 4:
            four.append((i+1))
    if len(four) > 0:
        return max(four) * 4


def small_straight(dice_list):
    if all(x in dice_list for x in [1, 2, 3, 4, 5]):
        return sum(dice_list)
    else:
        return 0


def large_straight(dice_list):
    if all(x in dice_list for x in [2, 3, 4, 5, 6]):
        return sum(dice_list)
    else:
        return 0


def yatzy(dice_list):
    if dice_list.count[dice_list[0]] == 5:
        return 50
    else:
        return 0


playerScore = 0
playerDice = [None] * 5

print("Testing player_roll function:")

roll(playerDice)

rerollString = raw_input("Reroll your dice: ")
if rerollString != '':
    rerollList = rerollString.split(' ')
    rerollList = [int(i) for i in rerollList]
    reroll(rerollList, playerDice)
print(playerDice)
one_pair(playerDice)
