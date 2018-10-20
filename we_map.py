from we_items import *

room_exit = {
    "name" : "ALLANFA",

    "description": "",

    "exits" : {},

    "items" : [],

    "completed" : False,

    "puzzle" : "N/A"

}

room_reception = {
    "name": "Prif Derbynfa yr Ysbyty",

    "description": "",

    "exits": {"gogledd": "Fferyllfa", "de":"PATIENTS ROOM", "dwyrain":"Coridor", "gorllewin":"ALLANFA"},

    "items": [],

    "completed" : False,

    "puzzle" : "N/A"
    
}

room_hallway = {
    "name": "Coridor",

    "description":
    """Hyn yw'r coridor o'r prif derbynfa. Mae'n eithaf tywyll, beth sydd lawr fan hyn?""",

    "exits": {"gogledd":"Ystafell Archwiliad", "de":"Lolfa Doctoriaid", "gorllewin":"Prif Derbynfa yr Ysbyty", "dwyrain":"Ystafell Disgwyl"},

    "items": [],

    "completed" : False,

    "puzzle" : "N/A"

}

room_waiting_room = {
    "name": "Ystafell Disgwyl",
    
    "description": "",

    "exits": {"gogledd":"Ystafell Pelydr X", "de":"Ystafell Llawdriniaeth", "gorllewin":"Coridor"},

    "items": [],

    "completed" : False,

    "puzzle" : "N/A"
    
}

room_surgery = {
    "name" : "Ystafell Llawdriniaeth",

    "description": "",

    "exits": {"gogledd":"Ystafell Disgwyl"},

    "items": [],

    "completed" : False,

    "puzzle" : "surgery"
}

room_patients = {
    "name" : "PATIENTS ROOM",

    "description": "",

    "exits": {"gogledd" : "Prif Derbynfa yr Ysbyty"},

    "items" : [],

    "completed" : False,

    "puzzle" : "patients"

}

room_pharmacy = {
    "name" : "Fferyllfa",

    "description" : "",

    "exits": {"de":"Prif Derbynfa yr Ysbyty"},

    "items" : [],

    "completed" : False,

    "puzzle" : "pharmacy"

}

room_exam = {
    "name" : "Ystafell Archwiliad",

    "description" : "",

    "exits" : {"de" : "Coridor"},

    "items" : [],

    "completed" : False,

    "puzzle" : "pharmacy"

}

room_doctors_lounge = {
    "name" : "Lolfa Doctoriaid",

    "description" : "",

    "exits" : {"gogledd":"Coridor"},

    "items" : [],

    "completed" : False,

    "puzzle" : "doctors"
}

room_xray = {
    "name" : "Ystafell Pelydr X",

    "description" : "",

    "exits" : {"de" : "Ystafell Disgwyl"},

    "items" : [],

    "completed" : False,

    "puzzle" : "xray"

}

rooms = {
    "ALLANFA" : room_exit,
    "Prif Derbynfa yr Ysbyty" : room_reception,
    "Coridor" : room_hallway,
    "Ystafell Disgwyl" : room_waiting_room,
    "Ystafell Llawdriniaeth" : room_surgery,
    "PATIENTS ROOM" : room_patients,
    "Fferyllfa" : room_pharmacy,
    "Ystafell Archwiliad" : room_exam,
    "Lolfa Doctoriaid" : room_doctors_lounge,
    "Ystafell Peledr X" : room_xray,
    }
    
