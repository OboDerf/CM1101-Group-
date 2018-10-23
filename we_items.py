item_make_shift_hammer = {
    "id": "makeshift",# needs translating
    "name": "Make shift hammer",# needs translating
    "description": """A deadly weapon, were its head any sturdier.""",# needs translating
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_bandaged_hammer = {
    "id": "bandagedhammer",# needs translating
    "name": "Bandaged hammer head",# needs translating
    "description": """A blow softened. The purpose is lost on you.""",# needs translating
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_improvised_hammer = {
    "id": "improvhammer",# needs translating
    "name": "Improvised Hammer",# needs translating
    "description": """The right tool to forge the path.""",# needs translating
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_bandaged_cane = {
    "id": "bandagedcane",# needs translating
    "name": "Bandages walking cane",# needs translating
    "description": """Given new life. A step towards hope.""",# needs translating
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_scissors = {
    "id": "sisyrnau",
    "name": "Par o sisiyrnau",
    "description": """Dur gwrthstean. Mae'n edrych fel bod nhw wedi bod yma am byth.""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_hammer_head = {
    "id": "penmorthwyl",
    "name": "Pen o morthwryl",
    "description": """Wedi cael ei gwahanu o bwrpas. Rhydlyd efo oed. O hyn bydd rhai yn gweld pwrpas newydd.""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_bandages = {
    "id": "rhwymynnau",
    "name": "Rol o rhwymynnau",
    "description": """Wedi cael ei gylmu efo'i gilydd am dim rheswm o gwbl.""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_walking_cane = {
    "id": "ffon",
    "name": "Ffon cerdded",
    "description": """Wedi cael ei dorri yn hanner, efallai oedd y gwasgedd yn gormod""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_book_1 = {
    "id" : "llyfr1", 
    "name" : "Llyfr cyntaf", 
    "description" : "Mae'r llyfr yma yn edrych fel yr un cyntaf mewn cyfres?", 
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_book_2 = {
    "id" : "llyfr2", 
    "name" : "Ail llyfr", 
    "description" : "Mae'r llyfr yma yn edrych fel yr un ail mewn cyfres?", 
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_book_3 = {
    "id" : "llyfr3", 
    "name" : "Trydydd llyfr", 
    "description" : "Mae'r llyfr yma yn edrych fel yr un trydydd mewn cyfres?", 
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_book_4 = {
    "id" : "llyfr4", 
    "name" : "Pedwerydd llyfr", 
    "description" : "Mae'r llyfr yma yn edrych fel yr un olaf mewn cyfres??", 
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_lamp = { 
    "id" : "lamp", 
    "name" : "Lamp metal trwm", 
    "description" : "Lamp trwm arian a ddarganfodwyd ar y llawr.",
    "pick_up" : True,
    "move" : False,
    "moved" : False
}

item_bookshelf = {
    "id" : "silff",
    "name" : "Silff lyfrau llychlyd",
    "description" : "Rydych yn archwilio’r sielff lyfrau, mae yna niferoedd o lyfrau yno. Pob un efo gweoedd corynnod arnynt… heb law am 4?",
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

items_combinations = {
    "bandaged walking cane": {
        "components": [item_walking_cane, item_bandages],

        "output": item_bandaged_cane,
    },

    "improvised hammer": {
        "components": [item_bandaged_cane, item_hammer_head],

        "output": item_improvised_hammer,
    },

    "bandaged hammer head": {
        "components": [item_bandages, item_hammer_head],

        "output": item_bandaged_hammer,
    },

    "make shift hammer": {
        "components": [item_bandaged_hammer, item_walking_cane],

        "output": item_make_shift_hammer,
    },
}
