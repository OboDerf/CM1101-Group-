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

items_combinations = {
    "example_combined": {
        "components": [item_example, item_example_two],

        "output": item_combined_example,
    }

}
