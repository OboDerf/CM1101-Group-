## Imports
from gameparser import *
import sys

import en_map
import en_translation
import en_items
#import en_function
import we_map
import we_translation
import we_items
#import we_function

## Globals

#Globals are considered dirty, but that isn't going to stop me using them!
eng_lang = True
rooms = en_map.rooms
translation = en_translation.translation
items_combinations = en_items.items_combinations


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

def toggle_lang(player): # Does what it says on the tin. Takes the defined globals and toggles them between versions
    global eng_lang, rooms, translation
    if eng_lang:
        eng_lang = False
        rooms = we_map.rooms
        translation = we_translation.translation
        items_combinations = we_items.items_combinations
    else:
        eng_lang = True
        rooms = en_map.rooms
        translation = en_translation.translation
        items_combinations = en_items.items_combinations
    player.current_room = rooms[translation[player.current_room["name"]]]


def menu_start(game, player):
    while True:
        print(translation["main_menu_one"] + translation["difficulty"][game.difficulty] + translation["main_menu_two"])
        choice = normalise_str_input(input())
        if choice == '1': break
        elif choice == '2': toggle_lang(player)
        elif choice == '3': game.select_difficulty()
        elif choice == '0': return True
        else: print(translation["incorrect_answer"])
    return False


# -------------- MAIN GAME --------------
def room_print_items(items):
    if items:
        print(translation["room_print_items_one"])
        for a in items: print(" - " + a["name"] + translation["or"] + "'" + a["id"] + "'")
        print(translation["room_print_items_two"])
              

def room_print(current_room):
    print("\n" + translation["entry_message"] + current_room["name"] + "\n" + current_room["description"] + "\n")
    room_print_items(current_room["items"])


def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")
    

def menu_print(game, player):
    print(translation["command_message"])
    for direction in player.current_room["exits"]:
        print_exit(direction, exit_leads_to(player.current_room["exits"], direction))
        

def move(exits, direction):
    return rooms[exits[direction]]


def process_move(direction, player, game):
    if direction in player.current_room["exits"]:
        if move(player.current_room["exits"], direction) == rooms[translation["EXIT"]]:
            try_Exit(game, player)
        elif move(player.current_room["exits"], direction)["completed"]:
            print(translation["already_completed"])
        else: player.current_room = move(player.current_room["exits"], direction)
    else: print(translation["cannot_move"])
            

def print_inventory(player):
    if player.inventory:
        print(translation["player_print_inventory_one"])
        for a in player.inventory: print(" - " + a["name"] + translation["or"] + "'" + a["id"] + "'")
    else: print(translation["player_print_inventory_none"])
    

def print_keys(game, player): 
    print(translation["current_keys_one"] + str(player.current_keys) + translation["current_keys_two"])
    if player.current_keys >= game.difficulty_stats[game.difficulty]["keys_needed"]: print(translation["keys_full"])
    else: print(translation["keys_need_one"] + str(game.difficulty_stats[game.difficulty]["keys_needed"] - player.current_keys ) + translation["keys_need_two"])


def process_take(item, player):
    needed = True
    for a in player.current_room["items"]:
        if item in a["id"] and a["pick_up"]:
            needed = False
            player.inventory.append(a)
            player.current_room["items"].remove(a)
        elif item in a["id"] and not a["pick_up"]:
            print(translation["cannot_take"])
    if needed: print(translation["cannot_take_two"])


def process_drop(item, player):
    needed = True
    for a in player.inventory:
        if item in a["id"]:
            needed = False
            player.inventory.remove(a)
            player.current_room["items"].append(a)
    if needed: print(translation["cannot_drop"])


def process_inspect(item, player):
    needed = True
    for a in player.inventory:
        if item in a["id"]:
            needed = False
            print(a["description"])
    for b in player.current_room["items"]:
        if item in b["id"]:
            needed = False
            print(b["description"])
    if needed: print(translation["cannot_inspect"])


def process_move_item(item, player):
    needed = True
    for a in player.current_room["items"]:
        if item in a["id"] and a["move"] and not a ["moved"]:
            needed = False
            a["moved"] = True
            print(translation["moving_item"] + a["name"])
            break
        elif item in a["id"] and a["move"] and a ["moved"]:
            needed = False
            print(translation["item_already_moved"])
            break
        elif item in a["id"] and not a["move"]:
            needed = False
            print(translation["cannot_move_item"])
            break
    if needed: print(translation["cannot_find_move"])


def item_id_to_item(item_id, player):
    for a in player.inventory:
        if item_id == a["id"]: return a
    for b in player.current_room["items"]:
        if item_id == b["id"]: return b
    


