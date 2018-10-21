import en_puzzles.surgery
import en_puzzles.patients
import en_puzzles.pharmacy
import en_puzzles.exam
import en_puzzles.doctors
import en_puzzles.xray
import we_puzzles.surgery
import we_puzzles.patients
import we_puzzles.pharmacy
import we_puzzles.exam
import we_puzzles.doctors
import we_puzzles.xray


from en_map import rooms
import en_items

            

class example:

    def __init__(self):
        #These two are standard. One is to track the rooms within the puzzle
        #One is to track if the puzzle is completed
        self.linked_rooms = [rooms["Example Room"]]
        self.completed = False

        #Each of these tracks the sub-value of the puzzles, allowing you to program a puzzle with more than one stage
        self.puzzle_part_one = False
        self.puzzle_part_two = False


    def puzzle_process(self, itemx, itemy, command, player, game):
        #There will only be two functions that call puzzle_process: Use and Move.
        #If you want anything else, speak to me but be quick about it
        try:
            needed = True
            if not self.puzzle_part_one:
                needed = self.puzzle_one(itemx, player)
                
            if not self.puzzle_part_two and needed:
                # Every call after the first one check if needed. This will make sure we don't accidently send more error messages then needed
                needed = self.puzzle_two(itemx, player)

            if self.puzzle_part_one and self.puzzle_part_two and not self.completed and needed:
                needed = self.puzzle_final(itemx, itemy, player, game)
                
            # This prints only if none of the puzzles were completed
            if needed: print("That had no effect")
        except TypeError:
            print("That had no effect")
                    
    #This puzzle is a move command puzzle. Once examplemove is moved, exampletwo is added to the room
    def puzzle_one(self, itemx, player):
        if itemx["id"] == "examplemove" and itemx["moved"]:
            self.puzzle_part_one = True
            #Saying the puzzle is now completed
            print("Moving the item revealed an item!")
            #Adding in any fluff with the action
            player.current_room["items"].append(en_items.item_example_two)
            return False # The return is to see if the error message is needed
        else:
            return True

    def puzzle_two(self, combined_item, player):
        if combined_item["id"] == "examplecombined" and combined_item in player.inventory:
            print("You successfully used the combined item. Now use two on combined or the reverse")
            self.puzzle_part_two = True
            return False
        else:
            return True

    def puzzle_final(self, itemx, itemy, player, game):
        if itemx["id"] == "examplecombined" and itemy["id"] == "exampletwo" and itemy in player.inventory and itemx in player.inventory:
            player.current_room["completed"] = True
            player.add_key(game)
            print("Wow, you completed the test room!")
            return False
        else:
            return True

we_puzzles = {
    
    "example": example(),

    "surgery": we_puzzles.surgery.surgery(),

    "patients": we_puzzles.patients.patients(),

    "pharmacy": we_puzzles.pharmacy.pharmacy(),

    "exam": we_puzzles.exam.exam(),

    "doctors": we_puzzles.doctors.doctors(),

    "xray": we_puzzles.xray.xray()
}

en_puzzles = {
    
    "example": example(),

    "surgery": en_puzzles.surgery.surgery(),

    "patients": en_puzzles.patients.patients(),

    "pharmacy": en_puzzles.pharmacy.pharmacy(),

    "exam": en_puzzles.exam.exam(),

    "doctors": en_puzzles.doctors.doctors(),

    "xray": en_puzzles.xray.xray()
}
