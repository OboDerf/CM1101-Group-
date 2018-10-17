## Imports
from gameparser import *
import sys

import en_map
#import en_items - in case these are ever created
#import en_function
import we_map
#import we_items
#import we_function

## Globals

#Globals are considered dirty, but that isn't going to stop me using them!
eng_lang = True
rooms = en_map.rooms
incorrect_answer = "\nPlease enter a valid answer\n"# For validation use 'incorrect_answer' as it's bilingual


## Classes
#Classes. They're like dictionaries so cool and fancy that they have their own functions.
class Player:

    def __init__(self, starting_room, max_attempts):
        self.current_keys = 0
        self.inventory = []
        self.current_room = starting_room
        self.attempts_left = max_attempts


class Game:

    def __init__(self):
        self.difficulty = 'medium' # This is setting all the default variables. I'm assuming medium until user says otherwise
        self.max_attempts = 60
        self.keys_max = 5
        self.keys_avaliable = 5
        self.keys_needed = 3
        self.game_lost = False
        self.game_won = False
        
    def difficulty_calc(self): # If the difficulty is 'e', 'm', 'h', or 'i' it edits the game settings
        # Note: I know there's a better way of doing this, but this is easy so bugger it
        if self.difficulty == 'easy' or self.difficulty == 'hawdd':
            self.max_attempts = 100
            self.keys_max = 6
            self.keys_avaliable = 6
            self.keys_needed = 2
        elif self.difficulty == 'medium' or self.difficulty == 'canolig':
            self.max_attempts = 80
            self.keys_max = 5
            self.keys_avaliable = 5
            self.keys_needed = 3
        elif self.difficulty == 'hard' or self.difficulty == 'caled':
            self.max_attempts = 60
            self.keys_max = 4
            self.keys_avaliable = 4
            self.keys_needed = 4
        elif self.difficulty == 'impossible' or self.difficulty == 'amhosibl':
            self.max_attempts = 50
            self.keys_max = 6
            self.keys_avaliable = 6
            self.keys_needed = 6
        else: print("If you ever see this, Kai's an idiot")

    def select_difficulty(self):
        if eng_lang:
            a = normalise_str_input(input("What difficulty would you like?\n - 1. Easy\n - 2. Medium\n - 3. Hard\n - 4. Impossible\n"))
            difficulties = ['easy', 'medium', 'hard', 'impossible']
            if a in difficulties: self.difficulty = a

            # Selecting the difficulty with a number in addition to typing
            try:
            	if int(a)-1 >= 0 and int(a) < len(difficulties):
            		self.difficulty = difficulties[int(a)-1]
            	else:
            		raise Exception
            except Exception:
            	print(incorrect_answer)

        else:
            a = normalise_str_input(input("Pa anhawster yr hoffech chi?\n - Hawdd\n - Canolig\n - Caled\n - Amhosibl\n")) 
            if a in ['hawdd', 'canolig', 'caled', 'amhosibl']: self.difficulty = a
            else: print(incorrect_answer)
        self.difficulty_calc()


## Main Code

def toggle_lang(): # Does what it says on the tin. Takes the defined globals and toggles them between versions
    global eng_lang, rooms, incorrect_answer
    if eng_lang:
        eng_lang = False
        rooms = we_map.rooms
        incorrect_answer = "\nRhowch ateb dilys.\n"
    else:
        eng_lang = True
        rooms = en_map.rooms
        incorrect_answer = "\nPlease enter a valid answer\n"
    return rooms


def main_menu(game, player):
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
            print("1. I paly Gêm")
            print("2. Toggle: English \ Cymraeg")
            print("3. I dewiswch anhawster (Ar hyn o bryd " + game.difficulty + ")")
            print("0. I ymadael\n")

        choice = normalise_str_input(input())
        if choice == '1': break
        elif choice == '2': rooms = toggle_lang()
        elif choice == '3': game.select_difficulty()
        elif choice == '0': sys.exit("DON'T EVER USE SYS.EXIT()")
        else: print(incorrect_answer)


def main():
    # When calling game and player, use the lowercase. Upper case is their pure versions, not what we work with
    game = Game() 
    player = Player(rooms["Reception"], game.max_attempts)
    main_menu(game, player)
    while True:
        if game.game_won or game.game_lost:
            break
    

if __name__ == "__main__":
    main()
