#!/usr/bin/python3
import Score
from Utils import input_with_validation_integer
import time
import random
import sys
import requests

#The function sends the difficulty t the backend to generate a random sequence
def request_sequence(difficulty):
    json_post = {"difficulty": f"{difficulty}"}
    response = requests.post("http://127.0.0.1:30000/Generate_Sequence", json=json_post)
    randomlist = response.json()
    return randomlist["sequence"]

#Get the numbers from the users and send them to the backend server to generate the user list
def get_list_from_user(difficulty):
    for i in range(0, difficulty):
        number = input_with_validation_integer("Enter a number: ")
        json_post = {"number": number}
        requests.post("http://127.0.0.1:30000/User_list", json=json_post)
    response = requests.get("http://127.0.0.1:30000/User_list")
    userlist = response.json()
    print(type(userlist["userlist"]), userlist["userlist"])
    return userlist["userlist"]



def is_list_equal(lista, listb):
    json_post = {"data1":lista,"data2":listb}
    result = (requests.post("http://127.0.0.1:30000/Compare", json=json_post)).json()

    return result["result"]


def play(difficulty):
    print(f"Your Difficulty is {difficulty}")
    #call the generate sequence function
    randomlist = request_sequence(difficulty)
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

    #Hide the numbers after 0.7 seconds

    sys.stdout.write('\r')
    sys.stdout.flush()

    print("Try to remember")
    #call the user list function
    userlist = get_list_from_user(difficulty)

    if is_list_equal(randomlist,userlist):
        # add the score to scores.txt
        Score.add_score(difficulty)
        return {"Result": True, "Message": "You have Won the Memory Game"}

    else:
        return {"Result": False, "Message" : "You have lost the Memory Game"}




