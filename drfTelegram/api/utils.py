from functools import wraps
import json

MF_FIELDS = (
    "message_from_id",
    "message_from_is_bot",
    "message_from_first_name",
    "message_from_username",
    "message_chat_id",
    "message_chat_title",
    "message_chat_type",
    "message_date",
    "message_text",
    "message_entities_type"
)

def rename_dict(dict, parent):
    ret_dict = {}
    for k, v in dict.items():
        if not type(v) == type(dict):
            rename = parent + k
            ret_dict[rename] = v

def dict_to_first_level(dict):
    ret_dict = {}
    print("empiezo", dict)
    for k, v in dict.items():
        print("entro for",k,v)
        if not type(v) == type(dict):
            print("es valor")
            ret_dict[k].append({k,v})
        else:
            
            print("contiene grupo")
            dict_to_first_level(v)
            
    return ret_dict

def filter_json(encoded_json, filter):
    ret_dict = {}
    json_dict = json.loads(encoded_json)
    first_level_dict = dict_to_first_level(json_dict)
    print("filter",first_level_dict)
    for k, v in first_level_dict.items():
        print("for",k,v)
        if k in filter:
            ret_dict.append("if",{k, v})
            print(k,v)
    return ret_dict

