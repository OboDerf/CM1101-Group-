import sys # Credit to Reddit user /u/cpt_fwiffo
sys.path.append('..')
from en_map import rooms
from en_translation import translation
from en_items import *


class pharmacy:

    def __init__(self):
        self.linked_rooms = [rooms[translation["Pharmacy"]]]
        self.completed = False
        self.needed = False


    def puzzle_process(self, itemx, itemy, command, player, game): 
        self.needed = True
        try:
            if itemx == item_scissors and itemy == item_bandaged_hammer and command == translation["use"]:
                player.inventory.remove(item_bandaged_hammer)
                player.inventory.append(item_bandages, item_hammer_head)
                print("A few cuts has freed the head from it's enprisonment.")# needs translating
                self.needed = False
            elif itemx == item_scissors and itemy == item_bandaged_cane and command == translation["use"]:
                player.inventory.remove(item_bandaged_cane)
                player.inventory.append(item_bandages, item_walking_cane)
                print("With the bandages removed, the cane's wounds are left to fester.")# needs translating
                self.needed = False
        except:
            print("What are you trying to cut?")# needs translating
        else:
            if command == translation["use"] and itemx == item_improvised_hammer and item_improvised_hammer in player.inventory:
                self.completed = True 
                player.current_room["complete"] = True 
                player.add_key(game)
                self.needed = False
                print("\nThe hammer holds and the box is broken.\n What lies inside may be the keys to salvation") # needs translating
            elif command == translation["use"] and itemx == item_make_shift_hammer and item_make_shift_hammer in player.inventory:
                self.completed = True 
                player.current_room["complete"] = True
                self.needed = False
                print("""
The swing at the box ends only in failour.
The hammer head launches, breaking a breaker vital to the alarm.
You dash out the room as the automatic security doors wake from their slumber.
The box, and with it a shred of hope, is lost to history.
""")# needs translating
            if needed and command != translation["inspect"]: print("This action has no effect") # needs translating
