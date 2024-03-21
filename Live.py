#!/usr/bin/python3


from Utils import select
import GuessGame
import MemoryGame
import CurrencyRouletteGame





def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.')
    return name


def load_game():
    game = select("""Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to
        guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n
        Your Choice: """,3)

    difficulty = select("""Please choose game difficulty from 1 to 5: """, 5)

    if game == 1:
        print("Welcome to Memory Game")
        MemoryGame.play(difficulty)
    elif game == 2:
        print("Welcome to Guess Game")
        GuessGame.play(difficulty)
    elif game == 3:
        print('Welcome to Currency Routeltte')
        CurrencyRouletteGame.play(difficulty)



    return game,difficulty







