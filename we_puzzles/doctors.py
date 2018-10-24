import sys # Credit to Reddit user /u/cpt_fwiffo
sys.path.append('..')
from we_map import rooms
from we_translation import translation
from we_items import *


class doctors:

    def __init__(self):
        self.linked_rooms = [rooms[translation["Doctors Lounge"]]]
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
            if self.needed: print("Doedd gan hyn dim effaith") 
        except TypeError:
            print("Doedd gan hyn dim effaith.") 
                    
    def puzzle_one(self, itemx, player, command):   
        if itemx in [item_blue_sofa, item_white_sofa, item_black_sofa, item_coffee_table] and itemx["moved"]:
            print("Gwnaeth symyd yr eitem yma, dangos yr llawr odano!") 
            
            if itemx == item_blue_sofa and not self.blue_sofa:
                print("Mae yna B wedi cael ei crafu mewn i'r llawr odan y soffa")
                itemx["description"] += ", mae yna B wedi cael ei crafu mewn i'r llawr odan y soffa."
                self.blue_sofa = True
                self.needed = False

            if itemx == item_white_sofa and not self.white_sofa:
                print("Mae yna A wedi cael ei crafu mewn i'r llawr odan y soffa")
                itemx["description"] += ", mae yna A wedi cael ei crafu mewn i'r llawr odan y soffa." 
                self.white_sofa = True
                self.needed = False

            if itemx == item_black_sofa and not self.black_sofa:
                print("Mae yna D wedi cael ei crafu mewn i'r llawr odan y soffa") 
                itemx["description"] += ", mae yna D wedi cael ei crafu mewn i'r llawr odan y soffa."         
                self.black_sofa = True
                self.needed = False

            if itemx == item_coffee_table:
                print("does dim byd odan y bwrdd yma")
                itemx["description"] += ", does dim byd odan y bwrdd yma"
                self.needed = False
            
            if self.blue_sofa and self.white_sofa and self.black_sofa:
                self.puzzle_part_one = True
            

    def puzzle_two(self, itemx, command):
       if command == tranlsation["inspect"] and itemx == item_white_board:
            itemx["description"] += """
Ar ol archwilio'r bwrdd gwyn, gwelwyd:
            6 = 6
            42 = 2A 
            B = 11
            F = 15
Mae gweddill yr bwrdd gwyn yn annarllenadwy."""
            self.puzzle_part_two = True
            self.needed = False
            

    def puzzle_final(self, user_input, command, player, game):
        if command == translation["input"] and user_input == "2989":
            print("Rydch yn mewnbynnu'r cod %s. Mae'r clo yn agor.") % user_input
            self.completed = True 
            player.current_room["complete"] = True 
            player.add_key(game)
            self.needed = False
        elif command == translation["input"]:
            self.needed = False
            print("Rydch yn mewnbynnu'r cod %s. Nad ydy'r clo yn agor.") % user_input
