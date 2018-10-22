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
from en_items import *
from en_map import rooms
from en_translation import translation


class patients:

    def __init__(self):
        self.linked_rooms = [rooms["Patients Room"]]
        self.completed = False
        self.needed = True

        ## Any progress checks would go here EG:
        self.puzzle_inspect = False
        self.puzzle_book1= False
        self.puzzle_book2 = False
        self.puzzle_book3 = False
        self.puzzle_lamphit = False

        self.attempts = 2

    #2431
        

    def puzzle_process(self, itemx, itemy, command, player, game): # The more if statements here, the more parts to the puzzle there are
        self.needed = True
        if not self.puzzle_inspect:
            self.puzzle_one(itemx, command, player)
        if self.puzzle_inspect and self.attempts > 0 and self.needed:
            if not self.puzzle_book1 and self.needed:
                self.puzzle_two(itemx, command, player)
            if not self.puzzle_book2 and self.puzzle_book1 and self.needed:
                self.puzzle_three(itemx, command, player)
            if not self.puzzle_book3 and self.puzzle_book2 and self.needed:
                self.puzzle_four(itemx, command, player)
            if not self.completed and self.puzzle_book3 and self.needed:
                self.puzzle_final(itemx, game, command, player)
        elif self.puzzle_inspect and self.attempts <= 0 and  not self.completed:
            self.error_safe (itemx, game, command, player)
        if self.needed: print("'Naut happened")
            
        


    def error_safe(self, itemx, game, command, player):
        if item_lamp in player.inventory and command == "use" and  itemx == item_lamp:
            print ("You knock the charging person unconscious!")
            self.needed = False
            self.completed = True 
            player.current_room["completed"] = True
            player.add_key(game)
        else:
            print("You run out of the room, it locks behind you.")
            self.completed = True
            player.current_room["completed"] = True
            player.current_room = rooms[translation["Hallway"]]
            

    def puzzle_one(self, itemx, command, player):
        if command == "inspect" and itemx["id"] == "bookshelf": # How do they complete the task? 
            player.current_room["items"].extend([item_book_1, item_book_2, item_book_3, item_book_4])
            player.current_room["items"].remove(item_bookshelf)
            self.needed = False
            self.puzzle_inspect = True 
        else:
            self.needed = False
            print("That had no effect") 

    def puzzle_two(self, itemx, command, player):
        if (command == "inspect" or command == "use") and itemx["id"] == "book2":
            self.needed = False
            self.puzzle_book1 = True
            print ("You read the second book, the woman in the corner raises her head from her hands.")
        else:
            self.needed = False
            self.attempts -=  1
            if self.attempts == 1:            
                print("The woman looks directly at you, she does not look happy.")
            elif self.attempts == 0:
                print("The woman charges in your direction! You:")

    def puzzle_three(self, itemx, command, player):
        if (command == "inspect" or command == "use") and itemx["id"] == "book4":
            self.needed = False
            self.puzzle_book2 = True
            print ("You read the fourth book, the woman stands up and faces you. A slight smile on her face")
        else:
            self.needed = False
            self.puzzle_book1 = False
            self.attempts -=  1
            if self.attempts == 1:            
                print("The woman looks directly at you, she does not look happy.")
            elif self.attempts == 0:
                print("The woman charges in your direction! You:")

    def puzzle_four(self, itemx, command, player):
        if (command == "inspect" or command == "use") and itemx["id"] == "book3":
            self.needed = False
            self.puzzle_book3 = True
            print ("You read the third book, the woman lays in her bed")
        else:
            self.needed = False
            self.puzzle_book1 = False
            self.puzzle_book2 = False
            self.attempts -=  1
            if self.attempts == 1:            
                print("The woman looks directly at you, she does not look happy.")
            elif self.attempts == 0:
                print("The woman charges in your direction! You:")
        
    
    def puzzle_final(self, itemx, game, command, player):
        if (command == "use" or command == "inspect") and itemx["id"] == "book1":
            print ("You read the first book, the woman takes off her necklace and places it on her bedside table. It has a vile on it!")
            self.needed = False
            self.completed = True 
            player.current_room["completed"] = True # This tells the rooms it's completed
            
            player.add_key(game) # Finally, this adds the key
            return False 
