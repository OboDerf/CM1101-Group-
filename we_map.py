from items import *

room_exit = {
    "name" : "ALLANFA"

    "description": "",

    "exits" : {},

    "items" : [],

    "completed" = False,

}

room_reception = {
    "name": "Prif Derbynfa yr Ysbyty",

    "description": "",

    "exits": {"gogledd": "Fferyllfa", "de":"Caffi", "dwyrain":"Coridor", "gorllewin":"Allanfa",},

    "items": [],

    "completed" = False,
    
}

room_hallway = {
    "name": "Coridor",

    "description":
    """Hyn yw'r coridor o'r prif derbynfa. Mae'n eithaf tywyll, beth sydd lawr fan hyn?"""

    "exits": {"gogledd":"Ystafell Archwiliad", "de":"Lolfa Doctoriaid", "gorllewin":"Prif Derbynfa", "dwyrain":"Ystafell Disgwyl",},

    "items": [],

    "completed" = False,

}

room_waiting_room = {
    "name": "Ystafell Disgwyl",
    
    "description": "",

    "exits": {"gogledd":"Ystafell Pelydr X", "de":"Ystafell Llawdriniaeth", "gorllewin":"Coridor", },

    "items": [],

    "completed" = False,
    
}

room_surgery = {
    "name" : "Ystafell Llawdriniaeth",

    "description": "",

    "exits": {"gogledd":"Ystafell Disgwyl"},

    "items": [],

    "completed" = False,
}

room_cafe = {
    "name" : "Caffi",

    "description": "",

    "exits": {"gogledd" : "Prif Derbynfa",}

    "items" : []

    "completed" = False,

}

room_pharmacy = {
    "name" : "Fferyllfa",

    "description" : "",

    "exits": {"de":"Prif Derbynfa",}

    "items" : []

    "completed" = False,

}

room_exam = {
    "name" : "Ystafell Archwiliad",

    "description" : "",

    "exits" : {"de" : "Coridor",}

    "items" : []

    "completed" = False,

}

room_doctors_lounge = {
    "name" : "Lolfa Doctoriaid",

    "description" : "",

    "exits" : {"gogledd":"Coridor",},

    "items" : []

    "completed" = False,
}

room_xray = {
    "name" : "Ystafell Pelydr X",

    "description" : "",

    "exits" : {"de" : "Ystafell Disgwyl"}

    "items" : []

    "completed" = False,

}

rooms = {
    "ALLANFA" : room_exit
    "Prif Derbynfa yr Ysbyty" : room_reception,
    "Coridor" : room_hallway,
    "Ystafell Disgwyl" : room_waiting_room,
    "Ystafell Llawdriniaeth" : room_surgery,
    "Caffi" : room_cafe,
    "Fferyllfa" : room_pharmacy,
    "Ystafell Archwiliad" : room_pharmacy,
    "Lolfa Doctoriaid" : room_doctors_lounge,
    "Ystafell Peledr X" : room_xray,
    }
    
