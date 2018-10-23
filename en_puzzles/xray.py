import sys # Credit to Reddit user /u/cpt_fwiffo
sys.path.append('..')
from en_map import rooms
from en_translation import translation
from en_items import *

class xray:

    def __init__(self):
        self.linked_rooms = [rooms["X-Ray Room"]]
        self.completed = False
        self.puzzle_one = False
        self.puzzle_part_one = False


    def puzzle_process(self, itemx, itemy, command, player, game):
        try:
            if command == translation["inspect"] and itemx == item_map:          
                print("You disloged a key and it has droped onto the floor.")# needs translating
                player.current_room["items"].append(item_xray_key)
                self.needed = False
        except:
            print("What are you trying to do?")# needs translating
        else:
            if command == translation["use"] and itemx == item_xray_key and item_xray_key in player.inventory:
                print("You have unlocked the cabinet.")# needs translating
                self.completed = True 
                player.current_room["complete"] = True 
                player.add_key(game)
                self.needed = False
                 # needs translating
