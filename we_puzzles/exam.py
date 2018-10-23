import sys # Credit to Reddit user /u/cpt_fwiffo
sys.path.append('..')
from we_map import rooms
from we_translation import translation
from we_items import *
from random import randint


class exam:

    def __init__(self):
        self.linked_rooms = [rooms["Examination Room"]]
        self.completed = False
        self.needed = True
        self.chair_puzzle = False
        self.hammer_puzzle = False
        self.table_puzzle = False
        self.fluid_puzzle = False
      

    def puzzle_process(self, itemx, itemy, command, player, game):
        self.needed = True
        if not self.completed:
            if not self.chair_puzzle and self.needed:
                self.puzzle_one(itemx, game, command, player)
            if self.chair_puzzle and not self.hammer_puzzle and self.needed:
                self.puzzle_two(itemx, game, command, player)
            if not self.table_puzzle and self.needed:
                self.puzzle_three(itemx, game, command, player)
            if self.table_puzzle and not self.fluid_puzzle and self.needed:
                self.puzzle_four(itemx, game, command, player) 
            if self.fluid_puzzle and self.needed:
                self.puzzle_final(itemx, game, command, player)
            if self.needed:
                error = ["I don't know what you were trying to do... but it didn't work", # needs traslation
                         "hmmm..try something else",# needs traslation
                         "what was that?",# needs traslation
                         "What were you thinking"]# needs traslation
                print(error[randint(0,3)])
        else:
            print("Nothing to see here...")# needs traslation
        

    def puzzle_one(self, itemx, game, command, player):
        if itemx["id"] == "chair" and command == "inspect":
            print("""Inspecting the tools you notice that there is a bonesaw, hammer, and some kind of metal wedge... How can that be helpful?
                  """)# needs traslation
            player.current_room["items"].extend([item_hammer, item_saw, item_wedge])
            player.current_room["items"].remove(item_chair)
            self.chair_puzzle = True
            self.needed = False
            
    
    def puzzle_two(self, itemx, game, command, player):
        if itemx["id"] == "hammerwedge" and command == "use":
            print("Using your fancy new hammerwedge you attempt to pry and bash the locked drawer and...it opens! but wait is that a human head?")# needs traslation
            player.current_room["items"].append(item_head)
            self.hammer_puzzle = True
            self.needed = False

            
    def puzzle_three(self, itemx, game, command, player):
        if itemx["id"] == "table" and command == "inspect":
            print("Hmmm… at first glance the examination table looked clean but now you can see it’s coated in some weird liquid")# needs traslation
            item_table["pick_up"] = True
            self.table_puzzle  = True
            self.needed = False

            
    def puzzle_four(self, itemx, game, command, player):
        if itemx["id"] == "jar" and command == "use":
            if item_table in player.inventory:
                print("You struggle but manage so fill the jar with the strangely warm liquid from the chair")# needs traslation
                player.inventory.remove(item_jar)
                player.inventory.remove(item_table)
                player.inventory.append(item_full_jar)
                self.fluid_puzzle = True
                self.needed = False
            else:
                print("You can't do that...yet")# needs traslation
                self.needed = False            
        

    def puzzle_final(self, itemx, game, command, player):
        if command == "use" and itemx["id"] == "fluid": 
            self.completed = True 
            player.current_room["completed"] = True 
            print("You notice some of the top of the head melting so decide to pour all of it onto the head and look inside...It’s a vial!")# needs traslation
            player.inventory.remove(item_full_jar)
            player.add_key(game)
            player.current_room = rooms[translation["Hospital Reception"]]
            self.needed = False

