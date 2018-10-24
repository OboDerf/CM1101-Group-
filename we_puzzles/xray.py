import sys # Credit to Reddit user /u/cpt_fwiffo
sys.path.append('..')
from we_map import rooms
from we_translation import translation
from we_items import *

class xray:

    def __init__(self):
        self.linked_rooms = [rooms[translation["X-Ray Room"]]]
        self.completed = False
        self.puzzle_one = False
        self.puzzle_part_one = False


    def puzzle_process(self, itemx, itemy, command, player, game):
        self.needed = True
        try:
            if command == translation["inspect"] and itemx == item_map:          
                print("Mae'r goriad yn syrthio ar y llawr.")
                player.current_room["items"].append(item_xray_key)
                self.needed = False
        except:
            print("Beth ydych yn trio gwneud?")
        else:
            if command == translation["use"] and itemx == item_xray_key and item_xray_key in player.inventory and not self.completed:
                print("Rydych wedi agor yr cabinet.")
                self.completed = True 
                player.current_room["completed"] = True 
                player.add_key(game)
                self.needed = False
            elif self.needed:
                print("Dydy hyh heb unrhyw effaith")
                 
