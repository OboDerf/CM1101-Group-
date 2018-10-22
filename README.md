# CM1101-Group-

# Tasks to do 
- Kai and Jack is coding the <b>patient's</b> room
- Connor is coding <b>Doctor's Lounge</b> room
- Marton is coding <b>X-ray</b> room
- Marton is coding <b>Surgery</b> room
- Kai is coding <b>Pharmacy</b>
- Someone will code <b>Exam</b> room
 

# Github Help
1. Whenever you want to work on the project, make sure to pull the latest version by typing: "git pull"
2. Once you've made some changes in the code, run git status to see which files you've modified by typing: "git status"
3. Add your modified files by typing: "git add file.py"
3. Commit your changes to your local repository by typing: "git commit -m "commit message"
4. Push your changes by typing: "git push"
 
# FRAMEWORK - A BRIEF AND LOOSE EXPLAINATION ON THE PUZZLES

   Key:

 - self: This means you're using a variable or function defined within the class. It's an easy way of carrying 
         variables over for when you're feeling lazy. Add new variables to __init__ and new functions wherever you want

 - itemx: So this will always be an item directly from the item file. You need to check it's location (in room vs
          in inventory) before you can use it. 

 - itemy: This will only contain a variable on 'use <itemx> <itemy>'. Otherwise calling it will return an error that's
          try excepted' all the way over in game.py. Use this only for item on item though

 - player: Player is a class defined in game.py. It has the current room, inventory, and all that good stuff in.
           player.current_room is the current room
           player.inventory is the inventory

 - game: This mostly holds stats and shouldn't be needed outside of puzzle_final's player.add_key(game)

   Common Functions:

 - itemx in player.inventory: checks if the item is in the player's inventory

 - itemx in player.current_room["items"]: checks if the item is in the room's floor

 - itemx["moved"]: Checks if the item has been moved

 - itemx["id"] == "example": Checks if the player's inputed item is what you're looking for

 - NOTE: Combining is handled elsewhere. If the puzzle requires a combined item, look for it's ID

 - You can always make more def var() functions or self.var = <> statements. What's provided is a framework. 

 - When a change is made and you're calling it, please also update the welsh version (Just override until it's finished though)

 - If there's anything I've missed, do ask.

 - If you're going to add in more rooms to your puzzle, ask me how to do it (Or try it yourself, who am I to tell you what to do?)


import sys # Credit to Reddit user /u/cpt_fwiffo
sys.path.append('..')
from en_map import rooms


class doctors:

    def __init__(self):
        self.linked_rooms = [rooms["Doctors Lounge"]] # This keeps a track of what rooms are in this puzzle.
        self.completed = False # This keeps a track of if the user has 

        ## Any progress checks would go here EG:
        self.puzzle_one = False

    def puzzle_process(self, itemx, itemy, player, game): # The more if statements here, the more parts to the puzzle there are
        needed = True
        if not self.puzzle_one:
            puzzle_one(self, itemx, player)
        elif not <> and needed = True:
            <>()
        elif not <> and needed = True:
            <>()
        elif <> and <> and needed = True: # This check should be your last
            
        if needed: print("That had no effect")

    def puzzle_one(self):
        if <> == <> and <> in <>: # How do they complete the task? 
            print("Some fluff about how well they're doing, tell them what they just did")
            self.puzzle_one = True #(Or whatever you end up calling it)
            return False # This means you no longer need to tell the user they did nothing
        else:
            return True # This means they failed the check and may still need a message saying 'did nothing'
    

    def puzzle_final(self, game, player):
        self.completed = True
        player.current_room["complete"] = True
        player.add_key(game)
