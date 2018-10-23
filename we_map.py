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

    "description": "Even in its with its lights cold and facilities, \nthere still glows the faintest amount of hope",# Needs Translation

    "exits": {"gogledd": "Fferyllfa", "de":"Ystafell Archwiliad", "dwyrain":"Coridor", "gorllewin":"ALLANFA"},

    "items": [],

    "completed" : False,

    "puzzle" : "N/A"
    
}

room_hallway = {
    "name": "Coridor",

    "description":
    """Hyn yw'r coridor o'r prif derbynfa. Mae'n eithaf tywyll, beth sydd lawr fan hyn?""",

    "exits": {"gogledd":"Ystafell Claf", "de":"Lolfa Doctoriaid", "gorllewin":"Prif Derbynfa yr Ysbyty", "dwyrain":"Ystafell Disgwyl"},

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
    "name" : "Ystafell Claf",

    "description": "",

    "exits": {"de" : "Coridor"},

    "items" : [],

    "completed" : False,

    "puzzle" : "patients"

}

room_pharmacy = {
    "name" : "Fferyllfa",

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
""", # Needs Translation

    "exits": {"de":"Prif Derbynfa yr Ysbyty"},

    "items" : [item_scissors, item_hammer_head, item_bandages, item_walking_cane],

    "completed" : False,

    "puzzle" : "pharmacy"

}

room_exam = {
    "name" : "Ystafell Archwiliad",

    "description" : "",

    "exits" : {"gogledd" : "Ptif Derbynfa yr Ysbyty"},

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
    "Ystafell Claf" : room_patients,
    "Fferyllfa" : room_pharmacy,
    "Ystafell Archwiliad" : room_exam,
    "Lolfa Doctoriaid" : room_doctors_lounge,
    "Ystafell Peledr X" : room_xray,
    }
    
