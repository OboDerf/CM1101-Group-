translation = {
    # globally used 
    "incorrect_answer": "\nPlease enter a valid answer\n",

    # game.difficulty 
    "difficulty": ['easy', 'medium', 'hard', 'impossible'],

    "difficulty_change": "What difficulty would you like?\n - 1. Easy\n - 2. Medium\n - 3. Hard\n - 4. Impossible\n",

    # add_key's 
    "key_gained": "You obtained a key for your efforts",
    "key_not_gained": "Unfortunately this puzzle paid out no keys",

    # locations ### KEEP THIS UPDATED
    "Prif Derbynfa yr Ysbyty": "Hospital Reception",
    "EXIT" : "EXIT", 
    "Hospital Reception" : "Hospital Reception",
    "Hallway" : "Hallway",
    "Waiting Room" : "Waiting Room",
    "Surgery Room" : "Surgery Room",
    "Cafe" : "Cafe",
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
    "keys": "keys",
    "inspect": "inspect",
    "move": "move",
    "turns": "turns",


    # menu_main's 
    "main_menu_one": """
----------
TEMP MENU
----------
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
    "current_keys_two": " keys.",
    "keys_full": "Congrats! You found all the keys. You can exit the game!",
    "keys_need_one": "You still need to find ",
    "keys_need_two": " keys to win.",

    # help_print's 
    "help_print" :
    """--------------------
                   HELP - Displays a list of all commands and functions,
              INVENTORY - Lists all items currently in your inventory,
                   KEYS - Displays how many keys you have and how many you need,
                  TURNS - Allows you to see how many actions you have left before loss,
              GO <EXIT> - Moves the player to a valid location,
COMBINE <ITEMX> <ITEMY> - Attempts to combine two items together,
           TAKE <ITEMX> - Attempts to take the item and put it in your inventory,
           DROP <ITEMX> - Drops the item on the room's floor,
    USE <ITEMX> <ITEMY> - Uses one item on another or the room (Leave ITEMY empty),
        INSPECT <ITEMX> - Gives you a description of the selected item,
           MOVE <ITEMX> - Moves items you can't pick up. Only works on items in room
--------------------""",
    
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

    # did_user_win's 
    "game_won": "Well done you won!", ## Lackluster as hell, content pls fix this
    "game_not_won": "You don't have enough <<KEYS>> yet.", ## Again, fix this to fit the story
    "game_lost": "Unfortunately you've run out of time. Whatever terrible thing happens is slow and painful."
}   
