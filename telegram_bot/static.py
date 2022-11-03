import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

REGEX_POLE_FILTERS = {
    "Poleet":r"[pP][oO][lL][eE][eE][tT]",
    "Poeet":r"[pP][oO][eE][eE][tT]",
    "Pole":r".*[pP][oO][lL][eE].*",
    "Oro":r"[oO][rR][oO].*",
    "Plata":r"[pP][lL][aA][tT][aA].*",
    "Bronce":r"[bB][rR][oO][nN][cC][eE].*",
    "Hora":r"[hH][oO][rR][aA].*",
    "Alarma Magnas":r"[aA][lL][aA][rR][mM][aA]\s[mM][aA][ñÑ][aA][sS]",
}

REGEX_POLE_TYPE = {
    "Fracapole":r"fracapole",
    "Pole Canaria":r"pole canaria",
    "Oro Canario":r"oro canario",
    "Subpole Canaria":r"subpole canaria",
    "Plata Canario":r"plata canario",
    "Bronce Canario":r"bronce canario",
    "Hora Pi":r"hora pi",
    "Pole Insomnio":r"pole insomnio",
    "Hora Porro":r"hora porro",
    "Pole Cotizante":r"pole cotizante",
    "Pole Cafelito":r"pole cafelito",
    "Pole Andaluza":r"pole andaluza",
    "Postpole":r"postpole",
    "Prepole":r"prepole",
    "Polerdaka":r"polerdaka",
    "Polerdamen":r"polerdamen",
    "Pole Básica":r"pole básica",
    "Pole Magnas":r"pole magnas",
    "Pole CRX":os.getenv("CRX_REGEX"),
    "Pole Contemporánea":r"pole contemporánea",
    "Pole Letal":r"pole letal",
    "Pole Máxima":r"pole máxima",
    "Pole Mínima":r"pole mínima",
    "Polerdakardamenaka":r"polerdakardamenaka",
    "Polen":r"polen",
    "Pole Ucraniana":r"pole ucraniana",
    "Pole Montero":r"pole montero",
    "Pole Toakiza":r"pole toakiza",
    "Pole Presko":r"pole presko",
    "Pole Pseudo":r"pseudopole",
    "Pole Mistica":r"pole mística",
    "Pole Clásica":r"pole clásica",
    "Pole Eterna":r"pole eterna",
    "Pole Binaria":r"pole binaria",
    "Pole Boix":r"pole boix",
    "Pole Germà":r"pole germà",
    "Pole Fran":r"pole fran",
    **REGEX_POLE_FILTERS,
}

POLE_WITH_COIN = {
    "Binaria":"Germà Coin",
    "Boix":"Germà Coin",
    "Germa":"Germà Coin",
    "Fran":"Triggered Coin",
    "Ucraniana":"Triggered Coin",
    "Montero":"Triggered Coin",
    "Toakiza":"Triggered Coin",
    "Presko":"Triggered Coin",
    "Polen":"CRX Coin",
    os.getenv("CRX"):"CRX Coin",
}

MF_FIELDS = {
    "message_from_id":"tg_user_id",
    "message_from_is_bot":"tg_is_bot",
    "message_from_first_name":"tg_first_name",
    "message_from_username":"tg_username",
    "message_chat_id":"tg_group_id",
    "message_chat_title":"tg_group_title",
    "message_chat_type":"tg_group_type",
    "message_date":"tg_date_time",
    "message_text":"tg_message",
    "message_entities_type":"tg_entity_type",
}

MF_FIELDS_KEYS = MF_FIELDS.keys()

REGEX_FILTERS = {
    **REGEX_POLE_FILTERS,
}

