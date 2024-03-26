#!/usr/bin/python3

from Utils import input_with_validation_float
import requests
import random
import Score


def get_money_interval(difficulty):
    response = requests.get(
        'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_47QYRoRYGfieLsGi0sSjQNPBkDv9Gp4aDJanJ1xR'
        '&currencies=ILS')
    currency = response.json()
    t = currency['data']['ILS']
    return t - (5 - difficulty), t + (5 - difficulty)


def get_guess_from_user(message):
    return input_with_validation_float(message)

def play(difficulty):

    number_of_dollars = random.randint(1, 100)

    print(f"What is the value in ILS of {number_of_dollars} dollars")

    guess = get_guess_from_user("Make a Guess: ")

    guess_interval = number_of_dollars * get_money_interval(difficulty)[0], number_of_dollars * get_money_interval(difficulty)[1]

    if guess_interval[0] <= guess <= guess_interval[1]:
        print("You Won the CurrencyRoulette Game")
        #add the score to scores.txt
        Score.add_score(difficulty)
    else:
        print("You lost the CurrencyRouletteGame")


