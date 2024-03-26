#!/usr/bin/python3
import Score
from Utils import input_with_validation_integer
import time
import random
import sys


def generate_sequence(difficulty):
    randomlist = []
    for i in range(0, difficulty):
        randomlist.append(random.randint(1, 101))
    return randomlist


def get_list_from_user(difficulty):
    userlist = []
    for i in range(0, difficulty):
        userlist.append(input_with_validation_integer("Enter a number: "))
    return userlist


def is_list_equal(lista, listb):
    if lista == listb:
        return True
    else:
        return False

def play(difficulty):
    print(f"Your Difficulty is {difficulty}")
    randomlist = generate_sequence(difficulty)
    print("Focuse on the number in",)
    #Counter to tell the user to start concentrate before the number appears
    counter = 5
    for i in range(5):
        print(counter, end='')
        time.sleep(1)
        print(end='\r')
        counter-=1

    print(f"The Numbers Are: {randomlist}", end='')

    time.sleep(0.7)

    ## Hide the numbers after 0.7 seconds

    sys.stdout.write('\r')
    sys.stdout.flush()

    print("Try to remember")

    userlist = get_list_from_user(difficulty)

    if is_list_equal(randomlist,userlist):
        print("You have Won the Memory Game")
        # add the score to scores.txt
        Score.add_score(difficulty)
    else:
        print("You have lost the Memory Game")




