import sys # Credit to Reddit user /u/cpt_fwiffo
sys.path.append('..')
from en_map import rooms
from en_translation import translation
from en_items import *


class doctors:

    def __init__(self):
        self.linked_rooms = [rooms["Doctors Lounge"]]
        self.completed = False
        self.needed = False

        self.white_sofa = False
        self.blue_sofa = False
        self.black_sofa = False

        self.puzzle_part_one = False
        self.puzzle_part_two = False


    def puzzle_process(self, itemx, itemy, command, player, game):
        try:
            self.needed = True
            if not self.puzzle_part_one:
                self.puzzle_one(itemx, player, command)
            if not self.puzzle_part_two and self.needed:
                self.puzzle_two(itemx, command)
            if self.puzzle_part_one and not self.completed and self.needed:
                self.puzzle_final(itemx, command, player, game)
            if self.needed: print("That had no effect")
        except TypeError:
            print("That had no effect.")
                    
    def puzzle_one(self, itemx, player, command):   
        if itemx in [item_blue_sofa, item_white_sofa, item_black_sofa, item_coffee_table] and itemx["moved"]:
            print("Moving the item revealed the floor beneath it!")
            
            if itemx == item_blue_sofa and not self.blue_sofa:
                print("there is a B scratched into the floor under the sofa")
                itemx["description"] += ", there is a B scratched into the floor under the sofa"
                self.blue_sofa = True
                self.needed = False

            if itemx == item_white_sofa and not self.white_sofa:
                print("there is a A scratched into the floor under the sofa")
                itemx["description"] += ", there is a A scratched into the floor under the sofa"
                self.white_sofa = True
                self.needed = False

            if itemx == item_black_sofa and not self.black_sofa:
                print("there is a D scratched into the floor under the sofa")
                itemx["description"] += ", there is a D scratched into the floor under the sofa"          
                self.black_sofa = True
                self.needed = False

            if itemx == item_coffee_table:
                print("there is nothing under the table")
                itemx["description"] += ", there is nothing under the table"
                self.needed = False
            
            if self.blue_sofa and self.white_sofa and self.black_sofa:
                self.puzzle_part_one = True
            

    def puzzle_two(self, itemx, command):
       if command == tranlsation["inspect"] and itemx == item_white_board:
            itemx["description"] += """
upon inspection the white board reveals
            6 = 6
            42 = 2A 
            B = 11
            F = 15
the rest of the board is illegible."""     
            self.puzzle_part_two = True
            self.needed = False
            

    def puzzle_final(self, user_input, command, player, game):
        if command == translation["input"] and user_input == "2989":
            print("You enter the code %s. The lock pops open.") % user_input
            self.completed = True 
            player.current_room["complete"] = True 
            player.add_key(game)
            self.needed = False
        elif command == translation["input"]:
            self.needed = False
            print("You enter the code %s. The lock doesn't open.") % user_input 
