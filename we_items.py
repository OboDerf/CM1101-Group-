item_example = {
    "id": "example",
    
    "name": "an example item",

    "description":
    """Wait, hang on, you shouldn't be seeing this.
Hmmm... Try telling Kai he's an idiot. That normally fixes these things.""",

    "pick_up": True,

    "move": True,

    "moved": False
    
}

item_example_two = {
    "id": "exampletwo",

    "name": "the second example item",

    "description":
    """This is getting out of hand, now there's two of them!""",

    "pick_up": True,

    "move": False,

    "moved": False
}

item_combined_example = {
    "id": "examplecombined",

    "name": "a combination of the two example items",

    "description": "Purely for test purposes.",

    "pick_up": True,

    "move": True,

    "moved": False
}

item_example_move = {
    "id": "examplemove",

    "name": "something to test the move function",

    "description": "The floor boards bend at how heavy this is, but not enough to stop you moving it.",

    "pick_up": False,

    "move": True,

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
    "example_combined": {
        "components": [item_example, item_example_two],

        "output": item_combined_example,
    }

}
