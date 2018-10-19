translation = {
    # globally used (Completed, for now)
    "incorrect_answer": "\nRhowch ateb dilys.\n",

    # game.difficulty (Completed)
    "difficulty": ['hawdd', 'canolig', 'anodd', 'amhosibl'],

    "difficulty_change": "Pa anhawster yr hoffech chi?\n - Hawdd\n - Canolig\n - Anodd\n - Amhosibl\n",

    # locations (Completed) ### KEEP THIS UPDATED
    "Prif Derbynfa yr Ysbyty": "Prif Derbynfa yr Ysbyty",
    "EXIT" : "ALLANFA",
    "Hospital Reception" : "Prif Derbynfa yr Ysbyty",
    "Hallway" : "Coridor",
    "Waiting Room" : "Ystafell Disgwyl",
    "Surgery Room" : "Ystafell Llawdriniaeth",
    "Cafe" : "Caffi",
    "Pharmacy" : "Fferyllfa",
    "Examination Room" : "Ystafell Archwiliad",
    "Doctors Lounge" : "Lolfa Doctoriaid",
    "X-Ray Room" : "Ystafell Peledr X",

    # direction (Completed)
    "north": "gogledd",
    "east": "dwyrain",
    "south": "de",
    "west": "gorllewin",

    # commands (Needs translation)
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

    # menu_main's (Completed)
    "main_menu_one": """
----------
TEMP DDEWISLEN
----------
Nodwch i:
1. Chwarae'r gêm
2. Togl: English \ Cymraeg
3. Dewiswch anhawster (Ar hyn o bryd """,

    "main_menu_two": """)
0. I ymadael\n""",

    # menu_print's (Needs translation)
    "entry_message": "You are now in ",
    "command_message": "If you're ever unsure of avalible commands, use HELP\n",

    # print_exit's (Needs translation)
    "exit_one": "GO ",
    "exit_two": " to ",

    # print_room_items' (Needs translation)
    "room_print_items_one": "There is:",
    "room_print_items_two": "In this room.\n",
    "or": " or ",

    # print_inventory's (Needs translation)
    "player_print_inventory_one": "You have:",
    "player_print_inventory_none": "You have no items",

    # key_print's (Needs translation)
    "current_keys_one": "You currently have ",
    "current_keys_two": " keys.",
    "keys_full": "Congrats! You found all the keys. You can exit the game!",
    "keys_need_one": "You still need to find ",
    "keys_need_two": " keys to win.",

    # help_print's (Needs translation)
    "help_print" :
    """--------------------
                   HELP - Displays a list of all commands and functions,
              INVENTORY - Lists all items currently in your inventory,
                   KEYS - Displays how many keys you have and how many you need,
              GO <EXIT> - Moves the player to a valid location,
COMBINE <ITEMX> <ITEMY> - Attempts to combine two items together,
           TAKE <ITEMX> - Attempts to take the item and put it in your inventory,
           DROP <ITEMX> - Drops the item on the room's floor,
    USE <ITEMX> <ITEMY> - Uses one item on another or the room (Leave ITEMY empty),
        INSPECT <ITEMX> - Gives you a description of the selected item,
           MOVE <ITEMX> - Moves items you can't pick up. Only works on items in room
--------------------""",

    # process_move's (Needs translation)
    "cannot_move": "You cannot go there",
    "already_completed": "This room is already completed",

    # process_take's (Needs translation)
    "cannot_take": "You cannot take that",
    "cannot_take_two": "This item isn't in this room",

    # process_drop's (Needs translation)
    "cannot_drop": "This item isn't in your inventory",

    # process_inspect's (Needs translation)
    "cannot_inspect": "This item couldn't be found",

    # process_move_item's (Needs translation)
    "moving_item": "You have moved ",
    "item_already_moved": "This item has already been moved",
    "cannot_move_item": "You cannot move this item",
    "cannot_find_move": "Cannot find this item to move",

    # process_combine's (Needs translation)
    "combine_succ_one": "You successfully combined ",
    "combine_succ_two": " with ",
    "combine_succ_three": " to make ",
    "combine_same": "You cannot combine an item with itself",
    "combine_fail": "You can't combine those two items",
    "combine_no_item": "Couldn't find those items",
    
    # did_user_win's (Needs translation)
    "game_won": "Well done you won!", ## Lackluster as hell, content pls fix this
    "game_not_won": "You don't have enough <<KEYS>> yet." ## Again, fix this to fit the story
}
