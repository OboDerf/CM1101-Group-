import sys # Credit to Reddit user /u/cpt_fwiffo
sys.path.append('..')
from we_items import *
from we_map import rooms
from we_translation import translation


class patients:

    def __init__(self):
        self.linked_rooms = [rooms["Ystafell Claf"]]
        self.completed = False
        self.needed = True
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
        if self.needed: print("Gwnaeth dim byd digwydd")  


    def error_safe(self, itemx, game, command, player):
        if item_lamp in player.inventory and command == "use" and  itemx == item_lamp:
            print ("Rydych yn hitio'r person yn anymwybodol!")
            self.needed = False
            self.completed = True 
            player.current_room["completed"] = True
            player.add_key(game)
        else:
            print("Rydych yn rhedeg allan o'r ystafell. Mae'r drws yn cloi tŷ ôl i chi.")
            self.completed = True
            player.current_room["completed"] = True
            player.current_room = rooms[translation["Hallway"]]
            

    def puzzle_one(self, itemx, command, player):
        if command == "archwilio" and itemx["id"] == "silff": # How do they complete the task? 
            player.current_room["items"].extend([item_book_1, item_book_2, item_book_3, item_book_4])
            player.current_room["items"].remove(item_bookshelf)
            self.needed = False
            self.puzzle_inspect = True 
        else:
            self.needed = False
            print("Doedd yna dim effaith")
            

    def puzzle_two(self, itemx, command, player):
        if (command == "archwilio" or command == "defnyddio") and itemx["id"] == "llyfr2":
            self.needed = False
            self.puzzle_book1 = True
            print ("Rydych yn darllen yr ail lyfr, mae’r ddynas yn y cornel yn codi ei phen allan o’i dulo.")
        else:
            self.needed = False
            self.attempts -=  1
            if self.attempts == 1:            
                print("Mae’r ddynas yn edrych ato chi, dydy hi ddim yn edrych yn hapus.")
            elif self.attempts == 0:
                print("Mae’r ddynas yn rhedeg yn eich cyfeiriad. Rydych yn:")

    def puzzle_three(self, itemx, command, player):
        if (command == "archwilio" or command == "defnyddio") and itemx["id"] == "llyfr4":
            self.needed = False
            self.puzzle_book2 = True
            print ("Rydych yn darllen yr pedwerydd lyfr, mae’r dynas yn sefych i fyny ac yn gwenu arnych chi.")
        else:
            self.needed = False
            self.puzzle_book1 = False
            self.attempts -=  1
            if self.attempts == 1:            
                print("Mae’r ddynas yn edrych ato chi, dydy hi ddim yn edrych yn hapus.")
            elif self.attempts == 0:
                print("Mae’r ddynas yn rhedeg yn eich cyfeiriad. Rydych yn:")

    def puzzle_four(self, itemx, command, player):
        if (command == "archwilio" or command == "defnyddio") and itemx["id"] == "llyfr3":
            self.needed = False
            self.puzzle_book3 = True
            print ("Rydych yn darllen yr trydydd lyfr, mae’r dynas yn cerdded ar draws yr ystafell ac yn gorfadd yn ei gwely.")
        else:
            self.needed = False
            self.puzzle_book1 = False
            self.puzzle_book2 = False
            self.attempts -=  1
            if self.attempts == 1:            
                print("Mae’r ddynas yn edrych ato chi, dydy hi ddim yn edrych yn hapus.")
            elif self.attempts == 0:
                print("Mae’r ddynas yn rhedeg yn eich cyfeiriad. Rydych yn:")
        
    
    def puzzle_final(self, itemx, game, command, player):
        if (command == "defnyddio" or command == "archwilio") and itemx["id"] == "llyfr1":
            print ("Rydych yn darllen yr llyfr cyntaf, mae’r dynas yn cymryd ei cadwyn du ac yn rhoi ar ei silf gwely. Mae’r ffiol ar ei cadwyn!")
            self.needed = False
            self.completed = True 
            player.current_room["completed"] = True # This tells the rooms it's completed
            
            player.add_key(game) # Finally, this adds the key
            return False 
