# This file will be used for any functions that handle data manipulation in the database

import json

def print_json():
    with open("data/database.json", encoding="utf-8") as j:
        raw_json = json.load(j)
    print(raw_json)

def write_json():
    test_dictionary = {"smiley": ":)"}
    json_object = json.dumps(test_dictionary, indent=4)
    with open("data/database.json", "w", encoding="utf-8") as j:
        j.write(json_object)

def overwrite_json():
    empty_dictionary = {}
    json_object = json.dumps(empty_dictionary)
    with open("data/database.json", "w", encoding="utf-8") as j:
        j.write(json_object)