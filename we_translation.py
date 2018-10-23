translation = {
    # globally used 
    "incorrect_answer": "\nRhowch ateb dilys.\n",

    # game.difficulty 
    "difficulty": ['hawdd', 'canolig', 'anodd', 'amhosibl'],

    "difficulty_change": "Pa anhawster yr hoffech chi?\n - Hawdd\n - Canolig\n - Anodd\n - Amhosibl\n",

    # add_key's
    "key_gained": "\nYou obtained a vial for your efforts.\n", # Needs Translation
    "key_not_gained": "\nUnfortunately the vial turned out the be a dud.\n", # Needs Translation

    # locations  ### KEEP THIS UPDATED
    "Prif Derbynfa yr Ysbyty": "Prif Derbynfa yr Ysbyty",
    "EXIT" : "ALLANFA",
    "Hospital Reception" : "Prif Derbynfa yr Ysbyty",
    "Hallway" : "Coridor",
    "Waiting Room" : "Ystafell Disgwyl",
    "Surgery Room" : "Ystafell Llawdriniaeth",
    "Patients Room" : "Ystafell Claf",
    "Pharmacy" : "Fferyllfa",
    "Examination Room" : "Ystafell Archwiliad",
    "Doctors Lounge" : "Lolfa Doctoriaid",
    "X-Ray Room" : "Ystafell Peledr X",

    # direction 
    "north": "gogledd",
    "east": "dwyrain",
    "south": "de",
    "west": "gorllewin",

    # commands
    "go": "mynd i'r",
    "help": "help",
    "combine": "cyfuno",
    "take": "cymryd",
    "drop": "gollwng",
    "use": "defnyddio",
    "inventory": "rhestr eiddo",
    "keys": "allweddi",
    "inspect": "archwilio",
    "move": "symud",
    "turns": "twrn",
    "room": "room", # Needs Translation
    "input": "input", # Needs Translation

    # menu_main's 
    "main_menu_one": """
-------------------------------------------------------
TEMP DDEWISLEN
-------------------------------------------------------
Nodwch i:
1. Chwarae'r gêm
2. Togl: English \ Cymraeg
3. Dewiswch anhawster (Ar hyn o bryd """,

    "main_menu_two": """)
0. I ymadael\n""",

    # menu_print's 
    "entry_message": "Rydych o fewn ",
    "command_message": "\nOs rydych yn ansicr o'r gorchmynion posib, teipiwch HELP",

    # print_exit's 
    "exit_one": "Mynd i'r ",
    "exit_two": " i fynd i'r ",
    
    # print_room_items' 
    "room_print_items": "Mae'r eitemau canlynol o fewn yr ystafell yma. I cymryd yr eitem, teipich CYMRYD + ID o'r eitem. E.g:",
    "or": " neu ",

    # print_inventory's 
    "player_print_inventory_one": "Mae gennych:",
    "player_print_inventory_none": "Does gennych ddim eitemau.",

    # print_turns'
    "turns_one": "Mae gennych ",
    "turns_two": " gweithredoedd ar ol.\n",

    #print directions
    "directions_available": "Mae'r cyfeiriadau yma ar gael:",

    # key_print's 
    "current_keys_one": "Rydych efo ",
    "current_keys_two": " vials.", # Needs Translation
    "keys_full": "Congrats! You found all the vials. With these you can create the cure and save humanity!", # Needs Translation
    "keys_need_one": "Rydych dal angen ddod o hyd i ",
    "keys_need_two": " working vials before you can leave this cursed place.", # Needs Translation

    # help_print's   (Needs Translation)
    "help_print" : 
    """
                       HELP - Yn dangos y rhestr o orchmynion posib,
                      EIDDO - Yn rhestru pob eitem sydd yn eich rhestr eiddo,
                      VIALS - Displays how many vials you have and how many you need, 
                      TURNS - Allows you to see how many actions you have left before loss,
                       ROOM - Prints the description of the room and the items within it,
            MYND I'R <EXIT> - Yn symyd yr chwaraewr i lleoliad dilys,
               INPUT <TEXT> - Inputs text for those times when hitting items together isn't enough,
     CYFUNO <ITEMX> <ITEMY> - Yn gwneud ymgais i gyfuno dwy eitem efo'i gilydd,
             CYMRYD <ITEMX> - Yn gwneud ymgais i cymryd eitem ac wedyn rhoi yn eich rhestri eiddo,
            GOLLWNG <ITEMX> - Yn gollwng yr eitem ar y llawr,
  DEFNYDDIO <ITEMX> <ITEMY> - Uses one item on another or the room (Leave ITEMY empty),
          ARCHWILIO <ITEMX> - Gives you a description of the selected item,
            SYMYD Y <ITEMX> - Moves items you can't pick up. Only works on items in room
-------------------------------------------------------""",

    # process_move's 
    "cannot_move": "Dydych fethu mynd i fana",
    "already_completed": "Mae'r ystafell yma wedi cael ei gwblhau yn barod",

    # process_take's 
    "cannot_take": "Dydych methu cymryd hwnna",
    "cannot_take_two": "Dydy'r eitem yna ddim yn yr ystafell hon",

    # process_drop's 
    "cannot_drop": "Nid oes gennych yr eitem yna",

    # process_inspect's 
    "cannot_inspect": "Doedd yr eitem yna methu cael ei ddarganfod",

    # process_move_item's 
    "moving_item": "Rydych wedi symyd ",
    "item_already_moved": "Mae'r eitem yma wedi cael ei symyd yn barod",
    "cannot_move_item": "Dydych methu'r symyd yr eitem hon",
    "cannot_find_move": "Methu ddod o hyd i'r eitem i symyd",

    # process_combine's 
    "combine_succ_one": "Rydych wedi cyfuno'r eitemau yn llwyddianus ",
    "combine_succ_two": " efo ",
    "combine_succ_three": " i greu ",
    "combine_same": "Dydych methu cyfuno'r eitem efo ei hun",
    "combine_fail": "Dydych methu cyfuno'r ddwy eitem yma",
    "combine_no_item": "Mathu ddod o hyd i'r eitemau yna",
    
    # did_user_win's (Needs translation)
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
We require only the strength to follow it.

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
