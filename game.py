## Imports
from gameparser import *
from random import random
import functions

import en_map
import en_translation
import en_items
import we_map
import we_translation
import we_items

## Globals

#Globals are considered dirty, but that isn't going to stop me using them!
eng_lang = True
rooms = en_map.rooms
translation = en_translation.translation
items_combinations = en_items.items_combinations
puzzles = functions.en_puzzles


## Classes
#Classes. They're like dictionaries so cool and fancy that they have their own functions.
class Player:

    def __init__(self, starting_room, max_attempts):
        self.current_keys = 0 #player.current_keys
        self.rooms_rewarded = 0
        self.inventory = []
        self.current_room = starting_room
        self.attempts_left = max_attempts

    def add_key(self, game):
        if game.difficulty_stats[game.difficulty]["keys_avaliable"]/(6 - self.rooms_rewarded) >= random():
            game.difficulty_stats[game.difficulty]["keys_avaliable"] -= 1
            self.rooms_rewarded += 1
            self.current_keys +=1
            print(translation["key_gained"])
        else:
            self.rooms_rewarded += 1
            print(translation["key_not_gained"])
            
        

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
                if int(a)-1 >= 0 and int(a)-1 < len(translation["difficulty"]):
                        self.difficulty = int(a)-1
                else:
                        raise Exception
            except Exception:
                print(translation["incorrect_answer"])

    def turn_ticker(self):
        self.difficulty_stats[self.difficulty]["attempts_max"] -= 1
        if self.difficulty_stats[self.difficulty]["attempts_max"] == 0:
            self.game_lost = True
            print(translation["game_lost"])
                

## Main Code

def toggle_lang(player): # Does what it says on the tin. Takes the defined globals and toggles them between versions
    global eng_lang, rooms, translation, puzzles
    if eng_lang:
        eng_lang = False
        rooms = we_map.rooms
        translation = we_translation.translation
        items_combinations = we_items.items_combinations
        puzzles = functions.we_puzzles
    else:
        eng_lang = True
        rooms = en_map.rooms
        translation = en_translation.translation
        items_combinations = en_items.items_combinations
        puzzles = functions.en_puzzles
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
        print(translation["room_print_items"] + translation["take"].upper() + " + " + items[0]["id"])
        for a in items: print(" - " + a["id"] + ", " + a["name"] + " - " + a["description"])
        print()

def room_print(current_room):
    print("\n" + translation["entry_message"] + current_room["name"] + "\n\n"
          + current_room["description"] + "\n--------------------\n")
    room_print_items(current_room["items"])


def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    print("- " + translation["exit_one"] + direction.upper() + translation["exit_two"] + leads_to + ".")
    

def menu_print(game, player):
    print(translation["directions_available"])
    for direction in player.current_room["exits"]:
        print_exit(direction, exit_leads_to(player.current_room["exits"], direction))
    print(translation["command_message"])
        

def move(exits, direction):
    return rooms[exits[direction]]


def process_move(direction, player, game):
    if direction in player.current_room["exits"]:
        if move(player.current_room["exits"], direction) == rooms[translation["EXIT"]]:
            try_Exit(game, player)
        elif move(player.current_room["exits"], direction)["completed"]:
            print(translation["already_completed"])
        else:
            # drop all item if players goes back to corridor
            playerGoingToRoom = player.current_room["exits"][direction]
            if playerGoingToRoom == "Hospital Reception" or playerGoingToRoom == "Hallway" or playerGoingToRoom == "Hallway":
                print("We are dropping all the items here")
                drop_all_items(player)
            player.current_room = move(player.current_room["exits"], direction)
    else: print(translation["cannot_move"])
            

def drop_all_items(player):
    player.current_room["items"] += player.inventory
    del player.inventory[:]

def print_inventory(player):
    if player.inventory:
        print(translation["player_print_inventory_one"])
        for a in player.inventory:  print(" - " + a["id"] + ", " + a["name"])
    else: print(translation["player_print_inventory_none"])
    

def print_keys(game, player): 
    print(translation["current_keys_one"] + str(player.current_keys) + translation["current_keys_two"])
    if player.current_keys >= game.difficulty_stats[game.difficulty]["keys_needed"]: print(translation["keys_full"])
    else: print(translation["keys_need_one"] + str(game.difficulty_stats[game.difficulty]["keys_needed"] - player.current_keys ) + translation["keys_need_two"])


def process_take(item, player):
    needed = True
    for a in player.current_room["items"]:
        if item in a["id"] and a["pick_up"]:
            if game.difficulty != 3: game.turn_ticker()
            needed = False
            player.inventory.append(a)
            player.current_room["items"].remove(a)
        elif item in a["id"] and not a["pick_up"]:
            print(translation["cannot_take"])
    if needed: print(translation["cannot_take_two"])


def process_drop(item, player, game):
    needed = True
    for a in player.inventory:
        if item in a["id"]:
            if game.difficulty != 3: game.turn_ticker()
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


def process_move_item(item, player, game):
    needed = True
    for a in player.current_room["items"]:
        if item in a["id"] and a["move"] and not a ["moved"]:
            if game.difficulty != 3: game.turn_ticker()
            needed = False
            a["moved"] = True
            print(translation["moving_item"] + a["name"])
            puzzles[player.current_room["puzzle"]].puzzle_process(item_id_to_item(item, player), "none", translation["move"], player, game)
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
    

def process_combine(itemx, itemy, player, game):
    needed = True
    if itemx != itemy and itemx in player.inventory and itemy in player.inventory:
        for a in items_combinations:
            if itemx in items_combinations[a]["components"] and itemy in items_combinations[a]["components"]:
                if game.difficulty != 3: game.turn_ticker()
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
        

def process_use(itemx, itemy, player, game):
    if game.difficulty != 3: game.turn_ticker()
    itemx = item_id_to_item(itemx, player)
    if itemy != "none":
        itemy = item_id_to_item(itemy, player)
    puzzles[player.current_room["puzzle"]].puzzle_process(itemx, itemy, translation["use"], player, game)
    

def print_turns(game):
    print(translation["turns_one"] + str(game.difficulty_stats[game.difficulty]["attempts_max"]) + translation["turns_two"])


def menu_process(game, player):
    user_input = normalise_input(input("\n> "))
    #print("--------------------")
    if user_input:
        if user_input[0] == translation["help"]: print(translation["help_print"]) 
        elif user_input[0] == translation["inventory"]: print_inventory(player) 
        elif user_input[0] == translation["keys"]: print_keys(game, player)
        elif user_input[0] == translation["turns"]: print_turns(game)
        elif len(user_input) > 1:
            if game.difficulty == 3: game.turn_ticker()
            if user_input[0] == translation["go"]: process_move(user_input[1], player, game) 
            elif user_input[0] == translation["take"]: process_take(user_input[1], player, game) 
            elif user_input[0] == translation["drop"]: process_drop(user_input[1], player, game) 
            elif user_input[0] == translation["use"] and len(user_input) == 2: process_use(user_input[1], "none", player, game) 
            elif user_input[0] == translation["inspect"]: process_inspect(user_input[1], player) 
            elif user_input[0] == translation["move"]: process_move_item(user_input[1], player, game) 
            elif len(user_input) > 2:
                if user_input[0] == translation["combine"]:
                      process_combine(item_id_to_item(user_input[1], player),
                                      item_id_to_item(user_input[2], player), player, game) 
                elif user_input[0] == translation["use"]: process_use(user_input[1], user_input[2], player, game)
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
