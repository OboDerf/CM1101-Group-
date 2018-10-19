from en_items import *

room_exit = {
    "name" : "EXIT",

    "description": "",

    "exits" : {},

    "items" : [],

    "completed" : False

}

room_reception = {
    "name": "Hospital Reception",

    "description": "",

    "exits": {"north": "Pharmacy", "south":"Cafe", "east":"Hallway", "west" : "EXIT",},

    "items": [item_example, item_example_two],

    "completed" : False

}

room_hallway = {
    "name": "Hallway",

    "description":
    """This is the hallway leading from the reception. I wonder what's down here?""",

    "exits": {"north":"Examination room", "south":"Doctors Lounge", "west":"Hospital Reception", "east":"Waiting Room"},

    "items": [],

    "completed" : False

}

room_waiting_room = {
    "name": "Waiting Room",
    
    "description": "",

    "exits": {"north":"X-Ray Room", "south":"Surgery Room", "west":"Hallway", },

    "items": [],

    "completed" : False

}

room_surgery = {
    "name" : "Surgery Room",
    "description": "",

    "exits": {"north":"Waiting Room"},

    "items": [],

    "completed" : False
    
}

room_cafe = {
    "name" : "Cafe",

    "description": "",

    "exits": {"north" : "Hospital Reception"},

    "items" : [],

    "completed" : False

}

room_pharmacy = {
    "name" : "Pharmacy",

    "description" : "",

    "exits": {"south":"Hospital Reception"},

    "items" : [],

    "completed" : False

}

room_exam = {
    "name" : "Examination Room",

    "description" : "",

    "exits" : {"south" : "Hallway"},

    "items" : [],

    "completed" : False

}

room_doctors_lounge = {
    "name" : "Doctors Lounge",

    "description" : "",

    "exits" : {"north":"Hallway"},

    "items" : [],

    "completed" : False
}

room_xray = {
    "name" : "X-Ray Room",

    "description" : "",

    "exits" : {"south" : "Waiting Room"},

    "items" : [],

    "completed" : False

}

rooms = {
    "EXIT" : room_exit,
    "Hospital Reception" : room_reception,
    "Hallway" : room_hallway,
    "Waiting Room" : room_waiting_room,
    "Surgery Room" : room_surgery,
    "Cafe" : room_cafe,
    "Pharmacy" : room_pharmacy,
    "Examination room" : room_exam,
    "Doctors Lounge" : room_doctors_lounge,
    "X-Ray Room" : room_xray
    }
    
    
# Corridors - needs to be added to welsh map
west_Corridor = {
	"name": "west corridor", # translate this value
	"left": "exit",
	"right": "center",
	"up": room_hallway,
	"down": room_waiting_room
}

center_Corridor = {
	"name": "center corridor",
	"left": "west",
	"right": "east",
	"up": room_reception,
	"down": room_xray
}

east_Corridor = {
	"name": "east corridor",
	"left": "center",
	"up": room_pharmacy,
	"down": room_doctors_lounge
}

exit_Corridor = {
	"name" : "exit",
	"right": "west"
}


corridors = {
	"west": west_Corridor,
	"center": center_Corridor,
	"east": east_Corridor,
	"exit": exit_Corridor
}
