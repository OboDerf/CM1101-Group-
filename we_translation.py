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
    "entry_message": "Rydych o fewn ",
    "command_message": "Os rydych yn ansicr o'r gorchmynion posib, teipiwch HELP\n",

    # print_exit's (Needs translation)
    "exit_one": "Mynd i'r ",
    "exit_two": " i fynd i'r ",

    # print_room_items' (Needs translation)
    "room_print_items_one": "Mae yna:",
    "room_print_items_two": "yn yr ystafell hon.\n",
    "or": " neu ",

    # print_inventory's (Needs translation)
    "player_print_inventory_one": "Mae gennych:",
    "player_print_inventory_none": "Does gennych ddim eitemau.",

    # key_print's (Needs translation)
    "current_keys_one": "Rydych efo ",
    "current_keys_two": " allwedd.",
    "keys_full": "Llongyfarchiadau! Rydych wedi dod o hyd i bob goriad! Rydych yn gallu gadael y gêm!",
    "keys_need_one": "Rydych dal angen ddod o hyd i ",
    "keys_need_two": " allweddau i ennill.",

    # help_print's (Needs translation)
    "help_print" :
    """--------------------
                       HELP - Yn dangos y rhestr o orchmynion posib,
                      EIDDO - Yn rhestru pob eitem sydd yn eich rhestr eiddo,
                  Allweddau - Yn dangos faint o goriadau sydd gennych ac faint sydd angen i ennill,
            MYND I'R <EXIT> - Yn symyd yr chwaraewr i lleoliad dilys,
     CYFUNO <ITEMX> <ITEMY> - Yn gwneud ymgais i gyfuno dwy eitem efo'i gilydd,
             CYMRYD <ITEMX> - Yn gwneud ymgais i cymryd eitem ac wedyn rhoi yn eich rhestri eiddo,
            GOLLWNG <ITEMX> - Yn gollwng yr eitem ar y llawr,
  DEFNYDDIO <ITEMX> <ITEMY> - Uses one item on another or the room (Leave ITEMY empty),
          ARCHWILIO <ITEMX> - Gives you a description of the selected item,
            SYMYD Y <ITEMX> - Moves items you can't pick up. Only works on items in room
--------------------""",

    # process_move's (Needs translation)
    "cannot_move": "Dydych fethu mynd i fana",
    "already_completed": "Mae'r ystafell yma wedi cael ei gwblhau yn barod",

    # process_take's (Needs translation)
    "cannot_take": "Dydych methu cymryd hwnna",
    "cannot_take_two": "Dydy'r eitem yna ddim yn yr ystafell hon",

    # process_drop's (Needs translation)
    "cannot_drop": "Nid oes gennych yr eitem yna",

    # process_inspect's (Needs translation)
    "cannot_inspect": "Doedd yr eitem yna methu cael ei ddarganfod",

    # process_move_item's (Needs translation)
    "moving_item": "Rydych wedi symyd ",
    "item_already_moved": "Mae'r eitem yma wedi cael ei symyd yn barod",
    "cannot_move_item": "Dydych methu'r symyd yr eitem hon",
    "cannot_find_move": "Methu ddod o hyd i'r eitem i symyd",

    # process_combine's (Needs translation)
    "combine_succ_one": "Rydych wedi cyfuno'r eitemau yn llwyddianus ",
    "combine_succ_two": " efo ",
    "combine_succ_three": " i greu ",
    "combine_same": "Dydych methu cyfuno'r eitem efo ei hun",
    "combine_fail": "Dydych methu cyfuno'r ddwy eitem yma",
    "combine_no_item": "Mathu ddod o hyd i'r eitemau yna",
    
    # did_user_win's (Needs translation)
    "game_won": "Llongyfarchiadau! Rydych wedi ennill!!!", ## Lackluster as hell, content pls fix this
    "game_not_won": "Dydych ddim efo digon o <<KEYS>> eto." ## Again, fix this to fit the story
}
