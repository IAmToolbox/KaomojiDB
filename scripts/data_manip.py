# This file will be used for any functions that handle data manipulation in the database

import json
from classes import Database

database = Database(None)

def load_database():
    with open("data/database.json", encoding="utf-8") as j:
        raw_json = json.load(j)
        database.database = raw_json
    print("Database successfully loaded!")
    
def add_item():
    new_kaomoji = input("Please paste your new kaomoji:")
    kaomoji_mood = input("What mood does this kaomoji represent?:")
    kaomoji_name = input("Give this kaomoji a name:")
    database.database[new_kaomoji] = (kaomoji_name, kaomoji_mood)
    print("Successfully added kaomoji!")

def search_item():
    found_items = []
    search_by = input("Search by mood or by name? (M/N): ")
    match search_by:
        case "M":
            search_query = input("Which mood do you want to search for?\n")
            for item in list(database.database.keys()):
                if search_query in database.database[item][1]:
                    found_items.append(item)
        case "N":
            search_query = input("What's the name of the kaomoji you want to search for?\n")
            for item in list(database.database.keys()):
                if search_query in database.database[item][0]:
                    found_items.append(item)
    #TODO Make search case-insensitive... just in case
    if len(found_items) != 0:
        print("Found the following kaomoji:")
        for item in found_items:
            print(item)
    else:
        print("No kaomoji found...")

def reset_data():
    response = input("Are you sure you want to reset database? This will delete all kaomoji stored within! (Y/N): ")
    match response:
        case "Y":
            overwrite_json()
            print("Database reset. Goodbye.")
            exit()
        case "N":
            print("Database has been kept as is.")
        case _:
            raise Exception("Invalid response...")

def print_json():
    print(database.database)

def write_json():
    json_object = json.dumps(database.database, indent=4)
    with open("data/database.json", "w", encoding="utf-8") as j:
        j.write(json_object)

def overwrite_json():
    empty_dictionary = {}
    json_object = json.dumps(empty_dictionary)
    with open("data/database.json", "w", encoding="utf-8") as j:
        j.write(json_object)