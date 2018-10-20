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

    "exits": {"north": "Pharmacy", "south":"Patients Room", "east":"Hallway", "west" : "EXIT",},

    "items": [],

    "completed" : False,

    "puzzle" : "N/A"    

}

room_hallway = {
    "name": "Hallway",

    "description":
    """This is the hallway leading from the reception. I wonder what's down here?""",

    "exits": {"north":"Examination Room", "south":"Doctors Lounge", "west":"Hospital Reception", "east":"Waiting Room"},

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

    "description": "",

    "exits": {"north" : "Hospital Reception"},

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

    "exits" : {"south" : "Hallway"},

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
