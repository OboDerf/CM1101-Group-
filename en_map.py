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

    "description": "Even in its with its lights cold and facilities, \nthere still glows the faintest amount of hope",

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

    "exits": {"north":"X-Ray Room", "south":"Surgery Room", "west":"Hallway"},

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

    "exits": {"south" : "Hallway"},

    "items" : [item_lamp, item_bookshelf],

    "completed" : False,

    "puzzle" : "patients"

}

room_pharmacy = {
    "name" : "Pharmacy",

    "description" : """As you enter the pharmacy you are greeted by a gigantic mass of plastic containers that had clearly been emptied
in a hurry. The room is dark and dirty, with a single lightbulb flickering occasionally. Broken shelves on both
sides of the room hold the remains of the merchandise that was previously sold at the pharmacy. A snapped pair
of scissors hold up a sign that reads. “NO LOOTING”. This sign had obviously been ignored at the start of the
outbreak. You take note of the ALARM system, which looks to not yet have been triggered. Tread cautious. 

Across the room from the sign was the pharmacy counter, on the counter is a small roll of bandages that look like
they’ve been knotted together. Beyond the counter is where the containers for the pharmacy’s prescription
medicines were stored. All but one of the plastic boxes have been broken into using the head of a hammer that
lies on the floor next in the remnants of the boxes.  A single half of a walking cane lies on a hook behind the
counter, shards of wood pepper the flood around the counter.  
""",

    "exits": {"south":"Hospital Reception"},

    "items" : [item_scissors, item_hammer_head, item_bandages, item_walking_cane],

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
    "X-Ray Room" : room_xray
    }
