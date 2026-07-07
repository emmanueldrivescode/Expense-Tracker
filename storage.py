import json
import os

filename = "expenses.json"

def load_expenses():
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump([], file, indent=4)
            return []
        
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)

def save_expenses(expenses):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)