def process_combine(itemx, itemy, player):
    needed = True
    if itemx != itemy and itemx in player.inventory and itemy in player.inventory:
        for a in items_combinations:
            if itemx in items_combinations[a]["components"] and itemy in items_combinations[a]["components"]:
                needed = False
                player.inventory.remove(itemx)
                player.inventory.remove(itemy)
                player.inventory.append(items_combinations[a]["output"])
                print(translation["combine_succ_one"] + itemx["name"] + translation["combine_succ_two"]+
                      itemy["name"] + translation["combine_succ_three"] + items_combinations[a]["output"]["name"])
        if needed: print(translation["combine_fail"])
    elif itemx == itemy: print(translation["combine_same"])
    elif itemy not in player.inventory or itemx not in player.inventory: print(translation["combine_no_item"])
    else: print(translation["combine_no_item"])
        

def process_use(itemx, itemy, player):
    if itemy == "none":
        pass ## SPEAK TO MARTON ABOUT HOW THIS BIT WILL WORK
    else:
        pass ## SAME STORY HERE
    

def menu_process(game, player):
    user_input = normalise_input(input("\n> "))
    if user_input:
        if user_input[0] == translation["help"]: print(translation["help_print"]) # Done
        elif user_input[0] == translation["inventory"]: print_inventory(player) # Done
        elif user_input[0] == translation["keys"]: print_keys(game, player) # Done
        elif len(user_input) > 1:  
            if user_input[0] == translation["go"]: process_move(user_input[1], player, game) # Done
            elif user_input[0] == translation["take"]: process_take(user_input[1], player) # Done
            elif user_input[0] == translation["drop"]: process_drop(user_input[1], player) # Done
            elif user_input[0] == translation["use"] and len(user_input) == 2: process_use(user_input[1], "none", player) 
            elif user_input[0] == translation["inspect"]: process_inspect(user_input[1], player) # Done
            elif user_input[0] == translation["move"]: process_move_item(user_input[1], player) # Done
            elif len(user_input) > 2:
                if user_input[0] == translation["combine"]:
                      process_combine(item_id_to_item(user_input[1], player),
                                      item_id_to_item(user_input[2], player), player) # Done
                elif user_input[0] == translation["use"]: process_use(user_input[1], user_input[2], player)
        else: print(translation["incorrect_answer"])
    else: print(translation["incorrect_answer"])

# needs to normalise it, parse it, try-except it
##    if userInput == "1": # help
##            print_help()
##    elif userInput == "2": # keys
##            print_keys(game, player)
##    elif userInput == "3": # up
##            print("go to a room up")
##    elif userInput == "4": # down
##            print("go to a room down")
##    elif userInput == "5" and player.current_room != corridors["west"]: # Go left and to the left is a corridor
##            player.current_room = corridors[player.current_room["left"]]
##            corridor_Menu(game, player)
##    elif userInput == "5": # go left and to the left is the exit
##            try_Exit(game, player)
##            corridor_Menu(game, player)
##    # check if user can go right
##    elif "right" in player.current_room and userInput == "6":
##            player.current_room = corridors[player.current_room["right"]]
##            corridor_Menu(game, player)
##
##
##def print_Corridor_Directions(currentRoom):
##    # Printing up
##    print("3 - " + translation["turnUp"] + currentRoom["up"]["name"]) # up is a room
##    # Printing down
##    print("4 - " + translation["turnDown"] + currentRoom["down"]["name"]) # down is a room
##
##    # Printing left
##    print("5 - " + translation["turnLeft"] + corridors[currentRoom["left"]]["name"]) # left is a room/exit
##
##    if "right" in currentRoom: # east corridor doesn't have a right corridor
##        # Printing right
##        print("6 - " + translation["turnRight"] + corridors[currentRoom["right"]]["name"]) # right is a corridor



def try_Exit(game, player):
    if player.current_keys >= game.difficulty_stats[game.difficulty]["keys_needed"]: did_User_Win(True, game)
    else: did_User_Win(False, game)


def did_User_Win(isWinner, game): # Made translation compatable and send back to main menu
    if isWinner:
        print(translation["game_won"])
        game.game_won = True
    else: print(translation["game_not_won"])


def main():
    while True:
    # When calling game and player, use the lowercase. Upper case is their pure versions, not what we work with
        game = Game() 
        player = Player(rooms[translation["Hospital Reception"]], game.difficulty_stats[game.difficulty]["attempts_max"])
        if menu_start(game, player): break
        while True:
            room_print(player.current_room)
            menu_print(game, player)
            command = menu_process(game, player)
            if game.game_won or game.game_lost:
                break
    

if __name__ == "__main__":
    main()
