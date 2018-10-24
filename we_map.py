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

room_surgery = {
    "name" : "Ystafell Llawdriniaeth",
    "description":
    """
Mae'r arogl ofnadwy sydd yn dod allan o'r ystafell yn cynyddu eich ddiddordeb i fynd i fewn. Rydych chi bellach
wedi mynd i fewn i'r ystafell llawdriniaeth.

Mae'r goleuadau yn diflanu ar adegau. Mae'n edrych fel bod yr firws wedi effeithio'r ystafell yma yn ystod llawdriniaeth. Mae'r
ystafell efo niferoedd o offer llawdriniaeth, ond mae mwy afrif efo gwaed arno ac mae'n edrych fel bod yr gwaed wedi ddod o'r corff
sydd ar yr bwrdd, efo'i stumog ar agor.

Mae yna doctor ar y llawr yn pwyso yn erbyn yr wal. Mae'n od, ond nad yw'r doctor yn edrych fel bod o wedi cael ei effeithio neu ei niwedu gan
y firws. Ar yr ochr arall o'r ystafell mae yna cloirau. Mae rhai ar agor efo ffialau wedi cael ei dorri, ac mae rhei eraill dal wedi cloi. Gobeithio
bod yna dal rhyw beth ty fewn.

Fel rydych yn cerddef i fewn i'r ystafell, rydych yn clywed yr drysau awtomatig cau ty ol iddych. Rydych yn trio agor nhw ond does dim gobaith. Mae'n
edrych fel bod yr unig ffordd i agor y drysau yw gan defnyddio cardyn staff.
""",

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

    "description" : """
Gan cerdded mewn i'r ystafell, rydych yn cael sioc i weld bod yr ystafell yn edrych fel dydy o heb cael ei effeithio,
bron iawn fel ystafell newydd. Mae'r ystafell yn fach iawn, ond mae pob dim yn taclus iawn, bydd yn gallu cael ei
ddefnyddio gan doctor rwan… efo tipyn back o waith tynnu llwch.

Mae'r bwrdd archwilio wedi cael ei leoli yn gannol yr ystafell, mae'n edrych yn llwchlud on ddim yn budr nac wedi cael ei
ddifrodi. Mae yna bwrdd sydd efo offer canoloesol sydd wedi cael ei leoli mewn ordor ar y bwrdd.

Fel rydych yn symyd mewn i'r ystafell rydych yn gweld silff efo gwydrau bach arnynt. Rydych yn sylweddoli ogla drewchyd yn
dod trwy eich mwgwd nwy, mae'r arogl yn edrych fel bod yn dod o'r dror odan. Mae'n arogli fel cyrff person wedi marw.
Dydy rhywbeth ddim yn iawn yma...
""",

    "exits" : {"gogledd" : "Ptif Derbynfa yr Ysbyty"},

    "items" : [item_jar, item_chair, item_table],

    "completed" : False,

    "puzzle" : "exam"

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

    "description" : """
Rydych mewn ystafell gwyn llachr efo waliau gwyn ac llawr glas.
MAe yna cyfrifiadur efo sgrin gwydr o amgylch.
Mae yna gwely pren lle bydd yr claf yn gorwedd pan yn cael eu scan. Does yna ddim ffenestri yn yr ystafell.

Mae'r ffiol ty ol i'r ateb i'r rhidyll:
Mae gen i ddinasoedd, ond dim tai. Mae gen i mynyddoedd, ond dim coed. Mae gen i dwr, ond dim pysgod. Beth ydw i?
""",

    "exits" : {"de" : "Ystafell Disgwyl"},

    "items" : [item_Cabinet, item_computer, item_map, item_glasses, item_desk, item_instrumunts, item_machines],

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
    
