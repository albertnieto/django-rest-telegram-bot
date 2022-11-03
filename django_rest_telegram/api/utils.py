from functools import wraps
import json

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

def is_parent(value):
    return isinstance(value, dict)

def dict_to_first_level(d, parent_name=None, rec_dict=None):
    ret_dict = {}

    if rec_dict: ret_dict = {**ret_dict, **rec_dict} 

    for k, v in d.items():

        if isinstance(v, dict):
            if parent_name: k = f'{parent_name}_{k}'

            _recursive, _, _ = dict_to_first_level(v, k, ret_dict)
            ret_dict = {**ret_dict, **_recursive} 

        else:
            if parent_name:
                k = f'{parent_name}_{k}'
            ret_dict[k] = v

    return ret_dict, parent_name, rec_dict

def filter_json(encoded_json, filter):
    ret_dict = {}
    json_dict = json.loads(encoded_json)
    first_level_dict, _, _ = dict_to_first_level(json_dict)

    for k, v in first_level_dict.items():
        if k in filter:
            ret_dict[k] = v

    return ret_dict

