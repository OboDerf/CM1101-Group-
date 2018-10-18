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
corridors = en_map.corridors
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
        self.corridorSide = "west"
        

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
                print(translation["incorrect_answer"])
                

## Main Code

def toggle_lang(): # Does what it says on the tin. Takes the defined globals and toggles them between versions
    global eng_lang, rooms, translation
    if eng_lang:
        eng_lang = False
        rooms = we_map.rooms
        translation = we_translation.translation
    else:
        eng_lang = True
        rooms = en_map.rooms
        translation = en_translation.translation


def main_menu(game, player):
    while True:
        print(translation["main_menu_one"] + translation["difficulty"][game.difficulty] + translation["main_menu_two"])
        choice = normalise_str_input(input())
        if choice == '1':
        	corridor_Menu(game, player)
        	break
        elif choice == '2': toggle_lang()
        elif choice == '3': game.select_difficulty()
        elif choice == '0': sys.exit("DON'T EVER USE SYS.EXIT()")
        else: print(incorrect_answer)


# -------------- MAIN GAME --------------
# Controls the corridor
def corridor_Menu(game, player):
	# Prints the side of the corridor the user is in at the moment (west, center, east)
	print();print()
	print(translation["corridor_Entry_Message"] + corridors[game.corridorSide]["name"])

	# Print the commands
	# 1 - Help
	print(translation["helpCommand"])
	# 2 - Keys
	print(translation["keysCommand"])
	# 3... - Left/Right/Exit/Enter Aroom
	print_Corridor_Directions(game.corridorSide)

	


def print_Corridor_Directions(currentCorridorSide):
	currentCorridorDict = corridors[currentCorridorSide]

	# Printing up
	print("1. " + translation["turnUp"] + currentCorridorDict["up"]["name"]) # up is a room
	# Printing down
	print("2. " + translation["turnDown"] + currentCorridorDict["down"]["name"]) # down is a room

	# Printing left
	print("3. " + translation["turnLeft"] + corridors[currentCorridorDict["left"]]["name"]) # left is a room/exit

	if "right" in currentCorridorDict: # east corridor doesn't have a right corridor
		# Printing right
		print("4. " + translation["turnRight"] + corridors[currentCorridorDict["right"]]["name"]) # right is a corridor



def move_From_Corridor_To_Room():
	print("")


def try_Exit(game, player):
	if player.current_keys >= difficulty_stats[difficulty]:
		didUserWin(True)
	else:
		didUserWin(False)



def did_User_Win(isWinner):
	if isWinner:
		print()
		# Good job you won
		# needs to reset the game variables such as keys and get back to main menu
	else:
		print()
		# Sorry, you lost
		# send user back to west side of corridor




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
