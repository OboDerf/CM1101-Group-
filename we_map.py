# These three are skeletons that I needed to create part of game.py. Expand at your leasure
exit_room = {
    "name": "Exit Room",

    "description": "The game ending room, need to have the keys",

    "exits": {"west": "Reception"}
}    

reception = {
    "name": "Derbynfa",

    "exits": {"east": "Corridor West", "west": "Exit"}
}

corridor_west = {
    "name": "Coridor West",

    "exits": {"east": "Corridor East", "west": "Reception"}
}

corridor_east = {
    "name": "Coridor East",

    "exits": {"west": "Corridor West"}
}



rooms = { # When you append, make sure this is bot of the file
    "Exit Room": exit_room,
    "Reception": reception,
    "Corridor West": corridor_west,
    "Corridor East": corridor_east
    
}
