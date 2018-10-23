## ITEM TEMPLATE AS FOLLOWS

##item_template = {
##    "id": "",
##
##    "name": "",
##
##    "description":
##    """TEXT HERE""",
##
##    "pick_up": True / False, (Can it be picked up?)
##
##    "move": True / False, (Can it be picked up?)
##
##    "moved": False
##}

item_make_shift_hammer = {
    "id": "makeshift",
    "name": "Make shift hammer",
    "description": """A deadly weapon, were its head any sturdier.""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_bandaged_hammer = {
    "id": "bandagedhammer",
    "name": "Bandaged hammer head",
    "description": """A blow softened. The purpose is lost on you.""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_improvised_hammer = {
    "id": "improvhammer",
    "name": "Improvised Hammer",
    "description": """The right tool to forge the path.""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_bandaged_cane = {
    "id": "bandagedcane",
    "name": "Bandages walking cane",
    "description": """Given new life. A step towards hope.""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_scissors = {
    "id": "scissors",
    "name": "A pair of scissors",
    "description": """Stainless steel. The bright, reflective gleam not representing its troubled history.""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_hammer_head = {
    "id": "hammerhead",
    "name": "The head of a hammer",
    "description": """Serperation from purpose. Rusted with age. From it some might see greater meaning.""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_bandages = {
    "id": "bandages",
    "name": "A roll of bandages",
    "description": """Knotted together for a reason lost to madness.""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_walking_cane = {
    "id": "cane",
    "name": "A walking cane",
    "description": """Broken under the weight of self-preservation.""",
    "pick_up": True, 
    "move": False, 
    "moved": False
}


item_book_1 = {
    "id" : "book1",
    "name" : "First book",
    "description" : "This book looks like the first of a series?",
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_book_2 = {
    "id" : "book2",
    "name" : "Second book",
    "description" : "This book looks like the second of a series?",
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_book_3 = {
    "id" : "book3",
    "name" : "Third book",
    "description" : "This book looks like the third of a series?",
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_book_4 = {
    "id" : "book4",
    "name" : "Fourth book",
    "description" : "This book looks like the final book of a series?",
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_lamp = {
    "id" : "lamp",
    "name" : "Heavy metalic lamp",
    "description" : "A heavy silver lamp that you found on the floor",
    "pick_up" : True,
    "move" : False,
    "moved" : False
}

item_bookshelf = {
    "id" : "bookshelf",
    "name" : "A dusty bookshelf",
    "description" : "Here you see an array of books, all covered in cobwebs.. apart from 4?",
    "pick_up" : False,
    "move" : False,
    "moved" : False
}



# Any new item combinations are added here in this format
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
