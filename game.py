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
	print()
	print(translation["corridor_Entry_Message"] + player.current_room["name"])

	# Print the commands
	# 1 - Help
	print(translation["helpCommand"])
	# 2 - Keys
	print(translation["keysCommand"])
	# 3... - Left/Right/Exit/Enter Aroom
	print_Corridor_Directions(player.current_room)
	userInput = input("< ")
	# needs to normalise it, parse it, try-except it
	if userInput == "1": # help
		print_help(player.current_room)
		corridor_Menu(game, player)
	elif userInput == "2": # keys
		print_keys(game,player)
		corridor_Menu(game,player)
	elif userInput == "3": # up
		print("go to a room up")
	elif userInput == "4": # down
		print("go to a room down")
	elif userInput == "5" and player.current_room != corridors["west"]: # Go left and to the left is a corridor
		player.current_room = corridors[player.current_room["left"]]
		corridor_Menu(game, player)
	elif userInput == "5": # go left and to the left is the exit
		try_Exit(game, player)
		corridor_Menu(game, player)

	# check if user can go right
	elif "right" in player.current_room and userInput == "6":
		player.current_room = corridors[player.current_room["right"]]
		corridor_Menu(game, player)


def room_Menu(game, player):
	print()
	


def print_Corridor_Directions(currentRoom):
	# Printing up
	print("3 - " + translation["turnUp"] + currentRoom["up"]["name"]) # up is a room
	# Printing down
	print("4 - " + translation["turnDown"] + currentRoom["down"]["name"]) # down is a room

	# Printing left
	print("5 - " + translation["turnLeft"] + corridors[currentRoom["left"]]["name"]) # left is a room/exit

	if "right" in currentRoom: # east corridor doesn't have a right corridor
		# Printing right
		print("6 - " + translation["turnRight"] + corridors[currentRoom["right"]]["name"]) # right is a corridor



def move_From_Corridor_To_Room():
	print("")


def try_Exit(game, player):
	if player.current_keys >= game.difficulty_stats[game.difficulty]["keys_needed"]:
		did_User_Win(True)
	else:
		did_User_Win(False)



def did_User_Win(isWinner):
	if isWinner:
		print("Good job you won! game is over!")
		# maybe show the main menu instead of quitting the game just make sure to reset the variables
		sys.exit()
		# Good job you won
		# needs to reset the game variables such as keys and get back to main menu
	else:
		print("Sorry you don't have enough keys yet")
		# Sorry, you lost
		# send user back to west side of corridor

def print_help(currentRoom):
	# we need to print some help based on what room the user is in, needs to be translated
	if currentRoom in corridors.values():
		print("trying to help: You're in a corridor!")
	else:
		print("trying to help: You are not in a corridor, in a room maybe?")


def print_keys(game, player):
	# needs to be translated
	playerKeys = player.current_keys # the number of keys the user has at the moment
	neededKeys = game.difficulty_stats[game.difficulty]["keys_needed"] # the number of keys the user still needs to collect

	print("You currently have " + str(playerKeys) + " keys")
	if playerKeys >= neededKeys:
		print("Congrats! You found all the keys. You can exit the game")
	else:
		print("You still need to find " + str(neededKeys- playerKeys ) + " keys to win")


def main():
    # When calling game and player, use the lowercase. Upper case is their pure versions, not what we work with
    game = Game() 
    player = Player(corridors["west"], game.difficulty_stats[game.difficulty]["attempts_max"])
    main_menu(game, player)
    while True:
        if game.game_won or game.game_lost:
            break
    

if __name__ == "__main__":
    main()
