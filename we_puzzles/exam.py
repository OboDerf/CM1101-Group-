import sys # Credit to Reddit user /u/cpt_fwiffo
sys.path.append('..')
from we_map import rooms
from we_translation import translation
from we_items import *
from random import randint


class exam:

    def __init__(self):
        self.linked_rooms = [rooms["Ystafell Archwiliad"]]
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
                error = ["Dwi ddim yn gwybod beth rydych yn trio gwneud, ond doedd o ddim yn gweithio",
                         "hmmm..triwch rhywbeth arall",
                         "beth oedd hwnna?",
                         "Beth roeddwch chi'n meddwl?"]
                print(error[randint(0,3)])
        else:
            print("Dim byd i weld...")
        

    def puzzle_one(self, itemx, game, command, player):
        if itemx["id"] == "chair" and command == "inspect":
            print("""Gan archwilio'r offer, rydych yn sylweddoli bod yno llif asgwrn, morthwyl ac rhyw fath o lletem... Sut bydd rhain yn gallu bod yn defnyddiol?
                  """)
            player.current_room["items"].extend([item_hammer, item_saw, item_wedge])
            player.current_room["items"].remove(item_chair)
            self.chair_puzzle = True
            self.needed = False
            
    
    def puzzle_two(self, itemx, game, command, player):
        if itemx["id"] == "hammerwedge" and command == "use":
            print("Gan defnyddio eich lletem morthwyl newydd, rydych yn trio agor yr drôr ac... mae'n agor! Ond beth yw'r pen yna?")
            player.current_room["items"].append(item_head)
            self.hammer_puzzle = True
            self.needed = False

            
    def puzzle_three(self, itemx, game, command, player):
        if itemx["id"] == "table" and command == "inspect":
            print("Hmmm… oedd yr bwrdd archwilio yn edrych yn glan, ond nawr rwyn sylweddoli rhyw fath o hylif arno")
            item_table["pick_up"] = True
            self.table_puzzle  = True
            self.needed = False

            
    def puzzle_four(self, itemx, game, command, player):
        if itemx["id"] == "jar" and command == "use":
            if item_table in player.inventory:
                print("Rydych yn llwyddo i llenwi'r jar efo'r hylif o'r cadair")
                player.inventory.remove(item_jar)
                player.inventory.remove(item_table)
                player.inventory.append(item_full_jar)
                self.fluid_puzzle = True
                self.needed = False
            else:
                print("Dydych methu gwneud hyn eto...")
                self.needed = False            
        

    def puzzle_final(self, itemx, game, command, player):
        if command == "use" and itemx["id"] == "fluid": 
            self.completed = True 
            player.current_room["completed"] = True 
            print("Rydych yn sylweddoli rhyw faint or pen yn dadmar, felly rydych yn penderfynu i tollti gweddill o'r hylif. Rydych yn edrych o fewn yr pen ac yn syldweddoli... Ffiol!")
            player.inventory.remove(item_full_jar)
            player.add_key(game)
            player.current_room = rooms[translation["Hospital Reception"]]
            self.needed = False

