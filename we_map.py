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

    "description":
    """Hyd yn oed efo'r goleuadau yn tywyllu,\n mae yna dal gobaith llesmair.""",

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

# needs translation
room_surgery = {
    "name" : "Ystafell Llawdriniaeth",

    "description": """The pungent smell coming out of the room sparked your interest and chose to enter. You have now entered the surgery room. 

Lights are flickering. Looks like the virus hit them during an operation. The room is covered with surgical equipment but mostly in blood and as it seems it came from the patient lying down on the bed with his stomach opened up”. 
There is a doctor on the floor against the wall. Strangely he does not look infected nor hurt. On the other side of the room there are lockers. Others are open and empty with broken vials below them covered in spilled medicine, others are just closed. Hopefully, there is still something left inside.
As you approach into the room, you hear the automatic doors behind you closing. You try to open the doors again without results. It seems like only staff could use this room and the doors once closed can only be opened by a staff card. """,


    "exits": {"gogledd":"Ystafell Disgwyl"},

    "items": [item_patient, item_doctorBody, item_lockers],

    "completed" : False,

    "puzzle" : "surgery"
}

room_patients = {
    "name" : "Ystafell Claf",

    "description": """
Rydych yn cerdded mewn i ystafell, mae’n edrych fel un plentyn. Mae’r ystafell yn hynod o flêr, union fel gweddill yr ysbyty.
Efo papur, ffeiliau, lampiau a gwydr ar hyd y llawr. Moss yn tyfu ar hyd y llawr. Mae’r waliau wedi cael ei beintio’n las efo
marc pinc (fel un allan o ben ffelt) ar hyd y waliau. Uwch ben gwely mhetal, mae yno ffenestr smal wedi cael ei ddylunio yn sialc.

I’r chwith o’r ystafell, rydych yn gweld silff lyfrau bach, efo paentiadau wedi cael ei sticio i’r wal efo selotep. Mae’r lluniau
yn cynnwys adeiladau wedi eu difetha, rhywbeth am gychwyn firws? Mae pob llun efo’r rhifau 2431 ar y cornel gwaelod.

Yn yr ochr arall o’r ystafell rydych yn gweld hen ddynas yn eistedd ar y llawr, efo’i wyneb yn ei ddulo. Rydych yn clywed hi’n sibrwd
yn ailadroddus “Dywedais wrthyn, nes i drio rhybuddio nhw”. Mae’r ddynas, sydd yn gwisgo cadwyn du, yn edrych fel bod hi wedi arfer i
fyw yn yr arogl drewchyd yma.
""",

    "exits": {"de" : "Coridor"},

    "items" : [item_lamp, item_bookshelf],

    "completed" : False,

    "puzzle" : "patients"

}

room_pharmacy = {
    "name" : "Fferyllfa",

    "description" :"""
Fel rydych yn cerdded mewn i’r fferyllfa, rydych yn gweld llwythi o gynhwysyddion plastig sydd wedi cael eu gwagio mewn brys.
Mae’r ystafell yn dywyll ac yn fudr, efo un bwlb yn fflicio ar adegau. Mae yna silffoedd wedi torri ar y ddwy ochr o’r ystafell
yn dal y gweddillion o’r cynhyrchion oedd yn cael ei werthu yma. Mae yno siswrn sydd yn dal arwydd i fyny sydd yn dweud “PAID DWYN”.
Mae’r arwydd yma wedi cael ei anwybyddu ers y cychwyn o’r firws. Mae yna system larwm yma, dydy’r system heb di cael ei setio eto.
Felly bydd angen bod yn ddiogel iawn wrth fynd cwmpas yr ystafell.

Ar yr ochr arall o’r ystafell, mae yna gownter sydd efo rhwymynnau arno. Tŷ ôl i’r cownter oedd y feddygaeth oedd yn cael eu darnodi.
Oedd pob un o’r bocsys plastig wedi cael ei dorri heb law am un? Mae’n edrych fel cafodd pob un ei dorri gan ddefnyddio'r pen o
forthwyl sydd ar y llawr o flaenach. Mae yna un hanner o ffon cerdded sydd yn hongian o’r bachau sydd tŷ ôl i’r cownter.
""",

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
    
