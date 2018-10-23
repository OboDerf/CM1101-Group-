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
#import en_items


class doctors:

    def __init__(self):
        self.linked_rooms = [rooms["Doctors Lounge"]]
        self.completed = False

        ## Any progress checks would go here EG:
        self.puzzle_part_one = False
        self.puzzle_part_two = False
        self.puzzle_final = False
        self.temp = False                                           

    def puzzle_process(self, itemx, itemy, command, player, game): # The more if statements here, the more parts to the puzzle there are
        #There will only be two functions that call puzzle_process: Use and Move.
        #If you want anything else, speak to me but be quick about it
        try:
            needed = True

            if not self.puzzle_part_one:
                needed = self.puzzle_one(itemx, player, command)
                
            if not self.puzzle_part_two and needed:
                # Every call after the first one check if needed. This will make sure we don't accidently send more error messages then needed
                needed = self.puzzle_two(itemx, command)

            if self.puzzle_part_one and self.puzzle_part_two and not self.completed and needed:
                needed = self.puzzle_final(itemx, itemy, player, game)
            # This prints only if none of the puzzles were completed
            if needed: print("That had no effect")
        except TypeError:
            print("That had no effect.")
                    
    #This puzzle is a move command puzzle. Once examplemove is moved, exampletwo is added to the room
    def puzzle_one(self, itemx, player, command):
        blue_sofa = False
        white_sofa = False
        black_sofa = False
        
        if (itemx["id"] == "bluesofa" or itemx["id"] == "whitesofa" or itemx["id"] == "blacksofa" or itemx["id"] == "coffeetable") and itemx["moved"]:
            
            #Saying the puzzle is now completed
            print("Moving the item revealed the floor beneath it!")
            
            if itemx["id"] == "bluesofa":
                print("there is a B scratched into the floor under the sofa")
                itemx["description"] += ", there is a B scratched into the floor under the sofa"
                blue_sofa = True

            if itemx["id"] == "whitesofa":
                print("there is a A scratched into the floor under the sofa")
                itemx["description"] += ", there is a A scratched into the floor under the sofa"
                white_sofa = True        

            if itemx["id"] == "blacksofa":
                print("there is a D scratched into the floor under the sofa")
                itemx["description"] += ", there is a D scratched into the floor under the sofa"          
                black_sofa = True  

            if itemx["id"] == "coffeetable":
                print("there is nothing under the table")
                itemx["description"] += ", there is nothing under the table"                              
            


            #Adding in any fluff with the action
            if blue_sofa == True and white_sofa == True and black_sofa == True:
                self.puzzle_part_one = True
            return False # The return is to see if the error message is needed
        else:
            return True

    def puzzle_two(self, itemx, command):
       """if command == "inspect" and itemx["id"] == "whiteboard":
            itemx["description"] += upon inspection the white board reveals
            6 = 6
            42 = 2A 
            B = 11
            F = 15
                    the rest of the board is illegible        
            self.puzzle_part_two = True
            return False
        else:
            return True"""

    def puzzle_final(self, itemx, itemy, player, game):
        if itemx["id"] == "examplecombined" and itemy["id"] == "exampletwo" and itemy in player.inventory and itemx in player.inventory:
            player.current_room["completed"] = True
            player.add_key(game)
            print("Wow, you completed the test room!")
            return False
        else:
            return True
"""player.current_room["completed"] = True
    player.add_key(game)"""