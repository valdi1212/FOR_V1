import random

__author__ = 'Valdimar Gunnarsson'
cardMap = {
    1: 'A',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'J',
    12: 'Q',
    13: 'K'
}

cardValues = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}


def keep_playing():
    print("Do you wish to play another round?(y/n)")
    while True:
        choice = input()
        if choice == 'y':
            super.keepPlaying = True
            break
        elif choice == 'n':
            super.keepPlaying = False
            break
        else:
            print("Wrong input. Please try again")


def show_points():
    print("Your points: " + str(points))


def show_cards(card_list):
    card_string = ''
    if len(card_list) > 1:
        for i in range(0, len(card_list) - 1):
            card_string += card_list[i] + ', '
    card_string += card_list[len(card_list) - 1]
    return card_string


def add_total(card_list, total, is_player):
    if (card_list[-1] != 'A') or (is_player is False):
        total += cardValues[card_list[-1]]
    else:
        print("You have been dealt an ace.\nDo you wish to count its value as 11(y/n)")
        while True:
            choice = input()
            if choice == 'y':
                total += 11
                break
            elif choice == 'n':
                total += 1
                break
            else:
                print("Wrong input. Please try again")
    return total


def deal_cards(card_list):
    rand = random.randint(1, 13)
    return card_list.append(cardMap[rand])


def start_round():
    deal_cards(playerCards)
    add_total(playerCards, playerTotal, True)
    deal_cards(playerCards)
    add_total(playerCards, playerTotal, True)
    deal_cards(dealerCards)
    add_total(dealerCards, dealerTotal, False)
    deal_cards(dealerCards)
    add_total(dealerCards, dealerTotal, False)
    print("Dealers's upface card: " + dealerCards[0])
    print("Your cards: " + show_cards(playerCards))


def show_menu():
    print("\nType 'hit' to receive another card.")
    print("Type 'stand' to stop recieving cards.\n")
    while True:
        choice = input()
        if choice == 'hit':
            deal_cards(playerCards)
            add_total(playerCards, playerTotal, True)
            print("Your cards: " + show_cards(playerCards))
            break
        elif choice == 'stand':
            print("You chose to stand")
            # do something?
            break
        else:
            print("Wrong input. Please try again.")


keepPlaying = True
points, bet = 50000, 0
playerCards, dealerCards = [], []
playerTotal, dealerTotal = 0, 0

while keepPlaying:
    bet = 0
    show_points()
    while bet == 0:
        bet = int(input("How much do you want to bet?"))
        if bet > points:
            print("You can't bet more than you have.")
            bet = 0
        elif bet < 500:
            print("Minimum bet is 500")
            bet = 0
    points -= bet
    start_round()
    while True:
        show_menu()
        print(playerTotal)
        if playerTotal > 21:
            print("You go bust and lose " + str(bet) + " points.")
            break
        elif dealerTotal > 21:
            print("The dealer goes bust, causing you to win " + str(bet) + " points.")
            bet *= 2
            points += bet
            break
    keep_playing()
