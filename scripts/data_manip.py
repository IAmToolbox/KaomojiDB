# This file will be used for any functions that handle data manipulation in the database

import json
from classes import Database

database = Database(None)

def load_database():
    with open("data/database.json", encoding="utf-8") as j:
        raw_json = json.load(j)
    database.database = raw_json
    print("Database successfully loaded!")
    

def print_json():
    print(database.database)

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