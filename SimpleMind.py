import random

__author__ = 'Valdimar Gunnarsson'

code = []
guessCounter = 0


def create_code(code_list):
    num = random.randint(1, 8)
    if len(code_list) != 5:
        if len(code_list) == 0:
            code_list.append(num)
            return create_code(code_list)
        else:
            for item in code_list:
                if item == num:
                    return create_code(code_list)
            code_list.append(num)
            return create_code(code_list)
    else:
        return code_list


def proccess_guess(guess_list):
    right_num = 0
    right_place_num = 0
    for item in guess_list:
        for i in range(0, len(guess_list)):
            if item == code[i]:
                right_num += 1
    for i in range(0, len(guess_list)):
        if guess_list[i] == code[i]:
            right_place_num += 1
    print("Right numbers: " + str(right_num))
    print("Right numbers in right place: " + str(right_place_num))


create_code(code)
print("When guessing code please use format: '1 2 3 4 5'")
while True:
    codeGuessString = raw_input("Guess the code: ")
    codeGuessList = codeGuessString.split(' ')
    codeGuessList = [int(i) for i in codeGuessList]
    proccess_guess(codeGuessList)
    guessCounter += 1
    if codeGuessList == code:
        if guessCounter > 1:
            print("You win after " + str(guessCounter) + " guesses.")
        else:
            print("You win after a single guess")
        break
    elif guessCounter == 8:
        print("You exceeded the maximum amount of guesses.\nYou lose!")
        break
