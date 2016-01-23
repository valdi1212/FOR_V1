import random

__author__ = 'Valdimar Gunnarsson'

code = []


def create_code(code_list):
    num = random.randint(1, 8)
    for i in range(0, 5):
        while True:
            for item in code_list:
                if item == num:
                    num = random.randint(1, 8)
            if len(code_list) > 0:
                if num == code_list[-1]:
                    num = random.randint(1, 8)
                else:
                    code_list.append(num)
                    break
            else:
                code_list.append(num)
                break
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
print(code)
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print(create_code([]))
print("When guessing code please use format: '1 2 3 4 5'")
codeGuessString = input("Guess the code: ")
codeGuessList = codeGuessString.split(' ')
codeGuessList = [int(i) for i in codeGuessList]
proccess_guess(codeGuessList)
