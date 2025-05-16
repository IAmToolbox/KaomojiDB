# KaomojiDB
# A project by Toolbox

# This is the main file, where everything comes together

import os
from data_manip import *

def init():
    if not os.path.isdir("data"):
        os.mkdir("data")
    if os.path.isfile("data/database.json"):
        print("Database found!")
        load_database()
    else:
        response = input("Database not found. Create new database? (Y/N): ")
        match response:
            case "Y":
                print(":)")
                overwrite_json()
                load_database()
            case "N":
                print(":(")
                exit()
            case _:
                raise Exception("Invalid response...")



def main():
    print("Welcome to KaomojiDB. This is just a placeholder message for now.")
    init()
    while True:
        main_menu_choice = input("What would you like to do? Please input a number to select an option.\n1. View current database\n2. Search for kaomoji\n3. Add new kaomoji to database\n4. Reset database\n5. Save and exit program\n")
        match main_menu_choice:
            case "1":
                print("This is the current database:")
                #TODO Make sure this is pretty-printed in the future. Can't have giant databases in a single line
                print_json()
            case "2":
                search_item()
            case "3":
                add_item()
            case "4":
                reset_data()
            case "5":
                write_json()
                print("Goodbye!")
                exit()
            case _:
                raise Exception("Invalid main menu choice")

main()