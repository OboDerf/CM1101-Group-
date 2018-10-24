translation = {
    # globally used 
    "incorrect_answer": "\nRhowch ateb dilys.\n",

    # game.difficulty 
    "difficulty": ['hawdd', 'canolig', 'anodd', 'amhosibl'],

    "difficulty_change": "Pa anhawster yr hoffech chi?\n - Hawdd\n - Canolig\n - Anodd\n - Amhosibl\n",

    # add_key's
    "key_gained": "\nRydych wedi cael ffiol am eich gwaith.\n",
    "key_not_gained": "\nYn anffodus, doedd yna ddim ffiol yma.\n",

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
    "keys": "ffiolau",
    "inspect": "archwilio",
    "move": "symud",
    "turns": "twrn",
    "room": "ystafell",
    "input": "mewnbwn",

    # surgery
    "surgery_patient": "Rydych newydd derbyn nodwydd!",
    "surgery_needle": "Rydych newydd agor yr cloirau. Mae gennych yr ffisig nawr",
    "surgery_medicine": "Rydych newydd dod a'r doctor nol i fyw. Rhodd o ei cardyn staff iddych chi.",
    "surgery_pass": "Llongyfarchiadau! datryswyd yr tasg, mae gennych yr goriad nawr!",

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
    "current_keys_two": " ffiolau.",
    "keys_full": "Llongyfarchiadau! Rydych wedi ddod o hyd i pob ffiol. Efo rhain bydd yn bosib i achub dynoliaeth!",
    "keys_need_one": "Rydych dal angen ddod o hyd i ",
    "keys_need_two": " ffiolau (sy'n gweithio) cyn gadael yr ysbyty melltigedig.",

    # help_print's
    "help_print" : 
    """
                       HELP - Yn dangos y rhestr o orchmynion posib,
                      EIDDO - Yn rhestru pob eitem sydd yn eich rhestr eiddo,
                      VIALS - Dangos faint o ffiolau sydd gennych ac faint sydd angen, 
                      TURNS - Allows you to see how many actions you have left before loss,
                       ROOM - Yn argraggu yr disgrifiad o'r ystafell ac yr eitemau sydd ynddo,
            MYND I'R <EXIT> - Yn symyd yr chwaraewr i lleoliad dilys,
               INPUT <TEXT> - Yn mewnbynnu testyn ar gyfer yr adegoedd lle dydy hitio eitemau efo'i gilydd ddim yn gweithio,
     CYFUNO <ITEMX> <ITEMY> - Yn gwneud ymgais i gyfuno dwy eitem efo'i gilydd,
             CYMRYD <ITEMX> - Yn gwneud ymgais i cymryd eitem ac wedyn rhoi yn eich rhestri eiddo,
            GOLLWNG <ITEMX> - Yn gollwng yr eitem ar y llawr,
  DEFNYDDIO <ITEMX> <ITEMY> - Yn defnyddio un eitem ar un arall, neu ar yr ystafell (Gadael ITEMY yn gwag),
          ARCHWILIO <ITEMX> - Yn rhoi disgrifiad o'r eitem yna,
            SYMYD Y <ITEMX> - yn symyd yr eitem nad ydych yn gallu codi. Ond yn gweithio ar eitemau o fewn ystafell
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
    
    # did_user_win's 
    "intro": """
-------------------------------------------------------

Mae pawb yn y byd wedi cael ei effeithio gan y firws
CM1101 a.k.a Krillian. Rydych wedi cael eich gyrru ar
cenhadaeth i ysbyty gwag i drio darganfod iachiâd. Yn
ôl beth mae pawb yn dweud, roeddynt yn agos. Mae rhaid
ddod o hyd i'r ffiolau, arhoswch yna tan iddych gorffen
eich cenhadaeth.

Doedd genych ddim digon o amser i baratoi ar gyfer eich
trip, nawr rydych yn dibynnu ar fwgwd nwy diffygiol fel
eich unig ffordd o anadlu. Mae yna 6 ystafell sydd yn
gallu dal y ffiolau. Tŷ fewn i'r ystafelloedd yma, mae
yna eitemau sydd yn gallu cael ei ddefnyddio i helpu
chi cwblhau eich tasg. Bydd eitemau yn gallu cael ei
ddefnyddio ar ben ei hun neu efo un arall.

Mae eich amser yn gyfyngedig. Bydd angen i chi gwblhau
y dasg efo prysurdeb. Neu efallai byddych yn rhy hwyr.

-------------------------------------------------------""",
    "game_won": """"
                    -------------------------------------------------------

██████╗ ██╗   ██╗██████╗ ██████╗ ██╗   ██╗ ██████╗  ██████╗ ██╗     ██╗ █████╗ ███████╗████████╗██╗  ██╗
██╔══██╗██║   ██║██╔══██╗██╔══██╗██║   ██║██╔════╝ ██╔═══██╗██║     ██║██╔══██╗██╔════╝╚══██╔══╝██║  ██║
██████╔╝██║   ██║██║  ██║██║  ██║██║   ██║██║  ███╗██║   ██║██║     ██║███████║█████╗     ██║   ███████║
██╔══██╗██║   ██║██║  ██║██║  ██║██║   ██║██║   ██║██║   ██║██║     ██║██╔══██║██╔══╝     ██║   ██╔══██║
██████╔╝╚██████╔╝██████╔╝██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║██║  ██║███████╗   ██║   ██║  ██║
╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝

                    -------------------------------------------------------

                    Rydych wedi ddianc o'r ysbyty, ffiolau yn eich dwylo
                    ac yn cymryd eich mwgwd nwy ac yn taflu ar yr llawr.
                    Nawr mae'n bosib iddych edrych ar eich gweithredoedd
                    arwrol. Mae nifer o bobl yn torri odan y gwasgedd; ond
                    dim chi, dim heddiw. Efo hyn mae'n bosib i greu yr
                    iachiâd, yr gaddo i rhoi ddiogelwch i bawb.

                    -------------------------------------------------------

""",
    "game_not_won": "Does gennych dim digon o ffiolau eto. I adael byddych yn gadael pawb lawr.",
    "game_lost": "Ac oedd pawb yn dibynu arnoch chi..."
}
