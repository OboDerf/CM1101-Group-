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
    "id": "scissors",# needs translating
    "name": "A pair of scissors",# needs translating
    "description": """Stainless steel. The bright, reflective gleam not representing its troubled history.""",# needs translating
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_hammer_head = {
    "id": "hammerhead",# needs translating
    "name": "The head of a hammer",# needs translating
    "description": """Serperation from purpose. Rusted with age. From it some might see greater meaning.""",# needs translating
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_bandages = {
    "id": "bandages",# needs translating
    "name": "A roll of bandages",# needs translating
    "description": """Knotted together for a reason lost to madness.""",# needs translating
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_walking_cane = {
    "id": "cane",# needs translating
    "name": "A walking cane",# needs translating
    "description": """Broken under the weight of self-preservation.""",# needs translating
    "pick_up": True, 
    "move": False, 
    "moved": False
}

item_book_1 = {
    "id" : "book1", # needs translating
    "name" : "First book", # needs translating
    "description" : "This book looks like the first of a series?", # needs translating
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_book_2 = {
    "id" : "book2", # needs translating
    "name" : "Second book", # needs translating
    "description" : "This book looks like the second of a series?", # needs translating
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_book_3 = {
    "id" : "book3", # needs translating
    "name" : "Third book", # needs translating
    "description" : "This book looks like the third of a series?", # needs translating
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_book_4 = {
    "id" : "book4", # needs translating
    "name" : "Fourth book", # needs translating
    "description" : "This book looks like the final book of a series?", # needs translating
    "pick_up" : False,
    "move" : False,
    "moved" : False
}

item_lamp = { 
    "id" : "Lamp", # needs translating
    "name" : "Heavy metalic lamp", # needs translating
    "description" : "A heavy silver lamp that you found on the floor", # needs translating
    "pick_up" : True,
    "move" : False,
    "moved" : False
}

item_bookshelf = {
    "id" : "Bookshelf", # needs translating
    "name" : "A dusty bookshelf", # needs translating
    "description" : "Here you see an array of books, all covered in cobwebs.. apart from 4?", # needs translating
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
