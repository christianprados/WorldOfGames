#!/usr/bin/python3
from Utils import input_with_validation_integer
import time
import random


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
    print(f"The Numbers Are:   {randomlist}", end='')
    time.sleep(0.7)
    ## Hide the numbers after 0.7 seconds
    print(end='\r')
    print("Try to remember")
    userlist = get_list_from_user(difficulty)

    if is_list_equal(randomlist,userlist):
        print("You have Won the Memory Game")
    else:
        print("You have lost the Memory Game")




