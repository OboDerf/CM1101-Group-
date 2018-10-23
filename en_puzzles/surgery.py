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

class surgery:

    def __init__(self):
        self.linked_rooms = [rooms["Surgery Room"]]
        self.completed = False

    def puzzle_process(self, itemx, itemy, command, player, game): # The more if statements here, the more parts to the puzzle there are

    	try:
    		if command == translation["inspect"] and itemx == item_patient:
    			# new item: needle +-> add it to user's inventory
    			print("You just received a needle!")
    		if command == translation["use"] and itemx == item_medicine and item_needle in player.current_room["items"]:
    			print()

    	except:
    		print("You can't do that!")

























   