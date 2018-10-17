from items import *

room_exit = {
    "name" : "EXIT"

    "description": "",

    "exits" : {},

    "items" : [],

    "completed" = False,

}

room_reception = {
    "name": "Hospital ReceptCoion",

    "description": "",

    "exits": {"north": "Pharmacy", "south":"Cafe", "east":"Hallway", "west" : "EXIT",},

    "items": [],

    "completed" = False,

}

room_hallway = {
    "name": "Hallway",

    "description":
    """This is the hallway leading from the reception. I wonder what's down here?"""

    "exits": {"north":"Examination room", "south":"Doctors Lounge", "west":"Reception", "east":"Waiting Room",},

    "items": [],

    "completed" = False,

}

room_waiting_room = {
    "name": "Waiting Room",
    
    "description": "",

    "exits": {"north":"X-Ray Room", "south":"Surgery Room", "west":"Hallway", },

    "items": [],

    "completed" = False,

}

room_surgery = {
    "name" : "Surgery Room",
    "description": "",

    "exits": {"north":"Waiting Room"},

    "items": [],

    "completed" = False
    
}

room_cafe = {
    "name" : "Cafe",

    "description": "",

    "exits": {"north" : "Reception",}

    "items" : []

    "completed" = False,

}

room_pharmacy = {
    "name" : "Pharmacy",

    "description" : "",

    "exits": {"south":"Reception",}

    "items" : []

    "completed" = False,

}

room_exam = {
    "name" : "Examination Room",

    "description" : "",

    "exits" : {"south" : "Hallway",}

    "items" : []

    "completed" = False,

}

room_doctors_lounge = {
    "name" : "Doctors Lounge",

    "description" : "",

    "exits" : {"north":"Hallway",},

    "items" : []

    "completed" = False,
}

room_xray = {
    "name" : "X-Ray Room",

    "description" : "",

    "exits" : {"south" : "Waiting Room"}

    "items" : []

    "completed" = False,

}

rooms = {
    "EXIT" : room_exit
    "Hospital Reception" : room_reception,
    "Hallway" : room_hallway,
    "Waiting Room" : room_waiting_room,
    "Surgery Room" : room_surgery,
    "Cafe" : room_cafe,
    "Pharmacy" : room_pharmacy,
    "Examination Room" : room_pharmacy,
    "Doctors Lounge" : room_doctors_lounge,
    "X-Ray Room" : room_xray,
    }
    
    
    


