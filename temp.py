eng_lang = True
incorrect_answer = "\nPlease enter a valid answer\n"

class Game:

    def __init__(self):
        self.difficulty = 'm' # This is setting all the default variables.I'm assuming medium until user says otherwise
        self.difficulty_stats = {
                "e" : {
                    'attempts_max': 100,
                    'keys_max': 6,
                    'keys_avaliable': 6,
                    'keys_needed': 2},
                "m" : {
                    'attempts_max': 80,
                    'keys_max': 5,
                    'keys_avaliable': 5,
                    'keys_needed': 3},
                
                "h" : {
                    'attempts_max': 60,
                    'keys_max': 4,
                    'keys_avaliable': 4,
                    'keys_needed': 4},

                "i" : {
                    'attempts_max': 50,
                    'keys_max': 6,
                    'keys_avaliable': 6,
                    'keys_needed': 6}        
            }
        self.game_lost = False
        self.game_won = False

    def select_difficulty(self):
        if eng_lang:
            a = (input("What difficulty would you like?\n - Easy\n - Medium\n - Hard\n - Impossible\n")) 
            if a in ['easy', 'medium', 'hard', 'impossible']: self.difficulty = a
            else: print(incorrect_answer)
        else:
            a = (input("Pa anhawster yr hoffech chi?\n - Hawdd\n - Canolig\n - Caled\n - Amhosibl\n")) 
            if a in ['hawdd', 'canolig', 'caled', 'amhosibl']: self.difficulty = a
            else: print(incorrect_answer)

def toggle_lang(): # Does what it says on the tin. Takes the defined globals and toggles them between versions
    global eng_lang, incorrect_answer
    if eng_lang:
        eng_lang = False
        incorrect_answer = "\nRhowch ateb dilys.\n"
    else:
        eng_lang = True
        incorrect_answer = "\nPlease enter a valid answer\n"

def main_menu(game):
    while True:
        if eng_lang:
            print("----------")
            print("TEMP MENU")
            print("----------\n")
            print("Enter _ to:\n")
            print("1. To play game")
            print("2. Toggle: English \ Cymraeg")
            print("3. To pick difficulty (Currently " + game.difficulty + ")")
            print("0. To exit\n")
        else:
            print("----------")
            print("TEMP DDEWISLEN")
            print("----------\n")
            print("Nodwch _ i:\n")
            print("1. I chwarae Gêm")
            print("2. Toggle: English \ Cymraeg")
            print("3. I ddewis anhawster (Ar hyn o bryd " + game.difficulty + ")")
            print("0. I ymadael\n")

        choice = (input())
        if choice == '1': break
        elif choice == '2': toggle_lang()
        elif choice == '3': game.select_difficulty()
        elif choice == '0': break
        else: print(incorrect_answer)

game = Game()
main_menu(game)

