import random

__author__ = 'Valdimar Gunnarsson'


# Creates the code by recursively assigning numbers that are not already in the list
def create_code(code_list):

    # Sets a random number to a variable
    num = random.randint(1, 8)

    # Checks whether the code has reached a satisfactory length
    if len(code_list) != 5:

        # Checks whether the code is empty
        if len(code_list) == 0:

            # If it is append a random number as the first item and then call the function again
            code_list.append(num)
            return create_code(code_list)
        else:

            # Checks if any single item of the code has the same number as the random one
            for item in code_list:

                # If it does call the function again
                if item == num:
                    return create_code(code_list)

            # After the loop has checked every item and the random number is unique, append to code and call function
            code_list.append(num)
            return create_code(code_list)

    # If the code has reached a satisfacory length, return the list
    else:
        return code_list


# Proccesses the player's guess
def proccess_guess(guess_list):
    # Declares variables
    right_num = 0
    right_place_num = 0

    # Loops through every item in the guess and compares it to the code
    for item in guess_list:
        for i in range(0, len(guess_list)):
            if item == code[i]:
                right_num += 1
    for i in range(0, len(guess_list)):
        if guess_list[i] == code[i]:
            right_place_num += 1

    # Prints out hints to help the player make a better guess next time
    print("Right numbers: " + str(right_num))
    print("Right numbers in right place: " + str(right_place_num))


# Code executes here
while True:
    # Initalizes variables
    code = []
    guessCounter = 0

    # Creates the code
    create_code(code)

    # starts the game itself
    print("When guessing code please use format: '1 2 3 4 5'")
    while True:
        codeGuessString = raw_input("Guess the code: ")
        codeGuessList = codeGuessString.split(' ')
        codeGuessList = [int(i) for i in codeGuessList]
        proccess_guess(codeGuessList)
        guessCounter += 1

        # Checks whether the answer was right or not
        if codeGuessList == code:
            if guessCounter > 1:
                print("You win after " + str(guessCounter) + " guesses.")
            else:
                print("You win after a single guess")
            break

        # Checks if player has run out of tries
        elif guessCounter == 12:
            print("You exceeded the maximum amount of guesses.\nYou lose!")
            break

    # Asks the player if he wishes to play another round
    choice = raw_input("Do you wish to play again?(y/n)")
    if choice == 'n':
        break
