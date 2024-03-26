
import Utils


# Function to add the score to the score file

def add_score(difficulty):
    try:
        with open(Utils.SCORES_FILE_NAME, 'r+', encoding='utf-8' ) as file:
            #calculates the earned points
            POINTS_OF_WINNING = (difficulty * 3) + 5
            new_score = int(file.read()) + POINTS_OF_WINNING
            file.seek(0)
            file.write(str(new_score))
    #if the file does not exist it will create the file with w+
    except Exception as error:
        print('error reading file', error)
        with open(Utils.SCORES_FILE_NAME, 'w+', encoding='utf-8') as file:
            # calculates the earned points
            POINTS_OF_WINNING = (difficulty * 3) + 5
            new_score = POINTS_OF_WINNING
            file.write(str(new_score))





