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


def show_points():
    print("Your points: " + str(points))


def show_cards(card_list):
    card_string = ''
    if len(card_list) > 1:
        for i in range(0, len(card_list) - 1):
            card_string += card_list[i] + ', '
    card_string += card_list[len(card_list) - 1]
    return card_string


def add_total(card_list, is_player=False):
    if card_list[-1] != 'A' and is_player is True:
        playerTotal.append(cardValues[card_list[-1]])
    elif is_player is False:
        dealerTotal.append(cardValues[card_list[-1]])
    else:
        print("You have been dealt an ace.\nDo you wish to count its value as 11(y/n)")
        while True:
            choice = raw_input()
            if choice == 'y':
                playerTotal.append(11)
                break
            elif choice == 'n':
                playerTotal.append(1)
                break
            else:
                print("Wrong input. Please try again")


def deal_cards(card_list, is_player=False):
    rand = random.randint(1, 13)
    card_list.append(cardMap[rand])
    add_total(card_list, is_player)


def start_round():
    for i in range(0, 2):
        deal_cards(playerCards, True)
        deal_cards(dealerCards)
    print("Dealers's upface card: " + dealerCards[0])
    print("Your cards: " + show_cards(playerCards))


def show_menu():
    print("\nType 'hit' to receive another card.")
    print("Type 'stand' to stop recieving cards.\n")
    while True:
        choice = raw_input()
        if choice == 'hit':
            deal_cards(playerCards, True)
            print("Your cards: " + show_cards(playerCards))
            break
        elif choice == 'stand':
            print("You chose to stand")
            break
        else:
            print("Wrong input. Please try again.")


keepPlaying = True
points = 50000

while keepPlaying:
    playerCards, dealerCards = [], []
    playerTotal, dealerTotal = [], []
    bet = 0
    show_points()
    while bet == 0:
        bet = int(raw_input("How much do you want to bet?"))
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
        if sum(dealerTotal) <= 17:
            deal_cards(dealerCards)
        print(playerTotal)
        if sum(playerTotal) > 21:
            print("You go bust and lose " + str(bet) + " points.")
            print("Your cards: " + show_cards(playerCards))
            print("Dealer's cards " + show_cards(dealerCards))
            break
        elif sum(dealerTotal) > 21:
            print("The dealer goes bust, causing you to win " + str(bet) + " points.")
            print("Your cards: " + show_cards(playerCards))
            print("Dealer's cards " + show_cards(dealerCards))
            bet *= 2
            points += bet
            break
        elif sum(dealerTotal) > 17:
            if sum(playerTotal) > sum(dealerTotal):
                print("You have a higher hand than the dealer, causing you to win " + str(bet) + " points.")
                print("Your cards: " + show_cards(playerCards))
                print("Dealer's cards " + show_cards(dealerCards))
                bet *= 2
                points += bet
                break
            elif sum(playerTotal) < sum(dealerTotal):
                print("The dealer has a higher hand than you, causing you to lose " + str(bet) + " points.")
                print("Your cards: " + show_cards(playerCards))
                print("Dealer's cards " + show_cards(dealerCards))
                break
            elif sum(playerTotal) == sum(dealerTotal):
                print("You both have an equal hand, meaning the game ends in a tie")
                print("Your cards: " + show_cards(playerCards))
                print("Dealer's cards " + show_cards(dealerCards))
                break
    if points == 0:
        print("You have run out of points, ending the game. :c")
    else:
        print("Do you wish to play another round?(y/n)")
        while True:
            choice = raw_input()
            if choice == 'y':
                keepPlaying = True
                break
            elif choice == 'n':
                keepPlaying = False
                break
            else:
                print("Wrong input. Please try again")
