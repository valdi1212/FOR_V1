import random
import math

__author__ = 'Valdimar Gunnarsson'

guessCounter = 0
correctNumber = random.randint(1, 100)

while True:
    guessedNumber = int(input("Please guess a number between 1 and 100: "))
    guessCounter += 1
    if guessCounter == 8:
        print("Sorry, you ran out of tries")
        print("The correct number was " + str(correctNumber))
        break
    elif guessedNumber == correctNumber:
        score = int(10 * (math.pow(2, 8 - guessCounter)))
        print("Congratulations! You guessed the right number. Your score is " + str(score))
        break
    elif guessedNumber < correctNumber:
        print("That number is too low.\n")
    elif guessedNumber > correctNumber:
        print("That number is too high.\n")
