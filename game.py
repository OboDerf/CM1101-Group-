## Imports
from gameparser import *
import sys

import en_map
import en_translation
#import en_items - in case these are ever created
#import en_function
import we_map
import we_translation
#import we_items
#import we_function

## Globals

#Globals are considered dirty, but that isn't going to stop me using them!
eng_lang = True
rooms = en_map.rooms
translation = en_translation


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
        self.difficulty = 1 # This is setting all the default variables.I'm assuming medium until user says otherwise
        self.difficulty_stats = {
                0 : {
                    'attempts_max': 100,
                    'keys_max': 6,
                    'keys_avaliable': 6,
                    'keys_needed': 2},
                1 : {
                    'attempts_max': 80,
                    'keys_max': 5,
                    'keys_avaliable': 5,
                    'keys_needed': 3},
                
                2 : {
                    'attempts_max': 60,
                    'keys_max': 4,
                    'keys_avaliable': 4,
                    'keys_needed': 4},

                3 : {
                    'attempts_max': 50,
                    'keys_max': 6,
                    'keys_avaliable': 6,
                    'keys_needed': 6}        
            }
        self.game_lost = False
        self.game_won = False
        
    def select_difficulty(self):
        a = normalise_str_input(input("What difficulty would you like?\n - Easy\n - Medium\n - Hard\n - Impossible\n")) 
        if a in ['easy', 'medium', 'hard', 'impossible']: self.difficulty = a
        else: print(translation["incorrect_answer"])
        self.difficulty_calc()


## Main Code

def toggle_lang(): # Does what it says on the tin. Takes the defined globals and toggles them between versions
    global eng_lang, rooms, incorrect_answer, tranlation
    if eng_lang:
        eng_lang = False
        rooms = we_map.rooms
        translation = we_translation
    else:
        eng_lang = True
        rooms = en_map.rooms
        translation = en_translation
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
            print("1. I chwarae Gêm")
            print("2. Toggle: English \ Cymraeg")
            print("3. I ddewis anhawster (Ar hyn o bryd " + game.difficulty + ")")
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
