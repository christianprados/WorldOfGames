#!/usr/bin/python3
from Utils import input_with_validation_integer
import Score
import requests


def request_secret_number(difficulty):
    json_post = {"difficulty": difficulty}
    response = requests.post("http://worldofgamesapi:30000/Generate_Secret", json=json_post)
    secret = response.json()
    return secret["secret"]

def get_guess_from_user(difficulty):
    while True:
        guess_number = input_with_validation_integer(f"Choose a number between  1 and {difficulty}")
        if guess_number <= difficulty:
            return guess_number
        else:
            print(f"The number is high than {difficulty}, please try again")

def fetch_compare_result(secret_number,guess_number):
    json_post = {"data1":secret_number,"data2":guess_number}
    result = requests.post("http://worldofgamesapi:30000/Compare",json=json_post).json()
    return result["result"]

def play(difficulty):
    print(f"Your Difficulty is {difficulty}")
    secret_number = request_secret_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    if fetch_compare_result(secret_number,user_number):
        print("You have Won the Guess Game")
        # add the score to scores.txt
        Score.add_score(difficulty)
    else:
        print("You have lost the Guess Game")



