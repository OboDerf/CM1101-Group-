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
translation = en_translation.translation


## Classes
#Classes. They're like dictionaries so cool and fancy that they have their own functions.
class Player:

    def __init__(self, starting_room, max_attempts):
        self.current_keys = 0 #player.current_keys
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
        a = normalise_str_input(input(translation["difficulty_change"]))
        if a in translation["difficulty"]: self.difficulty = translation["difficulty"].index(a)
        else:
            try:
                if int(a)-1 >= 0 and int(a) < len(translation["difficulty"]):
                        self.difficulty = translation["difficulty"][int(a)-1]
                else:
                        raise Exception
            except Exception:
                print(incorrect_answer)
                

## Main Code

def toggle_lang(): # Does what it says on the tin. Takes the defined globals and toggles them between versions
    global eng_lang, rooms, incorrect_answer
    if eng_lang:
        eng_lang = False
        rooms = we_map.rooms
        translation = en_translation.translation
    else:
        eng_lang = True
        rooms = en_map.rooms
        translation = we_translation.translation
    return rooms


def main_menu(game, player):
    while True:
        print(translation["main_menu_one"] + translation["difficulty"][game.difficulty] + translation["main_menu_two"])


        choice = normalise_str_input(input())
        if choice == '1': break
        elif choice == '2': rooms = toggle_lang()
        elif choice == '3': game.select_difficulty()
        elif choice == '0': sys.exit("DON'T EVER USE SYS.EXIT()")
        else: print(incorrect_answer)


def main():
    # When calling game and player, use the lowercase. Upper case is their pure versions, not what we work with
    game = Game() 
    player = Player(rooms["Hospital Reception"], game.difficulty_stats[game.difficulty]["attempts_max"])
    main_menu(game, player)
    while True:
        if game.game_won or game.game_lost:
            break
    

if __name__ == "__main__":
    main()
