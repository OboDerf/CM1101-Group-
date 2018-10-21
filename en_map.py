from en_items import *

room_exit = {
    "name" : "EXIT",

    "description": "",

    "exits" : {},

    "items" : [],

    "completed" : False,

    "puzzle" : "N/A"

}

room_reception = {
    "name": "Hospital Reception",

    "description": "",

    "exits": {"north": "Pharmacy", "south":"Examination Room", "east":"Hallway", "west" : "EXIT"},

    "items": [],

    "completed" : False,

    "puzzle" : "N/A"    

}

room_hallway = {
    "name": "Hallway",

    "description":
    """This is the hallway leading from the reception. I wonder what's down here?""",

    "exits": {"north":"Patients Room", "south":"Doctors Lounge", "west":"Hospital Reception", "east":"Waiting Room"},

    "items": [],

    "completed" : False,

    "puzzle" : "N/A"

}

room_waiting_room = {
    "name": "Waiting Room",
    
    "description": "",

    "exits": {"north":"X-Ray Room", "south":"Surgery Room", "west":"Hallway", "east": "Example Room"},

    "items": [],

    "completed" : False,

    "puzzle" : "N/A"

}

room_surgery = {
    "name" : "Surgery Room",
    "description": "",

    "exits": {"north":"Waiting Room"},

    "items": [],

    "completed" : False,

    "puzzle" : "surgery"
    
}

room_patients = {
    "name" : "Patients Room",

    "description":
    """
You walk in to a room, it looks like it belongs to a child. The room’s a mess like the rest of the hospital.
Papers, files, lamps and broken glass all over the floor. Moss forming on the dirty floor. The walls painted
blue with pink pen markings along it. A chalk window marked above a low metal bed. 
On the left of the room you see a small bookshelf. Above the bookshelf are a few paintings sellotaped to the wall,
all pictures of different buildings, something about an outbreak?  All paintings have 2431 painted on the bottom
right corner. 
In the far-right corner of the room, you see an old woman sat on the floor, her head in her hands. You hear a
quiet murmur, a repeated line “I told them, I tried to warn them”. The woman, wearing a black necklace, seems to
have gotten used to the smell of this forsaken place.
""",

    "exits": {"north" : "Hallway"},

    "items" : [],

    "completed" : False,

    "puzzle" : "patients"

}

room_pharmacy = {
    "name" : "Pharmacy",

    "description" : "",

    "exits": {"south":"Hospital Reception"},

    "items" : [],

    "completed" : False,

    "puzzle" : "pharmacy"

}

room_exam = {
    "name" : "Examination Room",

    "description" : "",

    "exits" : {"North" : "Hospital Reception"},

    "items" : [],

    "completed" : False,

    "puzzle" : "exam"

}

room_doctors_lounge = {
    "name" : "Doctors Lounge",

    "description" : "",

    "exits" : {"north":"Hallway"},

    "items" : [],

    "completed" : False,

    "puzzle" : "doctors"
}

room_xray = {
    "name" : "X-Ray Room",

    "description" : "",

    "exits" : {"south" : "Waiting Room"},

    "items" : [],

    "completed" : False,

    "puzzle" : "xray"

}

room_example = { # A temp room for a temp puzzle
    "name" : "Example Room",

    "description" : """This is a test room with three simple puzzle.
First you must move examplemove,
Then you must combine example and exampletwo,
Then you must use examplecombine on the room,
You'll notice there's still an exampletwo. User example combine on it for the key
""",

    "exits" : {"west" : "Waiting Room"},

    "items" : [item_example, item_example_two, item_example_move],

    "completed" : False,

    "puzzle" : "example"

}

rooms = {
    "EXIT" : room_exit,
    "Hospital Reception" : room_reception,
    "Hallway" : room_hallway,
    "Waiting Room" : room_waiting_room,
    "Surgery Room" : room_surgery,
    "Patients Room" : room_patients,
    "Pharmacy" : room_pharmacy,
    "Examination Room" : room_exam,
    "Doctors Lounge" : room_doctors_lounge,
    "X-Ray Room" : room_xray,
    "Example Room" : room_example
    }
