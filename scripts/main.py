# KaomojiDB
# A project by Toolbox

# This is the main file, where everything comes together

import os
from data_manip import *

def init():
    if not os.path.isdir("data"):
        os.mkdir("data")
    if os.path.isfile("data/database.json"):
        print("Database loaded!")
    else:
        response = input("Database not found. Create new database? (Y/N)")
        match response:
            case "Y":
                print(":)")
                overwrite_json()
            case "N":
                print(":(")
                exit()
            case _:
                raise Exception("Invalid response...")



def main():
    print("Welcome to KaomojiDB. This is just a placeholder message for now.")
    init()
    print_json()

main()