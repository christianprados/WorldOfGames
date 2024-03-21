import os
#Global Variables used in the game

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 400

#Function that clears the screen
def Screen_cleaner():
    os.system('cls')

#Validates the user input. If it is not an integer try again
def input_with_validation_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except:
            print('Please try again')
            continue

#Validates the user input. If it is not an float try again
def input_with_validation_float(message):
    while True:
        try:
            number = float(input(message))
            return number
        except:
            print('Please try again')
            continue

#Validates the user input for yes or no.
def input_with_validation_yes_no(message):
    while True:
        try:
            choice = input(message)
            if choice == 'yes' or choice == 'no':
                return choice
            else:
                print('Please try again')
                continue
        except:
            print('Please try again')
            continue

#This is a selection function with two inputs: A message for the user and how many options can be selected
def select(message,options):
    while True:
        selection = input_with_validation_integer(message)
        if selection <= options:
            break
        else:
            print("Invalid Choice, try again")
            continue
    return selection
