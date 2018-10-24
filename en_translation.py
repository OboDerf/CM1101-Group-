translation = {
    # globally used 
    "incorrect_answer": "\nPlease enter a valid answer\n",

    # game.difficulty 
    "difficulty": ['easy', 'medium', 'hard', 'impossible'],

    "difficulty_change": "What difficulty would you like?\n - 1. Easy\n - 2. Medium\n - 3. Hard\n - 4. Impossible\n",

    # add_key's 
    "key_gained": "\nYou obtained a vial for your efforts.\n",
    "key_not_gained": "\nUnfortunately the vial turned out the be a dud.\n",

    # locations ### KEEP THIS UPDATED
    "Prif Derbynfa yr Ysbyty": "Hospital Reception",
    "EXIT" : "EXIT", 
    "Hospital Reception" : "Hospital Reception",
    "Hallway" : "Hallway",
    "Waiting Room" : "Waiting Room",
    "Surgery Room" : "Surgery Room",
    "Patients Room" : "Patients Room",
    "Pharmacy" : "Pharmacy",
    "Examination Room" : "Examination Room",
    "Doctors Lounge" : "Doctors Lounge",
    "X-Ray Room" : "X-Ray Room",

    # direction
    "north": "north",
    "east": "east",
    "south": "south",
    "west": "west",

    # commands
    "go": "go",
    "help": "help",
    "combine": "combine",
    "take": "take",
    "drop": "drop",
    "use": "use",
    "inventory": "inventory",
    "keys": "vials",
    "inspect": "inspect",
    "move": "move",
    "turns": "turns",
    "room": "room",
    "input": "input",


    # menu_main's 
    "main_menu_one": """
-------------------------------------------------------
Main Menu
-------------------------------------------------------
Enter to:
1. Play the game
2. Toggle: English \ Cymraeg
3. To pick difficulty (Currently """,

    "main_menu_two": """)
0. To exit\n""",
	
    # menu_print's
    "entry_message": "You are now in ",
    "command_message": "\nIf you're ever unsure of avalible commands, use HELP",

    # print_exit's
    "exit_one": "GO ",
    "exit_two": " to ",

    # print_room_items'
    "room_print_items": "The following items are in the room. To pick up an item, type TAKE + ID of the item. E.g.: ",
    "or": " or ",

    # print_inventory's 
    "player_print_inventory_one": "You have the following items:",
    "player_print_inventory_none": "You have no items",

    # print_turns'
    "turns_one": "You have ",
    "turns_two": " actions left.\n",

    #print directions
    "directions_available": "The follwing directions are avalible:",

    # key_print's 
    "current_keys_one": "You currently have ",
    "current_keys_two": " vials.",
    "keys_full": "Congrats! You found all the vials. With these you can create the cure and save humanity!",
    "keys_need_one": "You still need to find ",
    "keys_need_two": " working vials before you can leave this cursed place.",

    # help_print's 
    "help_print" :
    """
                   HELP - Displays a list of all commands and functions,
              INVENTORY - Lists all items currently in your inventory,
                  VIALS - Displays how many vials you have and how many you need,
                  TURNS - Allows you to see how many actions you have left before the mask breaks,
                   ROOM - Prints the description of the room and the items within it,
              GO <EXIT> - Moves the player to a valid location,
           INPUT <TEXT> - Inputs text for those times when hitting items together isn't enough,
COMBINE <ITEMX> <ITEMY> - Attempts to combine two items together,
           TAKE <ITEMX> - Attempts to take the item and put it in your inventory,
           DROP <ITEMX> - Drops the item on the room's floor,
    USE <ITEMX> <ITEMY> - Uses one item on another or the room (Leave ITEMY empty),
        INSPECT <ITEMX> - Gives you a description of the selected item,
           MOVE <ITEMX> - Moves items you can't pick up. Only works on items in room
-------------------------------------------------------""",
    
    # process_move's 
    "cannot_move": "You cannot go there",
    "already_completed": "This room is already completed",

    # process_take's 
    "cannot_take": "You cannot take that",
    "cannot_take_two": "This item isn't in this room",

    # process_drop's 
    "cannot_drop": "This item isn't in your inventory",

    # process_inspect's 
    "cannot_inspect": "This item couldn't be found",

    # process_move_item's 
    "moving_item": "You have moved ",
    "item_already_moved": "This item has already been moved",
    "cannot_move_item": "You cannot move this item",
    "cannot_find_move": "Cannot find this item to move",

    # process_combine's 
    "combine_succ_one": "You successfully combined ",
    "combine_succ_two": " with ",
    "combine_succ_three": " to make ",
    "combine_same": "You cannot combine an item with itself",
    "combine_fail": "You can't combine those two items",
    "combine_no_item": "Couldn't find those items",

    # surgery
    "surgery_patient": "You just received a needle!",
    "surgery_needle": "You just unlocked the lockers. You got a medicine now",
    "surgery_medicine": "You just brought the doctor back to life. He gave you his pass card",
    "surgery_pass": "Congrats, you solved the puzzle, you got the vial now!",

    # did_user_win's
    "intro": """
-------------------------------------------------------

Everyone in the world is affected by a the CM1101
virus a.k.a Krillian. You have been sent on a mission
to an abandoned hospital in the hope of finding a cure.
Rumour has it they were close, bottling potential
remedies in vials. You seek to obtain these at any cost.

Your preperation was swift, to the point where you now
rely upon a defective gas mask as key to your survival.
There are a total of 6 rooms in the hospital that may
contain vials, within these rooms are items that can
be picked up and used to help you collect the vials.
Items can be both used on their own or with another
appropriate item.

Your time is limited. The way is lit. The path is clear.
You require only the strength to follow it.

-------------------------------------------------------""",
    "game_won": """"
-------------------------------------------------------

██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ 
╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  
 ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   
  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝

-------------------------------------------------------

You escape the forgotten tomb, vials clutched in hand.
You withdraw you cracked mask to view your own heroics.
Many fall in the face of chaos; but not this one, not
today. With this you can create the cure, the promise 
of safety! A moment of valour shines brightest against
the backdrop of dispair. As the light gains purchase,
spirits are lifted and purpose is made clear.

-------------------------------------------------------

""",
    "game_not_won": "You don't have enough vials yet. To leave would be to surrender hope.",
    "game_lost": "Slowly. Gently. This is how a life is taken."
}   
