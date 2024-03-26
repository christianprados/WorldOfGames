import os
from flask import Flask,abort
import Utils

app = Flask(__name__)

@app.route("/")
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
    #host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', '30000')
    app.run(port=int(port))