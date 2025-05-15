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
        main_menu_choice = input("What would you like to do? Please input a number to select an option.\n1. View current database\n2. Add new kaomoji to database\n3. Reset database\n4. Exit program\n")
        match main_menu_choice:
            case "1":
                print("This is the current database:")
                #TODO Make sure this is pretty-printed in the future. Can't have giant databases in a single line
                print_json()
            case "2":
                add_item()
            case "3":
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
            case "4":
                print("Goodbye!")
                exit()
            case _:
                raise Exception("Invalid main menu choice")

main()