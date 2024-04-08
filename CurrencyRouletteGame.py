#!/usr/bin/python3

from Utils import input_with_validation_float
import requests
import random
import Score


def fetch_money_interval(difficulty):
    json_post = {"difficulty": difficulty}
    interval = requests.post("http://127.0.0.1:30000/Money_interval", json=json_post).json()
    return interval


def get_guess_from_user(message):
    return input_with_validation_float(message)

def play(difficulty):

    number_of_dollars = random.randint(1, 100)

    print(f"What is the value in ILS of {number_of_dollars} dollars")

    guess = get_guess_from_user("Make a Guess: ")

    guess_interval = number_of_dollars * fetch_money_interval(difficulty)["interval"][0], number_of_dollars * fetch_money_interval(difficulty)["interval"][1]
    print(guess_interval[0],guess_interval[1])
    if guess_interval[0] <= guess <= guess_interval[1]:
        print("You Won the CurrencyRoulette Game")
        #add the score to scores.txt
        Score.add_score(difficulty)
    else:
        print("You lost the CurrencyRouletteGame")


