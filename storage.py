import json
import os

filename = "expenses.json"

# ------- Load Function -------
def load_expenses():

    # Checks if a json file doesn't exist therefore creating one and returning a python object(i.e. list)
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump([], file, indent=4)
            return []
    
    # Checks if the json file exist thereby reading from the to a python  object(i.e. [{...}, {...}])
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)

# ---- Save Function -------
def save_expenses(expenses):

    # Recieves an expense argument and save it to the json file in an indented format
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)