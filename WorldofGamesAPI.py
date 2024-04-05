import os
from flask import Flask, abort, request, jsonify
import Utils
import MemoryGame
import random
from copy import deepcopy

app = Flask(__name__)

# Global Variables FOR THE API

USERLIST = []


# API Endpoint to Generate a Random Sequence of Numbers for the Memory Game
@app.post("/Generate_Sequence")
def generate_sequence():
    if request.is_json:
        # randmlist is ephemeral
        randomlist = []
        data = request.get_json()
        for i in range(0, int(data["difficulty"])):
            randomlist.append(random.randint(1, 101))
        return jsonify({"sequence": randomlist}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400


# API Endpoint to post the numbers of the USERLIST, get USERLIST and DELETE the USERLIST
@app.post("/User_list")
def post_user_list():
    if request.is_json:
        number = request.get_json()
        USERLIST.append(int(number["number"]))
        return jsonify({"message": "User number added successfully"}), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400


@app.get("/User_list")
def get_user_list():
    list_to_send = deepcopy(USERLIST)
    # Clear USERLIST for the next game
    USERLIST.clear()
    return jsonify({"userlist": list_to_send}), 200


@app.delete
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
