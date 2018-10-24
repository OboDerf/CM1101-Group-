import sys # Credit to Reddit user /u/cpt_fwiffo
sys.path.append('..')
from we_map import rooms
from we_translation import translation
from we_items import *


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
                print("Gwnaeth cwpl o doriadau ryddhau yr pen.")
                self.needed = False
            elif itemx == item_scissors and itemy == item_bandaged_cane and command == translation["use"]:
                player.inventory.remove(item_bandaged_cane)
                player.inventory.append(item_bandages, item_walking_cane)
                print("Efo'r rhwymyn wedi cael ei ddiswyddo, roedd yr ffon wedi torri unwaith eto.")
                self.needed = False
        except:
            print("Beth ydych yn trio torri?")
        else:
            if command == translation["use"] and itemx == item_improvised_hammer and item_improvised_hammer in player.inventory:
                print("\nMae'r morthwyl yn digon cryf, ac mae'r bocs yn torri.\n Beth sydd yn disgwyl ty mewn gallu bod yn ein ateb i achyb y byd")
                self.completed = True 
                player.current_room["complete"] = True 
                player.add_key(game)
                self.needed = False
            elif command == translation["use"] and itemx == item_make_shift_hammer and item_make_shift_hammer in player.inventory:
                self.completed = True 
                player.current_room["complete"] = True
                self.needed = False
                print("""
Rydych yn taflu'r bocs, nid yw'n gweithio.
Mae pen y morthwyl yn hedfan ac yn gosod yr larwm.
Rydych yn rhedeg allan o'r ystafell fel mae'r drysau yn cau yn awtomatig.
Mae pob dim wedi cael ei golli.
""")
            if needed and command != translation["inspect"]: print("Dydy hyn heb unrhyw effaith")
