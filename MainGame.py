#!/usr/bin/python3

from Live import load_game, welcome
from Utils import input_with_validation_yes_no, Screen_cleaner
import time


welcome("""Christian Prados""")
while True:
    load_game()
    time.sleep(3)
    play = input_with_validation_yes_no("Would you like to play again (yes/no):")
    if play == 'yes':
        Screen_cleaner()
        continue
    else:
        break











