import random

__author__ = 'Valdimar Gunnarsson'

comboMap = {
    1: "ones",
    2: "twos",
    3: "threes",
    4: "fours",
    5: "fives",
    6: "sixes",
    7: "one pair",
    8: "two pairs",
    9: "three of a kind",
    10: "four of a kind",
    11: "small straight",
    12: "large straight",
    13: "full house",
    14: "chance",
    15: "yatzy"
}


def show_score(player_score):
    print("Your current score is: %d" % player_score)


def show_dice(dice_list):
    for i in range(0, len(dice_list)):
        print("Dice %d: %d" % ((i + 1), dice_list[i]))


def roll(dice_list):
    for i in range(0, len(dice_list)):
        dice_list[i] = random.randint(1, 6)
        print("Dice %d: %d" % ((i + 1), dice_list[i]))


def reroll(dice, dice_list):
    for item in dice:
        dice_list[item - 1] = random.randint(1, 6)
    show_dice(dice_list)


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
    else:
        return 0


def four_kind(dice_list):
    four = []
    for i in range(0, 6):
        if dice_list.count((i+1)) >= 4:
            four.append((i+1))
    if len(four) > 0:
        return max(four) * 4
    else:
        return 0


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


def full_house(dice_list):
    house = []
    for i in range(0, 6):
        if dice_list.count((i+1)) >= 3:
            house.append((i+1))
    if len(house) > 1:
        for i in range(0, 6):
            if dice_list.count(i+1) >= 2 and i != house[0]:
                house.append((i+1))
                return (house[0] * 3) + (house[1] * 2)
    else:
        return 0


def yatzy(dice_list):
    for i in range(0, 6):
        if dice_list.count(i+1) == 5:
            return 50
    else:
        return 0


playerScore = 0
playerDice = [None] * 5
roundCounter = 0

print("Please enter number of dice you wish to reroll in this format: '1 2 3 4 5'")
print("If you do not wish to reroll simply press enter when prompted")

while roundCounter < 15:
    print("\nRolling dice\n")
    roll(playerDice)
    roundCounter += 1
    print("\nRolling for %s\n" % comboMap[roundCounter])
    for i in range(0, 2):
        rerollString = raw_input("Reroll your dice: ")
        if rerollString != '':
            rerollList = rerollString.split(' ')
            rerollList = [int(i) for i in rerollList]
            reroll(rerollList, playerDice)
        else:
            break

    # Ridiculously long if/else block since there is no switch in python
    if roundCounter == 1:
        print("You gain %d points." % dice_num(playerDice, 1))
        playerScore += dice_num(playerDice, 1)
    elif roundCounter == 2:
        print("You gain %d points." % dice_num(playerDice, 2))
        playerScore += dice_num(playerDice, 2)
    elif roundCounter == 3:
        print("You gain %d points." % dice_num(playerDice, 3))
        playerScore += dice_num(playerDice, 3)
    elif roundCounter == 4:
        print("You gain %d points." % dice_num(playerDice, 4))
        playerScore += dice_num(playerDice, 4)
    elif roundCounter == 5:
        print("You gain %d points." % dice_num(playerDice, 5))
        playerScore += dice_num(playerDice, 5)
    elif roundCounter == 6:
        print("You gain %d points." % dice_num(playerDice, 6))
        playerScore += dice_num(playerDice, 6)
        if playerScore >= 63:
            print("Congrats! You scored at least 63 in the upper section, netting you a bonus of 50 points!")
            playerScore += 50
    elif roundCounter == 7:
        print("You gain %d points." % one_pair(playerDice))
        playerScore += one_pair(playerDice)
    elif roundCounter == 8:
        print("You gain %d points." % two_pairs(playerDice))
        playerScore += two_pairs(playerDice)
    elif roundCounter == 9:
        print("You gain %d points." % three_kind(playerDice))
        playerScore += three_kind(playerDice)
    elif roundCounter == 10:
        print("You gain %d points." % four_kind(playerDice))
        playerScore += four_kind(playerDice)
    elif roundCounter == 11:
        print("You gain %d points." % small_straight(playerDice))
        playerScore += small_straight(playerDice)
    elif roundCounter == 12:
        print("You gain %d points." % large_straight(playerDice))
        playerScore += large_straight(playerDice)
    elif roundCounter == 13:
        print("You gain %d points." % full_house(playerDice))
        playerScore += full_house(playerDice)
    elif roundCounter == 14:
        print("You gain %d points." % sum(playerDice))
        playerScore += sum(playerDice)
    elif roundCounter == 15:
        print("You gain %d points." % yatzy(playerDice))
        playerScore += yatzy(playerDice)

print("Game over!\nYour total score is: %d" % playerScore)
