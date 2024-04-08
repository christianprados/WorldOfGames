import os
from flask import Flask, abort, request, jsonify
import Utils
import random
from copy import deepcopy
import requests

app = Flask(__name__)

# Global Variables FOR THE API

USERLIST = []

###################  Memory Game End Points #########################################
# API Endpoint to Generate a Random Sequence of Numbers for the Memory Game
@app.post("/Generate_Sequence")
def generate_sequence():
    if request.is_json:
        # randmlist is ephemeral
        randomlist = []
        data = request.get_json()
        for i in range(0, int(data["difficulty"])):
            randomlist.append(random.randint(1, 101))
        return jsonify({"sequence": randomlist}) , 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400


# API Endpoint to post the numbers of the USERLIST, get USERLIST and DELETE the USERLIST
@app.post("/User_list")
def post_user_list():
    if request.is_json:
        number = request.get_json()
        USERLIST.append(number["number"])
        return jsonify({"message": "User number added successfully"}), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400


@app.get("/User_list")
def get_user_list():
    list_to_send = deepcopy(USERLIST)
    # Clear USERLIST for the next game
    USERLIST.clear()
    return jsonify({"userlist": list_to_send}), 200

###################  Guess Game End Points #########################################

@app.post("/Generate_Secret")
def gen_secret_number():
    if request.is_json:
        json_data = request.get_json()
        secret_number = random.randint(1, json_data["difficulty"])
        return jsonify({"secret": secret_number}), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400


################   Currency Roulette Game  End Points  ##################

@app.post("/Money_interval")
def get_money_interval():
    if request.is_json:
        #Extract the difficulty value from the json post
        json_data = request.get_json()
        #get the current ILS currency value
        response = requests.get(
            'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_47QYRoRYGfieLsGi0sSjQNPBkDv9Gp4aDJanJ1xR'
            '&currencies=ILS')
        currency = response.json()
        t = currency['data']['ILS']
        #calculate the money interval
        money_interval = t - (5 - json_data["difficulty"]), t + (5 - json_data["difficulty"])
        return jsonify({"interval": money_interval}),200


##APA ENPOINT THAT RECEIVES ANE COMPARE TWO VALUES, USED BY MEMORYGAME AND GUESSGAME
@app.post("/Compare")
def compare_data():
    if request.is_json:
        json_data = request.get_json()
        data1 = json_data["data1"]
        data2 = json_data["data2"]
        if data1 == data2:
            return jsonify({"result":True}), 200
        else:
            return jsonify({"result":False}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route("/Score")
def score_server():
    try:
        with open('Scores.txt', 'r') as file:
            SCORE = file.read()
        return f"""<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                        <h1>The score is <div id="score">{SCORE}</div></h1>
                        </body>
                </html>"""
    except:
        return f"""<html>
                            <head>
                                    <title>Scores Game</title>
                            </head>
                            <body>
                                <h1><div id="score" style="color:red">{Utils.BAD_RETURN_CODE}</div></h1>
                            </body>
                    </html>"""


if __name__ == '__main__':
    # host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', '30000')
    app.run(port=int(port), debug=True)
