##   Key:
##
## - self: This means you're using a variable or function defined within the class. It's an easy way of carrying 
##         variables over for when you're feeling lazy. Add new variables to __init__ and new functions wherever you want
##
## - itemx: So this will always be an item directly from the item file. You need to check it's location (in room vs
##          in inventory) before you can use it. 
##
## - itemy: This will only contain a variable on 'use <itemx> <itemy>'. Otherwise calling it will return an error that's
##          try excepted' all the way over in game.py. Use this only for item on item though
##
## - player: Player is a class defined in game.py. It has the current room, inventory, and all that good stuff in.
##           player.current_room is the current room
##           player.inventory is the inventory
##
## - game: This mostly holds stats and shouldn't be needed outside of puzzle_final's player.add_key(game)
##
##   Common Functions:
##
## - itemx in player.inventory: checks if the item is in the player's inventory
##
## - itemx in player.current_room["items"]: checks if the item is in the room's floor
##
## - itemx["moved"]: Checks if the item has been moved
##
## - itemx["id"] == "example": Checks if the player's inputed item is what you're looking for
##
## - translation["<Command name>"] == command: checks if the player has entered this command. Useful to make sure they're 'using' or 'moving' or whatever
##
## - NOTE: Combining is handled elsewhere. If the puzzle requires a combined item, look for it's ID
##
## - You can always make more def var() functions or self.var = <> statements. What's provided is a framework. 
##
## - When a change is made and you're calling it, please also update the welsh version (Just override until it's finished though)
##
## - If there's anything I've missed, do ask.
##
## - If you're going to add in more rooms to your puzzle, ask me how to do it (Or try it yourself, who am I to tell you what to do?)
##
import sys # Credit to Reddit user /u/cpt_fwiffo
sys.path.append('..')
from en_map import rooms
from en_translation import translation
from en_items import *


class exam:

    def __init__(self):
        self.linked_rooms = [rooms["Examination Room"]]
        self.completed = False
        self.needed = True

        ## Any MANDATORY progress checks would go here EG:
        self.chair_puzzle = False
        self.hammer_puzzle = False
        self.table_puzzle = False
        self.fluid_puzzle = False

        self.temp = False

        

    def puzzle_process(self, itemx, itemy, command, player, game): 
        if not self.completed:
            if not self.chair_puzzle:
                self.puzzle_one(itemx, game, command, player)
            if self.chair_puzzle and not self.hammer_puzzle:
                self.puzzle_two(itemx, game, command, player)
            if not self.table_puzzle:
                self.puzzle_three(itemx, game, command, player)
            if self.table_puzzle and not self.fluid_puzzle:
                self.puzzle_four(itemx, game, command, player) 
            if self.fluid_puzzle:
                self.puzzle_final(itemx, game, command, player)
        else:
            print("Nothing to see here...")
        

    def puzzle_one(self, itemx, game, command, player):
        if itemx["id"] == "chair" and command == "inspect": # How do they complete the task? 
            print("""Inspecting the tools you notice that there is a bonesaw, hammer, some kind of metal wedge and a spanner...How can that be helpful?
                  """)
            player.current_room["items"].extend([item_hammer, item_saw, item_wedge])
            player.current_room["items"].remove(item_chair)
            self.chair_puzzle = True 
        else:
            print("I don't know what you were trying to do... but it didn't work")
            
    
    def puzzle_two(self, itemx, game, command, player):
        if itemx["id"] == "hammerwedge" and command == "use":
            print("Using your fancy new hammerwedge you attempt to pry and bash the locked drawer and...it opens! but wait is that a human head?")
            player.current_room["items"].append(item_head)
            self.hammer_puzzle = True
        else:
            print("hmmm..try something else")
            
    def puzzle_three(self, itemx, game, command, player):
        if itemx["id"] == "table" and command == "inspect":
            print("Hmmm… at first glance the examination table looked clean but now you can see it’s coated in some weird liquid")
            item_table["pick_up"] = True
            self.table_puzzle  = True
        else:
            print("what was that?")
            
    def puzzle_four(self, itemx, game, command, player):
        if itemx["id"] == "jar" and command == "use":
            if item_table in player.inventory:
                print("You struggle but manage so fill the jar with the strangely warm liquid from the chair")
                player.inventory.remove(item_jar)
                player.inventory.remove(item_table)
                player.inventory.append(item_full_jar)
                self.fluid_puzzle = True
            else:
                print("You can't do that...yet")
        else:
            print("What were you thinking")
            
        

    def puzzle_final(self, itemx, game, command, player):# This is the final part of the puzzle. After this the player will be awarded a key.
        if command == "use" and itemx["id"] == "fluid": # Another example of what a room condition looks like
            self.completed = True # These are all important. One tells the puzzle that it's completed
            player.current_room["completed"] = True # This tells the rooms it's completed
            print("You notice some of the top of the head melting so decide to pour all of it onto the head and look inside...It’s a key!")
            player.inventory.remove(item_full_jar)
            player.add_key(game) # Finally, this adds the key
            player.current_room = rooms[translation["Hospital Reception"]]
            return False
