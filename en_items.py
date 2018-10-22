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

item_example = {
    "id": "example",
    
    "name": "an example item",

    "description": "The description of the example item",

    "pick_up": True,

    "move": True,

    "moved": False
    
}

item_example_two = {
    "id": "exampletwo",

    "name": "the second example item",

    "description": "The description of the exampletwo item",

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
    "example_combined": {
        "components": [item_example, item_example_two],

        "output": item_combined_example,
    }

}
