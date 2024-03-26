#!/usr/bin/python3
from Utils import input_with_validation_integer
import random
import Score


def gen_secret_number(difficulty):
    return random.randint(1,difficulty)

def get_guess_from_user(difficulty):
    while True:
        guess_number = input_with_validation_integer(f"Choose a number between  1 and {difficulty}")
        if guess_number <= difficulty:
            return guess_number
        else:
            print(f"The number is high than {difficulty}, please try again")

def compare_results(secret_number,guess_number):
    if secret_number == guess_number:
        return True
    else:
        return False

def play(difficulty):
    print(f"Your Difficulty is {difficulty}")
    secret_number = gen_secret_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    if compare_results(secret_number,user_number):
        print("You have Won the Guess Game")
        # add the score to scores.txt
        Score.add_score(difficulty)
    else:
        print("You have lost the Guess Game")



